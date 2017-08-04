import eyed3
import os
import subprocess
import sys
import os.path

if sys.platform == "linux" or sys.platform == "linux2":
    sox = '/usr/bin/sox'
else:
    sox = '/usr/local/bin/sox'

def create_silence_from_list_of_files(list_of_files, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for f in list_of_files:
        create_silence_from_file(f, output_folder + '/' + f.split('/')[-1][:-4] + 's.' + f.split('/')[-1][-3:])

def create_silence_from_file(input_file, output_file):
    if os.path.isfile(output_file): return
    if not (input_file[-3:] == 'wav' or input_file[-3:] == 'mp3'): return
    subprocess.call([sox, '-v', '0', input_file, output_file])

def create_silence_from_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for f in os.listdir(input_folder):
        if not (f[-3:] == 'wav' or f[-3:] == 'mp3'): continue
        create_silence_from_file(input_folder + '/' + f, output_folder + '/' + f[:-4] + 's.' + f[-3:])
