import subprocess
import conf_parser
import clism_persistence

def execute():

    current_project = clism_persistence.load()

    current_track = current_project['track']
    current_dir = current_project['directory']

    config = conf_parser.get_conf()
    track_config = config[current_track]

    subprocess.call(track_config['test_cmd'], shell=True, cwd=current_dir)
