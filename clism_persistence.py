import pickle
import config

def save(conf_dict):
    outfile = open(config.CLISM_DATASTORE_FILENAME, 'wb')
    pickle.dump(conf_dict, outfile)
    outfile.close()

def load():
    infile = open('clism_data','rb')
    conf_dict = pickle.load(infile)
    infile.close()
    return conf_dict
