import json
import os

# Load the JSON file
with open('pyramid_500.json') as f:
    data = json.load(f)

# Directory to save Java files
java_dir = 'java_files'
os.makedirs(java_dir, exist_ok=True)

# Create Java files
for i, entry in enumerate(data):
    script = entry['text']
    label = entry['choices']['strategies']
    label_dir = os.path.join(java_dir, label)
    os.makedirs(label_dir, exist_ok=True)
    file_name = f"Script{i}.java"
    file_path = os.path.join(label_dir, file_name)

    with open(file_path, 'w') as java_file:
        java_file.write(script)

print("Java files created successfully.")