import git
import os

c = git.cmd.Git(os.getcwd())
c.pull()