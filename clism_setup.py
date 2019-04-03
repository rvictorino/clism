import subprocess
import conf_parser
import clism_persistence

def execute(exercise, track):

    config = conf_parser.get_conf()
    track_config = config[track]

    output = subprocess.check_output(
         ['exercism', 'download', '--exercise', exercise, '--track', track],
         stderr=subprocess.DEVNULL
    ).decode("utf-8")

    out_directory = output.split('\n')[0]

    current_project = {
        'track': track,
        'directory': out_directory
    }
    clism_persistence.save(current_project)

    subprocess.call(['atom', '.'], cwd=out_directory)

    if 'setup_cmd' in track_config:
        subprocess.call(track_config['setup_cmd'], shell=True, cwd=out_directory)
