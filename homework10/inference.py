import argparse
import pandas as pd
import pickle

# Loading the pipelines from training script
with open("breast_cancer_classifier_pipeline.pkl", "rb") as f:
    linear_classifier = pickle.load(f)

with open("breast_cancer_scaled_classifier_pipeline.pkl", "rb") as f:
    std_linear_classifier = pickle.load(f)

def inference(dataset: object) -> tuple:
    linear_pred = linear_classifier.predict(dataset)
    std_linear_pred = std_linear_classifier.predict(dataset)
    return (linear_pred, std_linear_pred)

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("--dataset", required = True, help = "Path to the dataset for inference")
      args = parser.parse_args()
   
      dataset = pd.read_csv(args.dataset)
   
      linear_pred, std_linear_pred = inference(dataset)
   
      print("Predictions from linear classifier:", linear_pred)
      print("Predictions from scaled linear classifier:", std_linear_pred)
   
if __name__ == "__main__":
      main()