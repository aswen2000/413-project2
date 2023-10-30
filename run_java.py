#import automatic_debug
#import output_parser
import subprocess

import subprocess
def run_java():
    # Specify the path to the Java executable (java command)
    java_executable = 'java'

    # Specify the path to the Java file you want to run
    java_file = 'file1v2.java'

    # Specify any command-line arguments your Java program needs
    java_arguments = ['5', '5', 'division']

    # Construct the command to run the Java program
    command = [java_executable, java_file] + java_arguments

    # Run the Java program
    try:
        subprocess.run(command, check=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}")
        return 1
