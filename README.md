# Add machine learning to search relevance - Azure Cognitive Search

This tutorial demonstrates the adoption of [Learning To Rank or machine-learning ranking (MLR)](https://en.wikipedia.org/wiki/Learning_to_rank) to improve search relevance in search applications backed by Azure Cognitive Search. A new [featuresMode parameter](https://docs.microsoft.com/rest/api/searchservice/2019-05-06-preview/search-documents#featuresmode) returns statistics that are used to train a ranking model.

This tutorial is for developers who are looking to improve relevance in their Azure Cognitive Search applications. Azure Cognitive Search provides different ways to control search relevance including [scoring profiles](https://docs.microsoft.com/azure/search/index-add-scoring-profiles) and [query term boosting](https://docs.microsoft.com/azure/search/search-query-lucene-examples#example-5-term-boosting). These techniques work well in scenarios where indexed content and user query patterns are relatively static and well understood. In applications where this is not true, machine learning based techniques can be used to tune relevance dynamically.

## Why machine learning for ranking?

Machine learned ranking models are highly effective, especially in applications that handle a lot of data and user traffic, such as Bing, Google, Facebook, Twitter, and Netflix. Ranking models are suitable for applications where a notion of what's relevant can be defined and observed. Machine learning based approaches to tune search relevance allow ever-changing information about user behavior and preferences to be injected into the search experience.

Training and serving a ranking model involves lots of "gotchas". This tutorial describes a simple pattern for doing this with Azure Cognitive Search as the retrieval engine where reranking happens on the application side.

## Getting Started

If you just want to read the code, skip the "Setup" section.
- [Setup](#setup)
- [Part 1: Data Engineering](l2r_part1_data_eng.ipynb)
- [Part 2: Experiment](l2r_part2_experiment.ipynb)
- [Conclusion](conclusion.md)

## Setup

### Prerequisites
- An existing [Azure Cognitive Search](https://azure.microsoft.com/services/search/) service
- Anaconda with Jupyter Notebooks and Python 3.7

#### Optional
- Prior background in machine learning is helpful. For a hands-on, introductory tutorial, check out [Machine learning crash course](https://docs.microsoft.com/learn/paths/ml-crash-course/). [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning) is also a great option if you have more time.

### Installation

1. Download and install the latest version of [Anaconda](https://www.anaconda.com/distribution/#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Clone this repository to your local machine.
    - On Windows, make sure to open this repo with an Anaconda command prompt.
    - On Linux or OSX, if you didn't add Anaconda to your system `PATH` variable, you'll have to source the Anaconda environment manually.
3. Install the conda environment with `conda env create -f environment.yml`. Wait for installation to finish.
4. Activate the environment with `conda activate azs-l2r`.
5. Run Jupyter with your choice of `jupyter notebook` or `jupyter lab`. Navigate to the tutorial at `l2r_part1_data_eng.ipynb` and `l2r_part2_experiment.ipynb`.

### One-Click Alternative

- For a free, runnable link to the notebook, please click on the Binder button below.
- Please note that MyBinder is a free public service with limited computational resources. Skip the K-Fold cross-validation section if you're running this on Binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://aka.ms/AA877hx)
 
