from pynput import keyboard
import time 
import sys


# ==============================================================================
# ==============================================================================
# ==============================================================================
# Options
# TODO save options to recordings themselves

# On press starts recording
startKey = keyboard.Key.shift

# On press of the key ends the recording
exitKey = keyboard.Key.esc

# Set how long to record in seconds
# 0 to ignore the time
duration = 0

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


recording = []
DELIM = ':'
ENDLINE = '\n'
timer = 0
exitKeyPressed = False


def resetTimer():
    global timer
    timer = time.time()
    return timer

def endTimer():
    now = time.time()
    interval = now - timer
    resetTimer()
    return interval

def addPress(key):
    recording.append(str(endTimer()) + DELIM + 'P' + DELIM + key + ENDLINE)

def addRelease(key):
    recording.append(str(endTimer()) + DELIM + 'R' + DELIM + key + ENDLINE)

def on_press(key):
    skey = str(key)
    if key == exitKey:
        global exitKeyPressed
        exitKeyPressed = True
        print('Exit recording')
        return
    addPress(skey)

def on_release(key):
    skey = str(key)
    addRelease(skey)

def writeRecordings(fileName):
    print('Writing recordings to file: "{}"'.format(fileName))
    f = open(fileName, 'w')
    for r in recording:
        f.write(r)
    f.close()

if  __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1]:
        print('Error: please supply a name of the file as argument')
        sys.exit(1)

    fileName = sys.argv[1]

    # Waits for the start key to be pressed
    if startKey is not None:
        with keyboard.Events() as events:
            for event in events:
                if event.key == startKey:
                    break

    print('>> Recording <<')
    startTime = resetTimer()

    # Start the listening threads
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    # Wait for the recording to end
    if duration == 0:
        while not exitKeyPressed:
            time.sleep(1)
    else:
        while not exitKeyPressed:
            now = time.time()
            if now - startTime >= duration:
                break
            time.sleep(1)

    listener.stop()

    writeRecordings(fileName)

    sys.exit(0)


