import json
import os
import re
import subprocess
import shutil
import time

# Define root directories
root_dir = "/Users/daviddai/Documents/GitHub/research_2024/StudentSimulator/generate/ImageGenerator/imagesByKs"
json_path = os.path.join(root_dir, "pyramid_ks_50.json")
java_dir = os.path.join(root_dir, "java_files_ks")
lib_dir = os.path.join(root_dir, "lib")
acm_jar = os.path.join(lib_dir, "acm.jar")
output_dir = os.path.join(root_dir, "generated_images_ks")

# Detect platform-specific classpath separator
classpath_sep = ";" if os.name == "nt" else ":"

# Ensure necessary directories exist
os.makedirs(java_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


def determine_category(choices):
    """Classifies Java files based on choices in JSON."""
    if choices.get("HLoopExistence") == "HelloWorld":
        return "Hello World"
    elif choices.get("VLoopExistence") == "SingleRow":
        return "Single Row"
    elif choices.get("NumRows") == "TwoRows":
        return "Double Rows"
    elif (
        choices.get("NumBrickPerRow") == "ConstantNumBricksPerRow"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("FalseOffsetTypes") == "NoOffset"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
    ):
        return "Rectangle"
    elif (
        choices.get("NumBrickPerRow") == "ConstantNumBricksPerRow"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("FalseOffsetTypes") == "HalfOffsetRightDir"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
    ):
        return "Parallelogram"
    elif (
        choices.get("NumBaseBricks") == "RightNumBaseBricks"
        and choices.get("StartingPoint") == "RightStartPoint"
        and choices.get("NumRows") == "RightNumRows"
        and choices.get("VLoopExistence") == "MultipleRows"
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("offsetCorrectness") == "RightOffset"
        and choices.get("BrickStyle") == "NoColorNotFilled"
    ):
        return "Perfect"
    elif (
        choices.get("NumBaseBricks") == "RightNumBaseBricks"
        and choices.get("StartingPoint") == "RightStartPoint"
        and choices.get("NumRows") == "RightNumRows"
        and choices.get("VLoopExistence") == "MultipleRows"
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("offsetCorrectness") == "RightOffset"
        and choices.get("BrickStyle") in ["ColorNotFilled", "NoColorFilled", "ColorFilled"]
    ):
        return "Perfect Extra"
    elif (
        choices.get("NumBaseBricks") == "RightNumBaseBricks"
        and choices.get("StartingPoint") == "FalseStartPoint"
        and choices.get("NumRows") == "RightNumRows"
        and choices.get("VLoopExistence") == "MultipleRows"
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("offsetCorrectness") == "RightOffset"
        and choices.get("BrickStyle") == "NoColorNotFilled"
    ):
        return "Offset"
    elif (
        choices.get("NumBaseBricks") == "RightNumBaseBricks"
        and choices.get("StartingPoint") == "FalseStartPoint"
        and choices.get("NumRows") == "RightNumRows"
        and choices.get("VLoopExistence") == "MultipleRows"
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("multiRowXSpace") == "RightBrickSpace"
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("offsetCorrectness") == "RightOffset"
        and choices.get("BrickStyle") in ["ColorNotFilled", "NoColorFilled", "ColorFilled"]
    ):
        return "Offset Extra"
    elif (
        choices.get("NumRows") in ["RightNumRows", "OtherLessRows"]
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("FalseOffsetTypes") == "NoOffset"
    ):
        return "Right Triangle"
    elif (
        choices.get("NumRows") in ["RightNumRows", "OtherLessRows"]
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("FalseOffsetTypes") in ["RamOffsetFalseDir", "RamOffsetRightDir", "FullOffsetRightDir"]
    ):
        return "Scalene Triangle"
    elif choices.get("HLoopExistence") == "Diagonal":
        return "Diagonal"
    elif (
        choices.get("NumBaseBricks") == "RightNumBaseBricks"
        and choices.get("NumRows") == "OtherLessRows"
        and choices.get("VLoopExistence") == "MultipleRows"
        and choices.get("NumBrickPerRow") == "RightNumBricksPerRow"
        and choices.get("multiRowXSpace") in ["RightBrickSpace", "OverlapBrickSpace"]
        and choices.get("YSpace") == "RightYSpace"
        and choices.get("offsetCorrectness") == "RightOffset"
        and choices.get("BrickStyle") == "NoColorNotFilled"
    ):
        return "Pyramid Like"
    else:
        return "Off Track"


def determine_ks_group(category):
    """Determines KS group based on category."""
    if category in ["Single Row", "Double Rows", "Diagonal"]:
        return "KS_1"
    elif category in ["Rectangle", "Right Triangle"]:
        return "KS_2"
    elif category in ["Parallelogram", "Scalene Triangle", "Pyramid Like", "Offset"]:
        return "KS_3"
    elif category in ["Offset Extra", "Perfect", "Perfect Extra"]:
        return "KS_4"
    else:
        return "KS_5"


def generate_java_files():
    """Generates Java files from JSON and categorizes them into KS groups."""
    print("Generating and categorizing Java files...")

    with open(json_path) as f:
        data = json.load(f)

    for i, entry in enumerate(data):
        script = entry.get("text", "")

        new_class_name = f"DrawStructure{i}"
        script = re.sub(r"\bDrawStructure\b", new_class_name, script)

        category = determine_category(entry.get("choices", {}))
        ks_group = determine_ks_group(category)

        ks_folder = os.path.join(java_dir, ks_group)
        os.makedirs(ks_folder, exist_ok=True)

        file_name = f"{new_class_name}.java"
        file_path = os.path.join(ks_folder, file_name)

        with open(file_path, "w") as java_file:
            java_file.write(script)

    print("Java files created and categorized successfully.")


def compile_and_run_java():
    """Compiles and runs Java files in each KS group, then moves images to the correct KS group directory."""
    print("Compiling and running Java files...")

    for ks_group in os.listdir(java_dir):
        ks_folder = os.path.join(java_dir, ks_group)
        if not os.path.isdir(ks_folder):
            continue  # Skip non-directory files

        # Ensure output directory for this KS group exists
        ks_output_dir = os.path.join(output_dir, ks_group)
        os.makedirs(ks_output_dir, exist_ok=True)

        java_files = [os.path.join(ks_folder, f) for f in os.listdir(ks_folder) if f.endswith(".java")]

        if not java_files:
            continue

        # Compile Java files
        compile_command = ["javac", "-cp", f".{classpath_sep}{acm_jar}"] + java_files
        compilation_result = subprocess.run(compile_command, capture_output=True, text=True)

        if compilation_result.returncode == 0:
            print(f"Compiled Java files in {ks_group} successfully.")
        else:
            print(f"Compilation failed in {ks_group}:", compilation_result.stderr)
            continue

        # Run Java files, passing the root directory as an argument
        for java_file in java_files:
            class_name = os.path.splitext(os.path.basename(java_file))[0]
            run_command = ["java", "-cp", f".{classpath_sep}{acm_jar}{classpath_sep}{ks_folder}", class_name, root_dir]
            run_result = subprocess.run(run_command, capture_output=True, text=True)

            if run_result.returncode == 0:
                print(f"Ran {class_name} successfully.")
            else:
                print(f"Error running {class_name}:", run_result.stderr)

        # Wait a moment to ensure images are fully generated before moving
        time.sleep(2)

        # Move images to the correct KS group directory
        for file in os.listdir(root_dir):
            if file.endswith(".png"):  # Detect PNG files
                src_path = os.path.join(root_dir, file)
                dest_path = os.path.join(ks_output_dir, file)
                os.rename(src_path, dest_path)
                print(f"Moved {file} -> {ks_output_dir}")

    print("Finished running Java files and moving images.")

def cleanup_java_files():
    """Deletes the entire Java folder tree after execution."""
    print("Cleaning up Java files...")
    if os.path.exists(java_dir):
        shutil.rmtree(java_dir)


if __name__ == "__main__":
    generate_java_files()
    compile_and_run_java()
    cleanup_java_files()