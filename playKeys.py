from pynput import keyboard as kb
from pynput.keyboard import Key, Controller
from time import sleep
import sys
import random


# ==============================================================================
# ==============================================================================
# ==============================================================================
# Options
# TODO save options to recordings themselves

startKey = Key.shift

# How many times to replay the sequence, 0 for forever 
replaysTotal = 1

# Interval between replays, in _seconds_
replayInterval: float = 0

# Set to true to enable randomized interval between replays in range, in _seconds_
#   <intervalMinBoundary, intervalMaxBoundary>
randomizeInterval = False 
intervalMinBoundary: int = 0
intervalMaxBoundary: int = 2

# Set to true to randomize time when keys pressed/released
randomizePress = False
randomizeRelease = False
# Adds random offset to time of key press or key release, in _milliseconds_
#   * realPressTime = pressTime + rand<-offset, +offset>
pressOffset: int = 50
releaseOffset: int = 50


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================

TOTAL_ITEMS_PER_LINE = 3
STATE_PRESSED = 'P'
STATE_RELEASED = 'R'
SECS_TO_MILLIS = 0.001

keyboard = Controller()



# Type 'Hello World' using the shortcut type method

def replayLine(toWait, state, key):
    if state == STATE_PRESSED:
        sleep(toWait + float(randomizePress) * 
              abs((random.randrange(-pressOffset, pressOffset) * SECS_TO_MILLIS)))
        keyboard.press(key)
    elif state == STATE_RELEASED:
        sleep(toWait + float(randomizeRelease) * 
              abs((random.randrange(-releaseOffset, releaseOffset) * SECS_TO_MILLIS)))
        keyboard.release(key)
    
def preprocessItems(toWait, state, key):
    toWait = float(toWait)
    key = key.strip()

    realKey = None
    # Is just a key char
    if key[0] == "'":
        realKey = key[1]
    # Special key
    else:
        realKey = eval(key)
    return (toWait, state, realKey)

def readRecordingsFromFile(fileName):
    lines = []
    with open(fileName) as f:
        for line in f:
            lines.append(line)

    itemList = []
    for line in lines:
        items = line.split(':')
        if len(items) == TOTAL_ITEMS_PER_LINE:
            itemList.append(preprocessItems(*items))

    return itemList

def replayRecordings(recordings):

    increment = int(bool(replaysTotal))
    i = increment
    while i <= replaysTotal:

        for item in recordings:
            replayLine(*item)

        if replayInterval > 0 and not randomizeInterval:
            sleep(replayInterval)
        elif randomizeInterval:
            sleep(random.randrange(intervalMinBoundary, intervalMaxBoundary))

        i += increment
    

if  __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1]:
        print('Error: please supply a name of the file as argument')
        sys.exit(1)

    fileName = sys.argv[1]

    recs = readRecordingsFromFile(fileName)

    # Wait for the start key to be pressed
    if startKey is not None:
        with kb.Events() as events:
            for event in events:
                if event.key == startKey:
                    break

    replayRecordings(recs)

