from time import gmtime, strftime

# logging functionality
log = open('log', 'a')

def writeLog (message):
    log.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": \t" + message + "\n")
