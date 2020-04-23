# wenyang-ltr

## What's This?
An end-to-end tutorial for training an external L2 Ranker on top of Azure Cognitive Search.

## Prerequisites
- An existing [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/) cluster
- Prior background in machine learning, at least at the level of [Machine learning crash course](https://docs.microsoft.com/en-us/learn/paths/ml-crash-course/) or better yet, [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning)

## Installation

1. Download and install the latest version of [Anaconda](https://www.anaconda.com/distribution/#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Clone this repository to your local machine.
    - If on Windows, make sure to open this repo with an Anaconda Command Prompt.
    - If on Linux or OSX, if you didn't add Anaconda to your system `PATH` variable, you'll have to source the Anaconda envrionment manually.
3. Install the conda environment with `conda env create -f environment.yml`. Wait for installation to finish.
4. Activate the environment with `conda activate azs-l2r`.
5. Run Jupyter with your choice of `jupyter notebook` or `jupyter lab`. Navigate to the tutorial at `l2r_msft_docs.ipynb`.


## One-Click Alternative

- For a free, runnable link to the notebook, please click on the Binder button below.
- Please note that MyBinder is a free public service with limited computational resources. Skip the K-Fold cross-validation section if you're running this on Binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://aka.ms/AA877hx)
