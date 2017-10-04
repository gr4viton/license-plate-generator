#!/bin/bash/env python

import sys
import re
import random

fname = 'spz.svg'
# font in file is
# font-pro-spz-cr-1-p23423.ttf
# from: https://www.slunecnice.cz/sw/font-pro-spz-cr/stahnout/27210/
# the letters are individual objects and are horizontal-centered and grouped together
with open(fname, 'r') as f:
    txt = f.readlines()

#
forbid = 'OQI'
alphas = [chr(num) for num in range(ord('A'), ord('Z')) if chr(num) not in forbid]
# wiki
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Czech_Republic
alphas = list('ABCEHJKLMPSTUVZ')

def rnd_char(char):
    if char.isalpha():
        out = random.choice(alphas)
    elif char.isdigit():
        out = str(random.randrange(0, 9+1))
    else:
        out = char
    return out

def mangle(line):
    subs = ['>A<', '>0 <']
    new_line = line
    for sub in subs:
        #print(type(sub), type(line))
        if sub in line:
            new_sub = ''.join([rnd_char(ch) for ch in sub])
            new_line = re.sub(sub, new_sub, line)
            print('{}\t->\t{}'.format(sub, new_sub))
            print('{}\t->\t{}'.format(line, new_line))

    return new_line

#print(txt)
#out = s
out = [mangle(l) for l in txt]

out_name = fname + '_out.svg'
with open(out_name, 'w') as f:
    f.writelines(out)
#sys.pause()
