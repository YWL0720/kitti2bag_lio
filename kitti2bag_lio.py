#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

import argparse
from collections import namedtuple




Config = namedtuple('Config', ['date', 'sequence'])


def get_arguments():
    """ 
    Get command-line arguments
    """
    # init parser:
    parser = argparse.ArgumentParser("Generate 100Hz OXTS measurements for LIO/VIO development.")

    # add required and optional groups:
    required = parser.add_argument_group('Required')
    optional = parser.add_argument_group('Optional')

    # add required:
    required.add_argument(
        "-d", dest="date", help="Input directory of KITTI test drive data.", 
        required=True, type=str
    )
    required.add_argument(
        "-s", dest="sequence", help="Input sequence of KITTI data.", 
        required=True, type=str
    )

    # parse arguments:
    return parser.parse_args()


def main(config):
    

    synced_bag_name = "kitti_" + config.date + "_drive_" + config.sequence + "_synced.bag"
    # print("Generating synced bag ...")
    # os.system("python -m kitti2bag -t %s -r %s raw_synced ." %(config.date, config.sequence))
    # os.system("mv %s synced.bag" % synced_bag_name)
    # print("Successfully generate synced.bag")
    # print()

    print("Generating 100Hz oxts ...")
    os.system("python pre.py -d %s -s %s" %(config.date, config.sequence))
    print()
    print("Successfully generate 100Hz oxts")
    print()

    print("Generating 100Hz bag")
    os.system("python -m kitti2bag -t %s -r %s raw_synced ." %(config.date, config.sequence))
    bag_name = config.date + "_drive_" + config.sequence + "_100hz.bag"
    os.system("mv %s %s" % (synced_bag_name, bag_name))
    print()
    print("Successfully generate " + bag_name)
    print()

    sys.exit(os.EX_OK) 

if __name__ == '__main__':
    # parse arguments:
    arguments = get_arguments()

    config = Config(
        date = arguments.date,
        sequence = arguments.sequence
    )

    main(config)
