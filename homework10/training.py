from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import pickle

breastcancer_data = load_breast_cancer()

X = breastcancer_data.data
y = breastcancer_data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)


# Pipeline fitting the data to a linear classifier
bc_linear_classifier = SGDClassifier()
bc_linear_classifier.fit(X_train, y_train)
y_pred_linear = bc_linear_classifier.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred_linear)}')

with open('breast_cancer_classifier_pipeline.pkl', 'wb') as f:
    pickle.dump(bc_linear_classifier, f)

# Pipeline normalizing data & then applying a linear classifier
bc_std_linear_classifier = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SGDClassifier())
])

bc_std_linear_classifier.fit(X_train, y_train)
y_pred_std = bc_std_linear_classifier.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred_std)}')

with open('breast_cancer_scaled_classifier_pipeline.pkl', 'wb') as f:
    pickle.dump(bc_std_linear_classifier, f)