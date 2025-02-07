import json
import os
import re
import subprocess

# Define directories
root_dir = "/Users/daviddai/Documents/GitHub/research_2024/StudentSimulator/generate/ImageGenerator/imagesByMilestone"
json_path = os.path.join(root_dir, "pyramid_50.json")
java_dir = os.path.join(root_dir, "java_files")
lib_dir = os.path.join(root_dir, "lib")
acm_jar = os.path.join(lib_dir, "acm.jar")
output_dir = os.path.join(root_dir, "generated_images")  # Directory for organized PNGs

# Detect platform-specific classpath separator
classpath_sep = ";" if os.name == "nt" else ":"

# Ensure necessary directories exist
os.makedirs(java_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


def generate_java_files():
    """Loads JSON and creates Java files with unique class names."""
    print("Generating Java files...")

    with open(json_path) as f:
        data = json.load(f)

    for i, entry in enumerate(data):
        script = entry['text']
        label = entry['choices']['strategies']
        label_dir = os.path.join(java_dir, label)
        os.makedirs(label_dir, exist_ok=True)

        # Modify the class name to match the file name
        new_class_name = f"DrawStructure{i}"
        script = re.sub(r'\bDrawStructure\b', new_class_name, script)

        # Write Java file
        file_name = f"{new_class_name}.java"
        file_path = os.path.join(label_dir, file_name)

        with open(file_path, 'w') as java_file:
            java_file.write(script)

    print("Java files created successfully.")


def compile_java_files():
    """Compiles all Java files."""
    print("Compiling Java files...")

    java_files = []
    for root, _, files in os.walk(java_dir):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))

    if not java_files:
        print("No Java files found. Skipping compilation.")
        return False

    sources_file = os.path.join(root_dir, "sources.txt")
    with open(sources_file, "w") as f:
        f.write("\n".join(java_files))

    compile_command = ["javac", "-cp", f".{classpath_sep}{acm_jar}", "@" + sources_file]
    compilation_result = subprocess.run(compile_command, capture_output=True, text=True)

    if compilation_result.returncode == 0:
        print("Java files compiled successfully.")
        return True
    else:
        print("Compilation failed:", compilation_result.stderr)
        return False


def run_java_files():
    """Runs all compiled Java class files."""
    print("Running Java files...")

    for root, _, files in os.walk(java_dir):
        for file in files:
            if file.endswith(".class"):
                class_name = os.path.splitext(file)[0]
                run_command = ["java", "-cp", f".{classpath_sep}{acm_jar}{classpath_sep}{root}", class_name]
                run_result = subprocess.run(run_command, capture_output=True, text=True)

                if run_result.returncode == 0:
                    print(f"Ran {class_name} successfully.")
                else:
                    print(f"Error running {class_name}:", run_result.stderr)

    print("All Java files executed successfully.")


def move_generated_images():
    """Moves generated PNG images from the root directory to their corresponding categories."""
    print("Moving generated images to output directory...")

    # Get all PNG files from the root directory
    for file in os.listdir(root_dir):
        if file.endswith(".png"):
            src_path = os.path.join(root_dir, file)

            # Extract the category label from the filename if available
            label = file.split("_")[0]  # Assumes naming format like "strategy1_image.png"
            label_output_dir = os.path.join(output_dir, label)

            os.makedirs(label_output_dir, exist_ok=True)  # Ensure category folder exists

            # Move PNG file to corresponding label folder
            dest_path = os.path.join(label_output_dir, file)
            os.rename(src_path, dest_path)
            print(f"Moved {file} -> {label_output_dir}")

    print("All images moved successfully.")


def cleanup_files():
    """Deletes all generated Java source and compiled files."""
    print("Cleaning up Java source and compiled files...")

    if os.path.exists(java_dir):
        shutil.rmtree(java_dir)

    sources_file = os.path.join(root_dir, "sources.txt")
    if os.path.exists(sources_file):
        os.remove(sources_file)

    print("Cleanup complete.")


if __name__ == "__main__":
    generate_java_files()
    if compile_java_files():
        run_java_files()
    move_generated_images()  # Move PNGs before deleting Java files
    cleanup_files()