import subprocess

def run_java(file_path, num1, num2, method):
    # Specify the path to the Java executable (java command)
    java_executable = 'java'

    # Specify the path to the Java file you want to run
    java_file = file_path

    # Specify any command-line arguments your Java program needs
    #java_arguments = [num1, num2, 'division']
    java_arguments = [num1, num2, method]

    # Construct the command to run the Java program
    command = [java_executable, java_file] + java_arguments

    print('=========')
    print(command)
    print('=========')

    # Run the Java program
    try:
        subprocess.run(command, check=True, text=True, shell=True)
        return 0
    except subprocess.CalledProcessError as e:
        #print(f"Error: {e.returncode}")
        return 1


#usage
# run_java("temp_copy.java", '5', '0', 'division')