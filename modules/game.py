from configs import Configs
import logging

class Game(object):
    def __init__(self, name):
        self.settings = {}
        self.settings['name'] = name
        return None

    def __getitem__(self, e):
        return self.settings[e]

    def __setitem__(self, set, to):
        self.settings[set] = to
        pass



def writeGamesList(gamesList):
    file = open('bin/games', 'w')
    logging.writeLog("Pickling games list...")
    try:
        pickle.dump(self.configs, file, protocol=pickle.HIGHEST_PROTOCOL)
        logging.writeLog("Pickling complete")
        return True
    except Exception as inst:
        logging.writeLog("Games list writing failed:\n" + str(type(inst)) + "\n" + inst.message)
        return False

def loadGamesList():
    file = open('bin/games', 'r')
    logging.writeLog("Loading games list...")
    try:
        gl = pickle.load(file)
        logging.writeLog("Games list loading complete")
        return gl
    except Exception as inst:
        logging.writeLog("Games list loading failed:\n" + str(type(inst)) + "\n" + inst.message)
        return False
