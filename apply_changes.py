import subprocess
import reset_files

reset_diff = reset_files

def cherrypick_diff(chunks):
    reset_diff.reset_diff_output()

    chunk_counter = -1
    lines = []

    with open('diff_output.patch', 'r') as file:
        lines = file.readlines()

    with open('diff_output.patch', 'w') as file:
        for line in lines:

            if line.startswith('@@'):
                chunk_counter = chunk_counter + 1
            if chunk_counter < 0 or chunk_counter in chunks:
                file.write(line)


def apply_changes(chunks):
    cherrypick_diff(chunks)

    print('===')
    print('applying changes: ' + str(chunks))
    #print('===')

    try:
        subprocess.run(["patch", "file1v1.java", "diff_output.patch"], check=True, text=True, shell=True)
    except subprocess.CalledProcessError as e:
        print('in apply changes')
        print(f"An error occurred: {e.returncode}")