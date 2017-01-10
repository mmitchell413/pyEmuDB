from modules.configs import Configs
from modules.emulator import Emulator

configs = Configs().configs
emu = {}
for e in configs:
    emu[e] = Emulator(e)

emu['wii']['location'] = 'usr/Dolphin'
print emu['wii']['location']
print emu['nes'].settings['controller']
