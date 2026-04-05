# Homework 09

This directory is for homework 9 of MBS 337, Research Computing in Biology.

## Setup

The tools for this homework involved the creating of a Jupyter notebook and installing the required dependencies, found in requirements.txt.

Use the following to clone the repository:

``` bash
git clone https://github.com/alypham16/mbs337-repo/
cd homework09
```

To create a virtual environment and install required dependencies:

```bash
source myenv/bin/activate
pip install -r requirements.txt
```

To launch a Jupyter notebook:

```bash
jupyter notebook
```

## Exercise Descriptions 

This homework is composed of 4 parts (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework09.html).

1. Data Retrieval
- The UCI Breast Cancer Wisconsin Dataset, which includes several features of cell nuclei from breast cancer biopsies, was utilized and imported from sklearn.

2. Data Preparation
- Involves importing train_test_split from sklearn.model_selection to split the data into training and test sets that is reproducible and maintains roughly the proportion of benign and malignant tumors.

3. Linear Classifier Fitting
- Fits the data to a linear classifier using the Perceptron algorithm that uses a stochastic gradient descent as the optimization algorithm.

4. Validation and Assessment
- Checks the accuracy of the train and test datasets and plots a confusion matrix.

## Miscellaneous
The following non-exercise files are also in the Git directory
- README.md: This file, which contains an overview of the homework09 directory.
- requirements.txt: includes dependencies for the exercise.

## AI Usage

No AI was used for this assignment.