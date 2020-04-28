import json
import os
from pathlib import Path
from pprint import pprint

import pandas as pd
import requests


class azs_msft_docs:
    def __init__(self, judgment_file_path, verbose=False):
        self.judgments = pd.read_csv(judgment_file_path)
        self.judgments = self.judgments.drop(['title'], axis=1)
        self.verbose = verbose

    def get_documents_from_local_folder(self, directory_path):
        directory = os.fsencode(directory_path)
        all_documents = []
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                full_path = str(os.path.join(directory_path, filename))
                with open(full_path) as f:
                    all_documents.append(json.load(f))

        return all_documents

    def _set_schema(self, service_metadata, schema_file="msft_docs_index_schema.json"):
        script_dir = Path(os.path.dirname(__file__))
        schema_path = script_dir / "index_schema" / schema_file
        with open(schema_path, 'r') as f:
            schema_body = json.load(f)
            index_schema = {}
            index_schema.update(schema_body)
            # Overwrite existing name in index schema with user-defined one.
            index_schema["name"] = service_metadata.index_name
        return index_schema

    def create_index(self, service_metadata, schema_file="msft_docs_index_schema.json"):
        index_schema = self._set_schema(service_metadata, schema_file)
        # print(index_schema)

        response = requests.post(
            service_metadata.index_api_uri,
            headers=service_metadata.headers,
            json=index_schema,
            verify=False
        )
        index = response.json()
        return index
