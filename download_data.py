import kagglehub
import os
import shutil

# Download dataset
path = kagglehub.dataset_download("blastchar/telco-customer-churn")
print("Downloaded at:", path)

# Search and copy CSV into data folder
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            source = os.path.join(root, file)
            destination = "data/telco_churn.csv"
            shutil.copy(source, destination)
            print("CSV copied to:", destination)
