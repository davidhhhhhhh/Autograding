import json
import os
import re
import csv

# Load the JSON file
with open('pyramid_ks_1000.json') as f:
    data = json.load(f)

# Directory to save Java files
java_dir = 'java_files_ks'
os.makedirs(java_dir, exist_ok=True)

# Initialize the list to store rows for the CSV
csv_data = []

# Function to determine the category based on the choices
def determine_category(choices):
    if choices.get('HLoopExistence') == 'HelloWorld':
        return 'Hello World'
    elif choices.get('VLoopExistence') == 'SingleRow':
        return 'Single Row'
    elif choices.get('NumRows') == 'TwoRows':
        return 'Double Rows'
    elif (choices.get('NumBrickPerRow') == 'ConstantNumBricksPerRow' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('FalseOffsetTypes') == 'NoOffset' and
          choices.get('multiRowXSpace') == 'RightBrickSpace'):
        return 'Rectangle'
    elif (choices.get('NumBrickPerRow') == 'ConstantNumBricksPerRow' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('FalseOffsetTypes') == 'HalfOffsetRightDir' and
          choices.get('multiRowXSpace') == 'RightBrickSpace'):
        return 'Parallelogram'
    elif (choices.get('NumBaseBricks') == 'RightNumBaseBricks' and
          choices.get('StartingPoint') == 'RightStartPoint' and
          choices.get('NumRows') == 'RightNumRows' and
          choices.get('VLoopExistence') == 'MultipleRows' and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('multiRowXSpace') == 'RightBrickSpace' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('offsetCorrectness') == 'RightOffset' and
          choices.get('BrickStyle') == 'NoColorNotFilled'):
        return 'Perfect'
    elif (choices.get('NumBaseBricks') == 'RightNumBaseBricks' and
          choices.get('StartingPoint') == 'RightStartPoint' and
          choices.get('NumRows') == 'RightNumRows' and
          choices.get('VLoopExistence') == 'MultipleRows' and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('multiRowXSpace') == 'RightBrickSpace' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('offsetCorrectness') == 'RightOffset' and
          choices.get('BrickStyle') in ['ColorNotFilled', 'NoColorFilled', 'ColorFilled']):
        return 'Perfect Extra'
    elif (choices.get('NumBaseBricks') == 'RightNumBaseBricks' and
          choices.get('StartingPoint') == 'FalseStartPoint' and
          choices.get('NumRows') == 'RightNumRows' and
          choices.get('VLoopExistence') == 'MultipleRows' and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('multiRowXSpace') == 'RightBrickSpace' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('offsetCorrectness') == 'RightOffset' and
          choices.get('BrickStyle') == 'NoColorNotFilled'):
        return 'Offset'
    elif (choices.get('NumBaseBricks') == 'RightNumBaseBricks' and
          choices.get('StartingPoint') == 'FalseStartPoint' and
          choices.get('NumRows') == 'RightNumRows' and
          choices.get('VLoopExistence') == 'MultipleRows' and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('multiRowXSpace') == 'RightBrickSpace' and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('offsetCorrectness') == 'RightOffset' and
          choices.get('BrickStyle') in ['ColorNotFilled', 'NoColorFilled', 'ColorFilled']):
        return 'Offset Extra'
    elif (choices.get('NumRows') in ['RightNumRows', 'OtherLessRows'] and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('FalseOffsetTypes') == 'NoOffset'):
        return 'Right Triangle'
    elif (choices.get('NumRows') in ['RightNumRows', 'OtherLessRows'] and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('FalseOffsetTypes') in ['RamOffsetFalseDir', 'RamOffsetRightDir', 'FullOffsetRightDir']):
        return 'Scalene Triangle'
    elif choices.get('HLoopExistence') == 'Diagonal':
        return 'Diagonal'
    elif (choices.get('NumBaseBricks') == 'RightNumBaseBricks' and
          choices.get('NumRows') == 'OtherLessRows' and
          choices.get('VLoopExistence') == 'MultipleRows' and
          choices.get('NumBrickPerRow') == 'RightNumBricksPerRow' and
          choices.get('multiRowXSpace') in ['RightBrickSpace', 'OverlapBrickSpace'] and
          choices.get('YSpace') == 'RightYSpace' and
          choices.get('offsetCorrectness') == 'RightOffset' and
          choices.get('BrickStyle') == 'NoColorNotFilled'):
        return 'Pyramid Like'
    else:
        return 'Off Track'


# Function to determine KS group
def determine_ks_group(category):
    if category in ['Single Row', 'Double Rows', 'Diagonal']:
        return 'KS_1'
    elif category in ['Rectangle', 'Right Triangle']:
        return 'KS_2'
    elif category in ['Parallelogram', 'Scalene Triangle', 'Pyramid Like', 'Offset']:
        return 'KS_3'
    elif category in ['Offset Extra', 'Perfect', 'Perfect Extra']:
        return 'KS_4'
    else:
        return 'KS_5'


# Create Java files and collect CSV data
for i, entry in enumerate(data):
    script = entry.get('text', '')

    # Modify the class name to match the file name
    new_class_name = f"DrawStructure{i}"
    script = re.sub(r'\bDrawStructure\b', new_class_name, script)

    file_name = f"{new_class_name}.java"
    file_path = os.path.join(java_dir, file_name)

    with open(file_path, 'w') as java_file:
        java_file.write(script)

    # Determine the category and KS group
    category = determine_category(entry.get('choices', {}))
    ks_group = determine_ks_group(category)

    # Add row to csv_data
    csv_data.append([file_name, category, ks_group])

# Save CSV file in the working directory
csv_file_path = 'java_file_labels_ks.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Java File', 'Label', 'KS Group'])
    writer.writerows(csv_data)

print(f"Java files created successfully with matching class names. CSV file saved at {csv_file_path}.")