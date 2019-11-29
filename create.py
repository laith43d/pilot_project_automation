import sys
import os
from github import Github
from config import PASSWORD
from subprocess import run
username = 'your_github_username'
password = PASSWORD

path = './'

def create():
    folder_name = str(sys.argv[1])
    os.makedirs(path + str(folder_name))
    github_user = Github(username, password).get_user()
    repo = github_user.create_repo(folder_name)
    run(f"""
    cd {folder_name}
    echo "# first init" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/laith43d/{folder_name}.git
    git push -u origin master
    """)
    print(f'Successfully created repository {folder_name}')

if __name__ == "__main__":
    create()
