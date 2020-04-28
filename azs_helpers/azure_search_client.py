import math
import json
import time
from pprint import pprint

import requests

from .l2r_helper import grouper


class azure_search_client:
    def __init__(self, service_name, endpoint, api_version, api_key, index_name):
        self.service_name = service_name
        self.endpoint = endpoint
        self.api_version = api_version
        self.api_key = api_key
        self.index_name = index_name

    @classmethod
    def from_json(cls, config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        return cls(
            config["service_name"],
            config["endpoint"],
            config["api_version"],
            config["api_key"],
            config["index_name"],
        )

    @property
    def headers(self):
        return {"Content-Type": "application/json", "api-key": self.api_key}

    @property
    def index_api_uri(self):
        return (
            self.endpoint
            + "indexes?api-version="
            + self.api_version
            + "&service="
            + self.service_name
        )

    @property
    def index_doc_count_api_uri(self):
        return (
            self.endpoint
            + "indexes/"
            + self.index_name
            + "/docs/$count?api-version="
            + self.api_version
            + "&service="
            + self.service_name
        )

    @property
    def upload_doc_uri(self):
        return (
            self.endpoint
            + "indexes/"
            + self.index_name
            + "/docs/index?api-version="
            + self.api_version
            + "&service="
            + self.service_name
        )

    @property
    def search_api_uri(self):
        return (
            self.endpoint
            + "indexes/"
            + self.index_name
            + "/docs/search?api-version="
            + self.api_version
            + "&service="
            + self.service_name
            + "&featuresMode=enabled"
        )

    def index_exist(self):
        response = requests.get(
            self.index_api_uri + "&$select=name", headers=self.headers, verify=False
        )

        if response.status_code != 200:
            print("Failed to connect to search service '{0}'. Response code '{1}'".format(self.service_name, response.status_code))
            print(response.text)
            return False
        else:
            print("Succesfully connected to search service '{0}'".format(self.service_name))
            matching_index = [service_index['name'] for service_index in response.json()['value'] if service_index['name'] == self.index_name]
            return len(matching_index) == 1

    def index_documents_count(self):
        response = requests.get(
            self.index_doc_count_api_uri, headers=self.headers, verify=False
        )
        response.encoding = 'utf-8-sig'
        return int(response.text)

    def get_indexes(self):
        response = requests.get(self.index_api_uri, headers=self.headers, verify=False)
        print(response.json())
        return response.json()

    def search(self, body, verbose=False):
        for retry_count in range(5):
            response = requests.post(
                self.search_api_uri, headers=self.headers, json=body, verify=False
            )

            if response.status_code == 200:
                return response.json()["value"]
            else:
                if verbose:
                    print(
                        f"Search request failed with status: {response.status_code}. Sleeping 100ms. Retrying... Retry count so far {retry_count}"
                    )
                time.sleep(0.1)
        print(f"Search request failed with status: {response.status_code} after {retry_count} retries.")

    def upload_doc_batch(self, documents):
        payload = {"value": documents}

        response = requests.post(
            self.upload_doc_uri, headers=self.headers, json=payload, verify=False
        )
        return (payload, response)

    def upload_documents(self, docs, batch_size=1000):
        total_len = len(docs)
        batch_count = math.ceil(total_len / batch_size)
        print("Total {0}, batch count {1}".format(total_len, batch_count))
        payload_response_tuples = []
        for batch_id, batch in enumerate(grouper(docs, batch_size)):
            retry_count = 0
            while True:
                start = batch_id * batch_size
                end = min(start + batch_size, total_len)
                print(f"Uploading items {start} to {end}")
                payload, response = self.upload_doc_batch(list(filter(None, batch)))

                if response.status_code != 200:
                    print(response)
                    retry_count = retry_count + 1
                    time.sleep(retry_count)
                    if retry_count > 10:
                        break
                else:
                    break
                # payload_response_tuples.append((payload, response))
        return payload_response_tuples
