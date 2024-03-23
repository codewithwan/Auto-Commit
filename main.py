import os
import random
import string
import time
from github import Github

def generate_random_content():
    content = ''.join(random.choices(string.ascii_lowercase + string.digits, k=1000))
    return content

def commit_to_repo(repo):
    file_name = f"random_file_{int(time.time())}.txt" 
    content = generate_random_content()
    repo.create_file(file_name, "Random commit", content)

def read_access_token(file_path):
    with open(file_path, 'r') as file:
        access_token = file.read().strip()
    return access_token

def countdown(seconds):
    for second in range(seconds, 0, -1):
        print(f"Waiting... {second} seconds remaining.", end="\r")
        time.sleep(1)

access_token_file = './access_token.txt'

if os.path.exists(access_token_file):
    print("Access token valid.")
else:
    print("Access token not valid.")

repo_name = "your_repo_name"

github_access_token = read_access_token(access_token_file)
g = Github(github_access_token)

user = g.get_user()
repo = user.get_repo(repo_name)

for _ in range(4):
    commit_to_repo(repo)
    print("The commit was successfully made in the repository : ", repo.full_name)
    countdown(10)

print("All commits were successfully made 4 times in the repository : ", repo.full_name)
