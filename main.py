#!/usr/bin/python

import argparse
import logging
import sys
import time

def myLogging():

    # ------------------------------------------------------------
    # Base Logging Setup
    # ------------------------------------------------------------

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s',
                        filename='0x01.console.log',
                        filemode='a')

    # ------------------------------------------------------------
    # Logging Handlers
    # ------------------------------------------------------------

    loggerConsole = logging.StreamHandler()
    loggerConsole.setLevel(logging.INFO)

    loggerFile = logging.FileHandler('0x01.file.log', 'a')
    loggerFile.setLevel(logging.INFO)

    # ------------------------------------------------------------
    # Logging Formatters
    # ------------------------------------------------------------

    loggerConsoleFormatter = logging.Formatter('%(name)-2s: %(module)-10s %(levelname)-4s %(message)s')
    loggerConsole.setFormatter(loggerConsoleFormatter)

    loggerFileFormatter = logging.Formatter('%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s')
    loggerFile.setFormatter(loggerFileFormatter)

    # ------------------------------------------------------------
    # Logging getLoggers
    # ------------------------------------------------------------

    logging.getLogger('').addHandler(loggerConsole)
    logging.getLogger('').addHandler(loggerFile)

if __name__=='__main__':

    myLogging()

    description = '0x01 Main'
    logging.info(description)

    while True:

        time.sleep(1)
        logging.info("Here")

# End of File
