pypboy
======

Notes from ZapWizard:
This is a work in progress of the code for my Functional Pip-Boy 3000 MK IV.
I branched off from the Fallout 3 style Pip-Boy 3000 code.
Most of the graphics are hard coded for my 720x720 display to make positioning exact.

======

Supports caching and offline loading of maps.
* In settings.py set 'LOAD_CACHED_MAP = False'
* Run the application once
* In settings.py set 'LOAD_CACHED_MAP = True'
* Pypboy will now load the cached map on starting

## Autors
* Fixes and Updates by kingpinzs

* Fixes and Updates by amolloy

* Fixes and Updates by Goldstein

* Updates by Sabas of The Inventor's House Hackerspace

* Originally by grieve work original<br>

* Updates by ZapWizard for Pip-Boy 3000 MK IV GUI

## License
MIT

### Enable app to startup on boot
pi@XXXX:~/Downloads/pypboy $ cat ~/launch_pipboy.sh
#!/bin/bash
cd ~/Downloads/pypboy
python ./main.py

pi@XXXX:~/Downloads/pypboy $ grep launch_pipboy /etc/lightdm/lightdm.conf
session-setup-script=/home/pi/launch_pipboy.sh
pi@XXXX:~/Downloads/pypboy $
