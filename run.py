import git 
from git_contributions_importer import *
import json

data = json.load(open('data.json', 'r'))
repos = []

for item in data:
	git.Repo.clone_from(item.repo, item.name)
	repos.append(git.Repo(item.name))

# Your mock repo
mock_repo = git.Repo("contributions")
importer = Importer(repos, mock_repo) # I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['eric@ebdm.dev', 'eric.muir@swimtime.org', 'www-data@ip-172-0-253-183.eu-west-2.compute.internal', 'www-data@ip-172-0-46-95.eu-west-2.compute.internal', 'ericmuir@protonmail.com', 'ericmuir@Erics-iMac.local', 'ebdmuir@gmail.com'])
importer.import_repository()