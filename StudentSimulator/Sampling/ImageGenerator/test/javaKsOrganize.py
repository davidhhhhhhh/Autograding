import shutil
import pandas as pd
import os

# Load the CSV file
csv_path = '/Users/daviddai/Documents/GitHub/research_2024/ImageGenerator/test/java_file_labels_ks.csv'
df = pd.read_csv(csv_path)

# Directory containing your Java files
source_directory = '/Users/daviddai/Documents/GitHub/research_2024/ImageGenerator/test/java_files_ks'
destination_directory = '/Users/daviddai/Documents/GitHub/research_2024/ImageGenerator/test/java_files_ks'

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    java_file = row['Java File']
    ks_group = row['KS Group']

    # Create the KS Group subfolder if it doesn't exist
    ks_folder = os.path.join(destination_directory, ks_group)
    os.makedirs(ks_folder, exist_ok=True)

    # Move the Java file to the corresponding KS folder
    source_path = os.path.join(source_directory, java_file)
    destination_path = os.path.join(ks_folder, java_file)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {java_file} to {ks_folder}")
    else:
        print(f"{java_file} not found in {source_directory}")

# Note: Replace '/path/to/your/java_files_ks' and '/path/to/organized_java_files'
# with the actual paths on your system.