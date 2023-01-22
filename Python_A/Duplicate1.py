from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd = open(path,'rb')
    