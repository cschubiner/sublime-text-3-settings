Sublime Text 3 Settings
=======================

These are the settings I use in Sublime Text 3. There are no dependencies right now.

## Install

###Installing necessary packages

#### Installing the package manager
See the instructions here: [Package Control Installation](http://wbond.net/sublime_packages/package_control/installation#ST3)

#### Installing packages
Using the package manager, open Sublime Text 3 and install the following packages:
- BracketHighlighter
- Clay Schubiner Color Schemes
- SublimePaneNavigation
- SideBarEnhancements
- SublimeAStyleFormatter

Also install BlockCursorEverywhere, which is currently not available in package control:
```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/jlangston/BlockCursorEverywhere.git
```

#####Optional packages
- Display Functions (Java)
- EasyMotion
- Emmet
- jQuery
- MagentoIntel
- Pretty JSON
- SCSS
- sublime-jslint


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
