from time import gmtime, strftime
import pickle
import json

# logging functionality
log = open('log', 'a')
def writeLog (message):
    log.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": \t" + message + "\n")

configs = { 'wiiEmu': {
                'name': 'Dolphin',
                'location': 'usr/dolphin',
                'controller': 'xinput',
                'fullscreen': True,
            },
            'n64Emu': {
                'name': 'Project 64',
                'location': 'usr/P64/exe',
                'controller': 'xinput',
                'fullscreen': True
            }
        }

file = open('bin/configs', 'wb')
writeLog("Pickling configs...")
try:
    pickle.dump(configs, file, protocol=pickle.HIGHEST_PROTOCOL)
    writeLog("Pickling complete")
except Exception as inst:
    writeLog("Config loading failed:\n" + str(type(inst)) + "\n" + inst.message)

file = open('bin/configs', 'rb')
writeLog("Loading configs...")
try:
    conf = pickle.load(file)
    writeLog("Config loading complete")
except Exception as inst:
    writeLog("Config loading failed:\n" + str(type(inst)) + "\n" + inst.message)

print(configs['wiiEmu']['name'])

while True:
    reply = raw_input("Enter input (type 'stop' to break): ")
    if reply == "stop": break
    print(reply)
