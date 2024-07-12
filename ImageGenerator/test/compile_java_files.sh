#!/bin/bash

# Directory containing Java files
JAVA_DIR="java_files"
LIB_DIR="lib"
ACM_JAR="$LIB_DIR/acm.jar"

# Compile all Java files
find $JAVA_DIR -name "*.java" > sources.txt
javac -cp ".;$ACM_JAR" @sources.txt

echo "Java files compiled successfully."

