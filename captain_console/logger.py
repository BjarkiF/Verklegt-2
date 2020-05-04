import os
import logging
import logging.handlers as handlers

path = 'logs/'
filename = 'captain_console.log'
level=logging.DEBUG

if not os.path.isdir(path):
    os.makedirs(path)

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(filename='%s%s' % (path, filename), level=level, format=format)

logger = logging.getLogger('host_scan')
logger.setLevel(level)

formatter = logging.Formatter(format)

logHandler = handlers.RotatingFileHandler('%s%s' % (path, filename), maxBytes=5*1024*1024, backupCount=2)
logHandler.setLevel(level)
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
