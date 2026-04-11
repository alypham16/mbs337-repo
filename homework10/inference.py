from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import pickle

breastcancer_data = load_breast_cancer()
X = breastcancer_data.data
y = breastcancer_data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)

# Pipeline fitting the data to a linear classifier
with open('breast_cancer_classifier_pipeline.pkl', 'rb') as f:
   linear_classifier = pickle.load(f)


# Pipeline normalizing data & then applying a linear classifier
with open('breast_cancer_normalizer_data_classifier_pipeline.pkl', 'rb') as f:
   std_linear_classifier = pickle.load(f)


def inference(dataset: object) -> tuple:
    linear_pred = linear_classifier.predict(dataset)
    std_linear_pred = std_linear_classifier.predict(dataset)
    return (linear_pred, std_linear_pred)