Sublime Text 3 Settings
=======================

These are the settings I use in Sublime Text 3.

## Presentation Slides

Slides with basic instructions are available here: [Sublime Text 3 Presentation Slides](https://www.dropbox.com/s/8tn6p01wncvf6rh/sublime%20text%20editor%20presentation%20Airbnb.key?dl=0)

## Install

###Installing necessary packages
See the instructions here: [Package Control Installation](http://wbond.net/sublime_packages/package_control/installation#ST3)

#### Installing the settings
Go to your Packages directory:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
```

Clone as your `User` packages:

```
git clone https://github.com/cschubiner/sublime-text-3-settings.git User
```

#### Installing SublimePaneNavigation
Most packages should install automatically, but you will need to manually install SublimePaneNavigation.

You can install SublimePaneNavigation by doing the following:
```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/borist/SublimePaneNavigation.git
```

#### Installing the autoformatter for Rails html.erb files
```
gem install htmlbeautifier
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
