#!/bin/python


import glob
import re
#import pandas as pd

path = "/cluster/projects/tikhonovalab/Ximing/XFE4KJN/FER18687.20211103/211101_A00987_0301_BHL5WNDRXY/"

file_list=glob.glob(path + '*R1*.gz')

with open('samples.tsv', 'w') as f:
        f.write("sample\tread1\tread2\n")
        for filename in file_list:
                samplename = filename.split("_L001_R1_")[0]
                samplename = re.sub(path, "", samplename)
                r1 = glob.glob(path + samplename + "*R1*.gz")[0]
                r1 = re.sub(path, "", r1)
                r2 = glob.glob(path + samplename + "*R2*.gz")[0]
                r2 = re.sub(path, "", r2)
                f.write(samplename + "\t" + r1 + "\t" + r2 + "\n")
				