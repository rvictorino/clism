import subprocess
import conf_parser
import clism_persistence
import glob
import fnmatch

def execute():

    current_project = clism_persistence.load()

    current_track = current_project['track']
    current_dir = current_project['directory']

    config = conf_parser.get_conf()
    track_config = config[current_track]

    if 'source_dir' in track_config:
        current_dir = current_dir + '/' + track_config['source_dir']

    descriptor = current_dir + '/*'
    if 'include_files' in track_config:
        descriptor = current_dir + '/' + track_config['include_files']

    files_to_submit = glob.glob(descriptor)

    if 'exclude_files' in track_config:
        files_to_submit = list(
            filter(
                lambda file: not fnmatch.fnmatch(
                    file,
                    track_config['exclude_files']
                ),
                files_to_submit
            )
        )


    subprocess.call(['exercism', 'submit'] + files_to_submit)
