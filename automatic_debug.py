import subprocess

#Specify the path to the Bash script
bash_script_path = "script.sh"
try:
    subprocess.run(["bash", bash_script_path], check=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.returncode}")

# Read the diff output from a text file
file_path = "diff_output.txt"  # Update this to the path of your text file
with open(file_path, "r") as input_file:
    lines = input_file.readlines()[2:]

# Write the modified content (without the first two lines) to the output file
with open(file_path, "w") as output_file:
    output_file.writelines(lines)