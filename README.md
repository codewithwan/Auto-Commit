# Random Content Committer

## Description
This Python script automates commits to a GitHub repository with random content. It generates random files with random content and commits them to the specified repository at regular intervals.

## Getting Started
### Prerequisites
- Python 3.x installed on your system
- GitHub account
- Personal access token generated on GitHub with repo scope

### Installation
1. Clone this repository to your local machine.
2. Create a virtual environment (optional but recommended).
3. Install the required dependencies:
## Installastion

```
pip install PyGithub
```
### Usage
1. Obtain a personal access token from GitHub with the `repo` scope.
2. Create a file named `access_token.txt` in the same directory as the script and paste your access token there.
3. Replace `"your_repo_name"` in the script with the name of your target GitHub repository.
4. Run the script:

5. The script will start committing random content to your repository at regular intervals.

## Acknowledgments
- [PyGithub](https://github.com/PyGithub/PyGithub) - Python library to interact with the GitHub API.
