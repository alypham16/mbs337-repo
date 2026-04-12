# Homework 10

This directory is for homework 10 of MBS 337, Research Computing in Biology.

## Setup

Use the following to clone the repository:

``` bash
git clone https://github.com/alypham16/mbs337-repo/
cd homework10
```

To create a virtual environment and install required dependencies:

```bash
source myenv/bin/activate
pip install -r requirements.txt
```
To run the models:

```bash
python3 training.py
python3 inference.py --dataset sample_data.csv
```

## Exercise Descriptions 

This homework is composed of 2 parts (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework10.html).

1. Fitting Two ML Models
- The UCI Breast Cancer Wisconsin Dataset, which includes several features of cell nuclei from breast cancer biopsies, was utilized.
- Involves splitting the data into training and test datasets and fitting a linear classifier (1) and normalizing the data before classification with a linear classifier (2). Both pipelines were saved using the pickle module.

2. Model Deployment
- Uses the pickle module to load the model and take sample data to make predictions utilizing both models created in part 1. 

## Miscellaneous
The following non-exercise files are also in the Git directory
- README.md: This file, which contains an overview of the homework10 directory.
- requirements.txt: includes dependencies for the exercise.

## AI Usage

No AI was used for this assignment.