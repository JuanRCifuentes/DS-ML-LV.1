<p align="center">
  <img src="Images/Git + GitHub.png" alt="drawing" width="100%"/>
</p>

## Table of Contents
- [Git](#git)
  - [Definition](#definition)
  - [Installation](#installation)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
    - [Additional Configurations](#additional-configurations)
    - [Useful Configurations](#useful-configurations)
  - [VCS](#vcs)
    - [Local](#local)
    - [Centralized](#centralized)
    - [Distributed](#distributed)
- [Github](#github)

# Git

## Definition
Git is a [VCS](#vcs), usually used for coordinating work among programmers.

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
1. Setup username: In terminal type
```bash
git config --global user.name "USERNAME"
```
2. Setup email: In terminal type
```bash
git config --global user.email "EMAIL@DOMAIN.COM"
```

### Useful Configurations
- Set colorUI as true for colored visualization. In terminal type:
```bash
git config --global color.ui true
```
- Setup an [alias](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) (**superlog**) for an easier and shorter log read. In terminal type:
```bash
git config --global alias.superlog "log --graph --abbrev-commit --date=relative --all --format=format:'%C(bold blue)%h%C(reset) %C(auto,magenta)%G? %C(bold green)(%>(18,trunc)%aD)%C(reset) %C(bold blue)[%<(10,trunc)%aN]%Creset - %s%C(reset) %C(bold yellow)%d%C(reset)'"
```
- Set the default text editor for global or local (replacing `global` with `local`) use. Replace `code` with `atom` to use Atom, `subl` to use Sublime Text, etc. Type in terminal:
```bash
git config --global core.editor “code —wait”
```

## VCS

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

# Github