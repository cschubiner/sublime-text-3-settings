Sublime Text 3 Settings
=======================

These are the settings I use in Sublime Text 3.

## Presentation Slides

Slides with basic instructions are available here: [Sublime Text 3 Presentation Slides](https://www.dropbox.com/sh/qyxc9uv558e3uur/AABWVnwcQkB57GMWDbR371LDa?dl=0)

## Install

###Installing necessary packages

#### Installing the package manager
See the instructions here: [Package Control Installation](http://wbond.net/sublime_packages/package_control/installation#ST3)

#### Installing packages
Using the package manager, open Sublime Text 3 and install the following packages:
- BracketHighlighter
- Clay Schubiner Color Schemes
- SideBarEnhancements
- SublimeAStyleFormatter

Also install SublimePaneNavigation, which is currently not available in package control:
```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/borist/SublimePaneNavigation.git
```

#####Optional packages
- Display Functions (Java)
- EasyMotion
- Emmet
- jQuery
- MagentoIntel
- Pretty JSON
- SCSS
- JavascriptBeautify
- SublimeLinter (See http://sublimelinter.readthedocs.org/en/latest/installation.html)


### Installing the settings
Go to your Packages directory:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
```

Clone as your `User` packages:

```
git clone https://github.com/cschubiner/sublime-text-3-settings.git User
```

You're done!

## Updating

Go to your User Packages directory:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User
```

Pull on the repo:

```
git pull
```
