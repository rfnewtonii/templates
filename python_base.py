#!/usr/bin/env python

import argparse
import logging
import os

parser = argparse.ArgumentParser(
    description='<Description of Process>',
    allow_abbrev=False
)

parser.add_argument(
    '--debug',
    help='OPTIONAL: Set Logging Level Debug',
    required=False,
    action='store_const',
    dest='loglevel',
    const=logging.DEBUG,
    default=logging.INFO
)

parser.add_argument(
    '--log',
    help='OPTIONAL: Override Default Log <Path/To/File>',
    required=False,
    default='{}.log'.format(
        os.path.splitext(os.path.abspath(os.path.expanduser(__file__)))[0]
    )
)

args = parser.parse_args()

try:
    logging.basicConfig(
        format=('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        datefmt=('%Y-%m-%d %H:%M:%S'),
        filename=args.log,
        level=args.loglevel
        )
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.info(args)
except BaseException as err:
    print('Logger Critical...\n{}'.format(err))
    exit(1)
