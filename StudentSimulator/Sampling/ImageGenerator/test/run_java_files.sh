#!/bin/bash

# Directory containing Java files
JAVA_DIR="java_files"
LIB_DIR="lib"
ACM_JAR="$LIB_DIR/acm.jar"

# Run each compiled Java file
for label_dir in $JAVA_DIR/*; do
  if [ -d "$label_dir" ]; then
    for java_file in $label_dir/*.class; do
      # Extract the base name of the Java class
      class_name=$(basename "$java_file" .class)
      
      # Run the Java class
      java -cp ".;$ACM_JAR:$label_dir" "$class_name"
      
      echo "Ran $class_name successfully."
    done
  fi
done

echo "All Java files executed successfully."
