SimKey
======

A Python script to record keystrokes and play them back at predefined intervals

Example:

```

```


How to Run:

* Activate the virtual environment

Windows:
```
$ tutorial-env\Scripts\activate.bat
```

Unix or MacOS:
```
$ source tutorial-env/bin/activate
```

* Run your script:
```
$ python3 simulateKeys.py
```

## Scripts
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



