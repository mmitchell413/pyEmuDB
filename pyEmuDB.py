from modules.configs import Configs
from modules.emulator import Emulator
from modules import game
from modules.game import Game

configs = Configs().configs
emu = {}
for e in configs:
    emu[e] = Emulator(e)

emu['wii']['location'] = 'usr/Dolphin'
print emu['wii']['location']
print emu['nes'].settings['controller']

gl = game.loadGamesList()
pkblk = Game('Pokemon Black')
pkblk['location'] = '/usr/roms/Pokemon Black.ds'
print pkblk['name'] + ": " + pkblk['location']
