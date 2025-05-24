import os

repo_url = "https://github.com/Tech-Michael112/Instagram-Hax"
repo_dir = "Instagram-Hax"
file_to_run = "gram1_enc.py"

try:
    if not os.path.exists(repo_dir):
        os.system(f"git clone {repo_url}")
    os.chdir(repo_dir)
    os.system("git pull")
    if os.path.exists(file_to_run):
        print("File can run now")
        os.system(f"python {file_to_run}")
    else:
        print(f"{file_to_run} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
