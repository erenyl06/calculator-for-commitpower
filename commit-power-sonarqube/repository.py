# repository.py

import os
import shutil
import subprocess

def clone_and_move_repo(github_url, new_location):
    repo_name = github_url.split('/')[-1].replace('.git', '')
    temp_dir = os.path.join('/tmp', repo_name)
    subprocess.run(['git', 'clone', github_url, temp_dir])
    new_dir = os.path.join(new_location, repo_name)
    shutil.move(temp_dir, new_dir)
    print(f'{repo_name} projesi {new_dir} konumuna taşındı.')
