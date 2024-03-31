import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '64bit':
    print('\n Your device is 64 bit')
    os.system('clear')
    os.system('git pull')
    os.system('python gram1_enc.py')
else:
    exit(" your device is not 64 ")
