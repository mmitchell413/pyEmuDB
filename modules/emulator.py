from configs import Configs
import logging

class Emulator(object):

    def __init__(self, platform):
        self.settings = {}
        self.settings['platform'] = platform
        self.loadSettings()
        return None

    def __getitem__(self, i):
        return self.settings[i]

    def __setitem__(self, set, to):
        self.settings[set] = to
        self.dumpConfigs(self.settings)

    def loadSettings(self):
        configs = Configs()
        logging.writeLog("Loading configs for " + self.settings['platform'] + " emulator")
        for prop in configs[self.settings['platform']]:
            self.settings[prop] = configs[self.settings['platform']][prop]

    def dumpConfigs(self, settings):
        configs = Configs()
        logging.writeLog("Dumping configs for " + self.settings['platform'] + " emulator")
        configs[self.settings['platform']] = self.settings
        configs.writeConfigs(configs)
        pass
