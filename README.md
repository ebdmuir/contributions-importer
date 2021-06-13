# Automated Contributions Importer for GitHub

This is an automated tool for importing third party repositories into your contributions graph on your profile

- First make a new SSH key and add it to your git providers

- Second create a contributions repository

- Finally add the secrets to your forked version of this repository and next run it'll sort your contributions out

Needed secrets:

- ``EXPORT_REPO``
- ``KNOWN_HOSTS``
- ``SSH_KEY``
- ``REPOS``
- ``EMAILS``

``EXPORT_REPO`` is a path to your contribtuions repository. Mine is ``ebdmuir/contributions``

``EMAILS`` and ``REPOS`` need to be JSON arrays, ``EMAILS`` is just an array of email strings but ``REPOS`` is an array of objects like follows

~~~ json
{
    "name":"repo-name",
    "repo":"ssh-connection-string"
}
~~~