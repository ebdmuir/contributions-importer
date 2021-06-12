import git 
from git_contributions_importer import *
import json
import os

emails = json.loads(os.environ['EMAILS'])
data = json.loads(os.environ['REPOS'])
repos = []

for item in data:
	print(item)
	git.Repo.clone_from(item['repo'], item['name'])
	repos.append(git.Repo(item['name']))

# Your mock repo
mock_repo = git.Repo("contributions")
importer = Importer(repos, mock_repo) # I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(emails)
importer.import_repository()