pypboy
======

Notes from ZapWizard:
This is a work in progress of the code for my Functional Pip-Boy 3000 MK IV.
I branched off from the Fallout 3 style Pip-Boy 3000 code.
The graphics are positioned for a 720x720 display.

======

Adding radio stations is now as easy as making a folder in sounds/radio with MP3, OGG or WAV files.
Make a file name Station.py, with station_name = "Your name here" to set the menu text. The folder name used if the file is missing.
Add a number to the beginning of the folder name to set the menu position.

If you want the original in-game music you can use the B.A.E. program to extract the files from the game, then the Yakitori Audio Converter to convert them back to MP3 files.

======

Navigation:
F1 - Stats
F2 - Inventory
F3 - Data
F4 - Map
F5 - Radio
F6 - Boot screen

1,2,3,4, etc to navigate the sub-header menu

Up/Down arrow keys to navigate the sub-menus

+/- to zoom the map

======

Supports caching and offline loading of maps.
* In settings.py set 'LOAD_CACHED_MAP = False'
* Run the application once
* In settings.py set 'LOAD_CACHED_MAP = True'
* Pypboy will now load the cached map on starting

======

## Autors
* Major overhaul by ZapWizard for the Functional Pip-Boy 3000 MK IV GUI

* Fixes and Updates by kingpinzs

* Fixes and Updates by amolloy

* Fixes and Updates by Goldstein

* Updates by Sabas of The Inventor's House Hackerspace

* Originally by grieve work original<br>

======

## License
MIT

======

### Enable app to startup on boot
pi@XXXX:~/Downloads/pypboy $ cat ~/launch_pipboy.sh
#!/bin/bash
cd ~/Downloads/pypboy
python ./main.py

pi@XXXX:~/Downloads/pypboy $ grep launch_pipboy /etc/lightdm/lightdm.conf
session-setup-script=/home/pi/launch_pipboy.sh
pi@XXXX:~/Downloads/pypboy $
