Record and Replay Keystrokes
============================

A pair of Python scripts for recording and replaying keystrokes with various 
configuration options.

Uses [pynput](https://pypi.org/project/pynput/) library to control and 
monitor input from keyboard.

## Requirements
- Python3.7+

Listed in [requirements.txt](requirements.txt):
- evdev==1.4.0
- pynput==1.7.5
- python-xlib==0.31
- six==1.16.0

## Setup
It is recommended to use virtual environment to set up the appropriate Python 
environment, as described in the [documentation](https://docs.python.org/3/tutorial/venv.html):
```
python3 -m venv env
```
Activate the environment:
* Windows:
```
env\Scripts\activate.bat
```
* Unix or MacOS:
```
source env/bin/activate
```
Install all the necessary packages:
```
python3 -m pip install -r requirements.txt
```
Now you should be ready to run the scripts, as described below.

## Scripts
See the configuration options at the top of the scripts:
- recordKeys.py
- playKeys.py

### Record your keystrokes
Run using:
```
$ python3 recordKeys.py recording.txt
```
When run, starts recording your keystrokes to a file. Only one key can be 
recorded at a time, as it is with typing (but many keys can be released at the 
same time).
Options to set:
- a specific key to start recording
- when to end the recording: 
    - set exit key
    - after a duration
    - or both

Outputs a file with recorded keys on each line, in format:
```
<OFP>:<state>:<key>
```
where 
- OFP, is offset from previous key press/release or from start in milliseconds
- state, is the state of the key - either pressed or released

### Replay your recorded keystrokes
Run using:
```
$ python3 playKeys.py recording.txt
```
When run, starts replaying the recorded keys into a focused window.
Options you can set:
- Start of replay: a specific key
- Number of replays: how many times to play the sequence over (positive integer)
- fixed interval between replays, positive float in seconds
- random interval between replays, with lower and upper boundary, positive 
    integers in seconds
- randomize time of press or release with a random offset, positive integer
    in milliseconds


