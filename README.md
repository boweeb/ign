# ign #

> **Forked from: [gh://Antrikshy/ignr](https://github.com/Antrikshy/ignr)**


`ign` is a Python-based command line utility to fetch `.gitignore` templates from [gitignore.io](https://gitignore.io). gitignore.io has official [command line tools](https://github.com/joeblau/gitignore.io#install-command-line), but they rely on bash or zsh, and *may* not be compatible with all systems out there.

The `.gitignore` file in this repository was generated using `ign`, if you want to look at a sample!

There's also a Go-based alternative, [gogi](https://github.com/Gnouc/gogi), but not everyone uses Go.

`ign` was created for Python users who prefer to install via [PyPI](https://pypi.python.org/pypi) and/or [pip](https://pip.pypa.io).


## Usage ##

Install using

    pip install ign


### List ###

    ign -l

Lists all available `.gitignore` templates on gitignore.io.


### Search ###

    ign -s mac

Searches for supplied query in list of available templates from gitignore.io, similar to using `grep`.


### Preview ###

    ign -p scala macOS

Prints a preview of the template without generating a `.gitignore` file. List multiple space-separated languages, frameworks, operating systems to get combined output.


### Create ###

    ign -n node sass windows

Generates a new `.gitignore` file in the current directory. List multiple space-separated languages, frameworks, operating systems to get combined output.

If a `.gitignore` already exists in the directory, `ign` will give you an option to back it up.


## Troubleshooting ##

Since `gitignore.io` uses HTTPS, running this utility in certain macOS environments may result in an SSL "handshake failure" error, which is discussed in detail in this [requests issue](https://github.com/kennethreitz/requests/issues/2022).

Unfortunately, there is no trivial fix.

In my experience, switching from the included Python in El Capitan to a standalone Python installed via brew solved the issue. All my existing packages seemed to remain intact.


## Contribute ##

Feel free to make improvements. PR's are greatly appreciated.

I can be reached [@jbutch](https://twitter.com/jbutch) or [via reddit](https://www.reddit.com/u/boweeb1011).
