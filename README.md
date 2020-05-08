## What's This?
A tutorial for improving search relevance in applcations baked by Azure Cognitive Search following the [Learning To Rank](https://en.wikipedia.org/wiki/Learning_to_rank) pattern.

## Who is This For?
Azure Cognitive Search users who are looking to improve relevance in their applications. Azure Cognitive Search provides different ways to control search relevance including [Scoring Profiles](https://docs.microsoft.com/en-us/azure/search/index-add-scoring-profiles) and [query term boosting](https://docs.microsoft.com/en-us/azure/search/search-query-lucene-examples#example-5-term-boosting). Those techniques work well in scenarios when indexed content as well as user query patterns don't change frequently and are well understood. In applications where this is not true, Machine Learning based techniques can be used to tune relevance dynamically.

## Why L2 Ranker?
- Machine learned ranking models are highly effective especially in applications that handle a lot of data and user traffic such as Bing, Google, Facebook, Twitter, and Netflix, but can be adopted to all applications where a notion of what's relevant can be defined and observed. Machine Learning based approaches to tune search relevance allow to inject changing information about user behavior and preferences into the ranking model.
- Training and serving a ranking model involves lots of "gotchas". This tutorial describes a simple pattern for doing this with Azure Cognitive Seach as the retrieval engine where reranking happens on the application side.

 ## Table of Contents

 - 
 - 

# Setup

## Prerequisites
- An existing [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) service.

### Optional
- Prior background in machine learning would be good to have. For a hands-on, introductory tutorial, check out [Machine learning crash course](https://docs.microsoft.com/en-us/learn/paths/ml-crash-course/). [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning) is also a great option if you have more time.

## Installation

1. Download and install the latest version of [Anaconda](https://www.anaconda.com/distribution/#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Clone this repository to your local machine.
    - If on Windows, make sure to open this repo with an Anaconda Command Prompt.
    - If on Linux or OSX, if you didn't add Anaconda to your system `PATH` variable, you'll have to source the Anaconda envrionment manually.
3. Install the conda environment with `conda env create -f environment.yml`. Wait for installation to finish.
4. Activate the environment with `conda activate azs-l2r`.
5. Run Jupyter with your choice of `jupyter notebook` or `jupyter lab`. Navigate to the tutorial at `l2r_part1_data_eng.ipynb` and `l2r_part2_experiment.ipynb`.


## One-Click Alternative

- For a free, runnable link to the notebook, please click on the Binder button below.
- Please note that MyBinder is a free public service with limited computational resources. Skip the K-Fold cross-validation section if you're running this on Binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://aka.ms/AA877hx)
 
