import git
import os

print('Hello World')

c = git.cmd.Git(os.getcwd())
c.pull()
