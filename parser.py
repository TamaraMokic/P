import os
import sys
import argparse
import pathlib

def parser():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('datapath', type=pathlib.Path)
        args = parser.parse_args()

        path = str(args.datapath)
        directories = os.listdir(path)
        return path

    except IOError:
        Log.Logovanje.log_error( None,"Pogresna putanja")


