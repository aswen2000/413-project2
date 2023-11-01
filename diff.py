import subprocess

def get_num_chunks():
    chunk_counter = 0
    lines = []

    with open('diff_output.patch', 'r') as file:
        lines = file.readlines()

        for line in lines:

            if line.startswith('@@'):
                chunk_counter = chunk_counter + 1
    return chunk_counter

def create_diff():
    bash_script_path = "create_diff.sh"
    try:
        subprocess.run(["bash", bash_script_path], check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.returncode}")
