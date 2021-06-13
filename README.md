# Ulauncher Thingiverse 
Ulauncher extension to quickly manage variety.

## Overview

Once you install this extension, just start Ulauncher and type: `v`. That will start the extension.

from here, you can execute a number of actions for controlling your wallpaper manager:

![List of actions](screenshots/img.png)


## Installation

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/subutux/ulauncher-variety
```

## Development

```
git clone git@github.com:subutux/ulauncher-variety.git
cd ulauncher-variety
make attach
```

The `make attach` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.
If the extensions folder does not exist, create it and run the command again.

Make sure Ulauncher is not running and from command line run:

```sh
ulauncher --no-extensions --dev -v |& grep "variety"
```

This will start ulauncher with all the extensions disabled which will make it easier to look for logs.

You then have to start the Laravel extension manually. In the output of the previous command you should find something
similar to this:

```sh
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-variety PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/mabasic/.cache/ulauncher_cache/extensions/ulauncher-variety/main.py
```

Copy and run that command in another terminal window.

Your extension should now be running. To see your changes, just Ctrl+C and re-run the last command.

## License

Ulauncher variety Extension is open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).