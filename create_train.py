from os import listdir
import os
import time
import ast
import sys
from PIL import Image

label_path = "train/"
files = [f for f in listdir(label_path)]

for f in files:
    if f.lower().endswith('png'):
        relative_path = "kitti/train/"
        output = open("train.txt", "a+")
        output.write(relative_path + f + '\n')
