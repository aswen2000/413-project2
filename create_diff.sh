#!/bin/bash

file1="file1v1.java"
file2="file1v2.java"
output_file="diff_output.patch"  # Name of the output file

# Check if both files exist
if [ -f "$file1" ] && [ -f "$file2" ]; then
    # Compare the two files with a unified context of 0 lines and save the output to a text file
    diff -U0 "$file1" "$file2" > "$output_file"
    echo "Diff output saved to $output_file"
else
    echo "One or both of the files do not exist."
fi