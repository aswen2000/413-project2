import subprocess

def create_diff():
    bash_script_path = "create_diff.sh"
    try:
        subprocess.run(["bash", bash_script_path], check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.returncode}")
