<h1 align="center">Git and GitHub</h1>

<p align="center">
  <img src="Images/Git + GitHub.png" alt="drawing" width="100%"/>
</p>

## Table of Contents
- [Git](#git)
  - [Definition](#definition)
  - [Installation](#installation)
    - [macOS](#macos)
    - [Linux](#linux)
    - [Windows](#windows)
    - [Additional Configurations](#additional-configurations)
    - [Useful Configurations](#useful-configurations)
  - [Terminal commands](#terminal-commands)
  - [Git Stages](#git-stages)
  - [Git Commands](#git-commands)
    - [Create a Git repository](#create-a-git-repository)
    - [Check Status](#check-status)
    - [Add, Restore and Commit](#add-restore-and-commit)
    - [Git Log](#git-log)
    - [Git Tags](#git-tags)
    - [Git Diff](#git-diff)
    - [Git Reset](#git-reset)
    - [Git Checkout](#git-checkout)
  - [Branching](#branching)
    - [Git Merge](#git-merge)
  - [Advanced Git Commands](#advanced-git-commands)
    - [Stash](#stash)
    - [Rebase](#rebase)
    - [Cherry Pick](#cherry-pick)
  - [Git-Ignore](#git-ignore)
  - [What is a VCS?](#what-is-a-vcs)
    - [Local](#local)
    - [Centralized](#centralized)
    - [Distributed](#distributed)
- [GitHub](#github)
  - [Remote Repositories](#remote-repositories)
  - [Generating a key](#generating-a-key)
  - [Push](#push)
    - [Force push](#force-push)
  - [Fetch and Pull](#fetch-and-pull)
  - [Issues and Pull-Request](#issues-and-pull-request)
  - [Other commands](#other-commands)
    - [Deleting a tag on remote repo](#deleting-a-tag-on-remote-repo)

# Git

## Definition
Git is a [VCS](#vcs), usually used for coordinating work among programmers. Can be used with plain text, as well as binary files, but binary files may not be fully supported.

## Installation
You can check for the Git installation in terminal (or Git Bash in windows) typing:

```bash
git --version
```

### macOS
There are multiple options to install Git on a mac:
1. Download Git from [Official Git website](https://git-scm.com) and execute the installer.
2. **Using [homebrew](https://www.youtube.com/watch?v=1uvr9-zUB3w):** Type  `brew install git` in terminal.
3. **Using Xcode package:** When executing git from the terminal for the first time, it will ask you if you want to install it.

### Linux
Type in terminal `sudo apt-get install git`

It is recommended to update "apt-get" before any installation.

### Windows
Windows does not have a proper programming environment, so it needs to configure a lot or additional things such as a Bash terminal and security protocols.

1. Download Git from [Official Git website](https://git-scm.com)
2. Execute installer
3. **Components:**
   - Git Bash
   - TrueType (Beautiful text)
   - Check daily for Git updates
4. **Default branch name:** "master" (It's usually the default value)
5. **Default editor:** Vim is defualt, but VSCode is recommended
6. **PATH environment:** Git from command line and also from 3rd-party-software (more compatibility)
7. **HTTPS transport:** OpenSSL (Easy option)
8. **Line ending:** Checkout Windows and Commit Unix (more compatibility)
9. **Terminal emulator:** MinTTY (Useful to get used to linux commands)
10. **Behaviour of `git pull`:** Default (Ease of use)
11. **Credential helper:** Git Credential Manager
12. **Symbolic links:** Enable (Shortcuts but on Linux and macOS)
13. **System caching:** Enable (for Git to run faster)
14. **Experimental support:** No if not sure about it

### Additional Configurations
1. **Setup username:**
```bash
git config --global user.name "USERNAME"
```
2. **Setup email:**
```bash
git config --global user.email "EMAIL@DOMAIN.COM"
```

### Useful Configurations
- Set colorUI as true for colored visualization.
```bash
git config --global color.ui true
```
- Setup an [alias](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) (**superlog**) for an easier and shorter log read.
```bash
git config --global alias.superlog "log --graph --abbrev-commit --date=relative --all --format=format:'%C(bold blue)%h%C(reset) %C(auto,magenta)%G? %C(bold green)(%>(18,trunc)%aD)%C(reset) %C(bold blue)[%<(10,trunc)%aN]%Creset - %s%C(reset) %C(bold yellow)%d%C(reset)'"
```
- Set the default text editor for global or local (replacing `global` with `local`) use. Replace `code` with `atom` to use Atom, `subl` to use Sublime Text, etc.
```bash
git config --global core.editor “code —wait”
```
## Terminal commands
- Print working directory: It is used to find out where we currently are
```bash
pwd
```
- Change directory: It is used to change the current working directory (`~` stands for the user account's home folder)
- To exit a directory, use dots after `cd`
```bash
cd ~/documents/git/proyectX/
cd ..
```
- In macOS you can crag and drop a folder to the terminal to copy it's path

- List of items in directory (`-a` to see even hidden files, `-l` to see as a list)
```bash
ls -a
ls -l
```
- Make directory: Creates a folder un the current working directory
```bash
mkdir NEW_DIRECTORY_NAME
```
- Clear: Cleans the terminal but doesn't delete any commands given
```bash
clear
```
- Create files
```bash
touch FILE_NAME.EXTENSION
```
- Remove: It deletes a file or a folder
```bash
rm FILE_NAME.EXTENSION
rm -rf FOLDER_NAME
```
- View file content
```bash
cat FILE_NAME.EXTENSION
```

## Git Stages
<p align="center">
  <img src="Images/GIT_stages.png" alt="drawing" width="300"/>
</p>

## Git Commands

### Create a Git repository
To create a git repository, while located in the proyect folder, type
```bash
git init
```
It creates a hidden folder called `.git`, you can check that with the comand `ls -al`

### Check Status
```bash
git status
```
It shows if there are files staged or in the working directory. With this command, changes yet commited are listed.

- No changes (or all changes commited)
<p align="center">
  <img src="Images/status_commited.png" alt="drawing" width="450"/>
</p>

- Changes in working directory
<p align="center">
  <img src="Images/status_wd.png" alt="drawing" width="450"/>
</p>

- Changes staged
<p align="center">
  <img src="Images/status_staged.png" alt="drawing" width="450"/>
</p>

### Add, Restore and Commit
The `add` command is used to stage changes made in working directory
```bash
git add FILE_NAME       # Sends a specific change to the staging area
git add -all            # Stages all changes in a folder
```

The `restore` command removes changes from the staging area or working directory
```bash
git restore --staged FILENAME.py  # Removes FILENAME.py changes from the staging area
git restore FILENAME.py           # Removes FILENAME.py chenges from working directory
```

The `commit` command, is used to 'confirm' all changes already staged. It is a good practice to include a message with every commit, explaining the changes made.
```bash
git commit -m "MESSAGE" # Commits every staged change with a message
git commit --amend      # Changes current commit message
```

### Git Log
The `log` command, shows the commits made with some useful information such as:
1. [SHA](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection): Unique identifier, sequence or numbers and letters
2. Author of the commit
3. Date (including time)
4. Commit description message

<p align="center">
  <img src="Images/git log.png" alt="drawing" width="400"/>
</p>

To use it, there are multiple posible parameters as shown below:
```bash
git log
git log --oneline       # Summary the whole commit in one line each
git log -5              # Limit the number of commits you want to see
git log -5 --graph      # Parameters can be nested

git superlog            # An alias we previously created in "Useful Configurations" section
```

### Git Tags

### Git Diff

### Git Reset

### Git Checkout

## Branching

### Git Merge

## Advanced Git Commands

### Stash

### Rebase

### Cherry Pick

## Git-Ignore

## What is a VCS?

### Local

<p align="center">
  <img src="Images/VCS_local.png" alt="drawing" width="160"/>
</p>

### Centralized

<p align="center">
  <img src="Images/VCS_centralized.png" alt="drawing" width="200"/>
</p>

### Distributed

<p align="center">
  <img src="Images/VCS_distributed.png" alt="drawing" width="300"/>
</p>

# GitHub

## Remote Repositories

## Generating a key

## Push

### Force push

## Fetch and Pull

## Issues and Pull-Request

## Other commands

### Deleting a tag on remote repo
```bash
git push -delete origin TAG_NAME
```