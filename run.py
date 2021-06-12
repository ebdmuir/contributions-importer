import git 
from git_contributions_importer import *
# Your private repo or Bitbucket repo
tfbaseinstance = git.Repo("terraform-aws-base-instance")
swimcloudbackend = git.Repo("backend-api")
swimcloudwebapps = git.Repo("web-applications")
swimcloudfinder = git.Repo("lesson-finder")
swimcloudportal = git.Repo("customer-portal")
# Your mock repo
mock_repo = git.Repo("contributions")
importer = Importer([tfbaseinstance, swimcloudbackend, swimcloudwebapps, swimcloudfinder, swimcloudportal], mock_repo) # I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['eric@ebdm.dev', 'eric.muir@swimtime.org', 'www-data@ip-172-0-253-183.eu-west-2.compute.internal', 'www-data@ip-172-0-46-95.eu-west-2.compute.internal', 'ericmuir@protonmail.com', 'ericmuir@Erics-iMac.local', 'ebdmuir@gmail.com'])
importer.import_repository()