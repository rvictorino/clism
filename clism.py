#!/usr/bin/python3

import argparse
import clism_setup
import clism_test
import clism_submit

parser = argparse.ArgumentParser(description='Parse exercise and track arguments')
parser.add_argument('type', choices=['setup', 'test', 'submit'])
parser.add_argument('--exercise')
parser.add_argument('--track')

args = parser.parse_args()
type = args.type
exercise = args.exercise
track = args.track

if type == 'setup':
    clism_setup.execute(exercise, track)
elif type == 'test':
    clism_test.execute()
elif type == 'submit':
    clism_submit.execute()
