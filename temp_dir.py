import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
import glob
import shutil
import datetime
from optparse import OptionParser

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    print(datetime.date.today())
    datenm = "{0:%Y%m%d}".format(datetime.date.today())
    dirnum = len(glob.glob("./temp_" + datenm + "*/"))
    cpname = "temp_{}{:03}".format(datenm, dirnum)
    print(cpname)
    shutil.copytree("./temp/", cpname)

    filename = "./temp/not_ignore.text-test.txt"
    basename = os.path.basename(filename)
    dir_name = os.path.dirname(filename)
    sub_name = os.path.basename(os.path.dirname(filename))
    rootname, ext_name = os.path.splitext(filename)
    print(basename)
    print(dir_name, sub_name)
    print(rootname, ext_name)
