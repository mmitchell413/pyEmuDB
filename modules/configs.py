import logging
import pickle
import json

class Configs():
    configs = {}

    def __init__(self):
        try:
            self.configs = self.loadConfigs()
            if not bool(self.configs):
                print("No configs found, initializing configs now")
                self.configs = {'n64': {},
                                'wii': {},
                                'snes': {},
                                'nes': {},
                                'gba': {},
                                'gb': {},
                                'gbc': {}
                                }
                self.writeConfigs(self.configs)
        except Exception as inst:
            logging.writeLog("Config loading failed:\n" + str(type(inst)) + "\n" + inst.message)
        return None
        # file = open('bin/configs', 'r')
        # logging.writeLog("Loading configs...")
        # try:
        #     configs = pickle.load(file)
        #     logging.writeLog("Config loading complete")
        #     print bool(configs)
        #     if not bool(configs):
        #         print "No configs found"
        #         configs = { 'wii': {
        #                         'name': 'Dolphin',
        #                         'location': 'usr/dolphin',
        #                         'controller': 'xinput',
        #                         'fullscreen': True,
        #                         'platform': 'wii'
        #                     },
        #                     'n64': {
        #                         'name': 'Project 64',
        #                         'location': 'usr/P64/exe',
        #                         'controller': 'xinput',
        #                         'fullscreen': True,
        #                         'platform': 'n64'
        #                     }
        #                 }
        #         print configs
        # except Exception as inst:
        #     logging.writeLog("Config loading failed:\n" + str(type(inst)) + "\n" + inst.message)
        # return None

    def __getitem__(self, i):
        return self.configs[i]

    def __iter__(self):
        return self.configs.itervalues()

    def __setitem__(self, set, to):
        self.configs[set] = to

    def toDict(self):
        return self.configs

    def writeConfigs(self, configs):
        file = open('bin/configs', 'w')
        logging.writeLog("Pickling configs...")
        try:
            pickle.dump(self.configs, file, protocol=pickle.HIGHEST_PROTOCOL)
            logging.writeLog("Pickling complete")
            return True
        except Exception as inst:
            logging.writeLog("Config writing failed:\n" + str(type(inst)) + "\n" + inst.message)
            return False

    def loadConfigs(self):
        file = open('bin/configs', 'r')
        logging.writeLog("Loading configs...")
        try:
            conf = pickle.load(file)
            logging.writeLog("Config loading complete")
            return conf
        except Exception as inst:
            logging.writeLog("Config loading failed:\n" + str(type(inst)) + "\n" + inst.message)
            return False
