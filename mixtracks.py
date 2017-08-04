import math
import argparse
from random import shuffle
from shutil import rmtree
import os

from utils import shuffle_track, get_name, makedir, convert_mp3, make_track, get_num_files
from music_file import MusicFile
from convert2mp3 import convert_file_2_mp3
from generator import generate_from_list_of_files

def create_accent_grammar(list_of_tracks, num_files_per_group, num_plays,
    num_copies=1, prefix='', to_mp3=False, artist='Accent', album='Accent Training', shuffled='', grammar=False):

    type_file = 'Accent' if not grammar else 'Grammar'
    artist = 'Accent' if not grammar else 'Grammar'
    album = 'Accent Training' if not grammar else 'Grammar Training'
    input_files = []

    for track in list_of_tracks:
        sub_input_files = []
        for f in sorted(os.listdir(type_file +'/' + type_file +'EN/')):
            if not (f[-3:] == 'mp3' or f[-3:] == 'wav'): continue
            if grammar: u = f[1:4]
            else: u = f[6:9]
            if u == '%03d' % (track):
                sub_input_files.append(type_file +'/' + type_file +'EN/' + f)
        if shuffled == "group":
            shuffle(sub_input_files)
        input_files.extend(sub_input_files)

    if shuffled == "all": shuffle(input_files)

    if num_files_per_group == 0:
        num_files_per_group = get_num_files(len(input_files))

    generate_from_list_of_files(input_files, type_file +'/' + type_file +'VN/', type_file, False)
    files = ['output' + type_file + '/' + f.split('/')[-1][:-6] + type_file + f.split('/')[-1][-4:] for f in input_files]
    # Shuffle files

    for copies in range(int(num_copies)):
        result = shuffle_track(files, num_plays, num_files_per_group)

        makedir(type_file + '(wav)')
        name = get_name(type_file, prefix, num_plays)
        make_track(result, name)
        convert_mp3(to_mp3, name, type_file + '(mp3)', artist, album)

    rmtree('output' + type_file)
