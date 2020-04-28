# wenyang-ltr

## What's This?
- An end-to-end tutorial for training an external L2 Ranker on top of Azure Cognitive Search.

## Who is This For?
- Azure Cognitive Search users who are looking to increase relevance in their search systems.
    - Azure Cognitive Search provides [Scoring Profiles](https://docs.microsoft.com/en-us/azure/search/index-add-scoring-profiles) as a way to boost relevance. This tutorial demonstrates more advanced techniques that can be used if you hit a wall with Scoring Profiles.
- Users interested in enriching their search systems with machine learning.

## Why L2 Ranker?
- Machine learned ranking models are highly effective and battle tested, seeing live use in many search systems, such as Bing, Google, Facebook, Twitter, and Netflix. A good ranking model drastically improves the quality of any given search experience.
- Training and serving a live ranking system involves lots of "gotchas". This tutorial distills the training process down to a simple, yet robust form.

# Setup

## Prerequisites
- An existing [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) cluster

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
