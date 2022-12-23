# General

Just a fun script to test automating keystrokes in different ways

# TODO:
* put the stuff the code will do into a config file and run from that instead
* instead of starting direct there should be a small gui with a start/stop button

# What it will do
* give you a 5 second countdown to be able to tab over to the window you want it to interact with
* press left or right arrow for a random amount of seconds
* then pressing w/a/s or d for a few random seconds
* sleep for a tiny bit
* then press the "oposite" key from the first keys for almost the same time as the initial pressing ie:  
  w -> s  
  s -> w  
  a -> d  
  d -> a  
* then it will sleep for a few random seconds between the key-presses
* lastly it will will sleep for a random amount of time


## it will also randomly :
* quickly press the space bar in the middle of holding the keys down
* press nr 9 before pressing the keys

# binary
The project has a compiled exe file uploaded in the binary folder.
It's compiled with PyInstaller, use it or don't the code runs just as well as just python.
