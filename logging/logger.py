#!/usr/bin/env python
"""
    This is a simple example to configure the logging packet to log in different
    files and to the console. Feel free to use some methods of this class
    and configure it on your own way or use the whole class

    In this example, we configure:

    * console output with loglevel "0" => prints all (should be configureable at the CLI
    * (user)logfile to log all above the warning loglevel
        in the most cases it is enough to use a tool
    * debug logfile to log all logged information.
        this logfile may be interesting for developer

    Written by DerCoop <dercoop@users.sourceforge.net>

    """


__author__ = 'coop'
__license__ = "GPLv2"

import logging as log


class myLogger:
    """Simple example class to configure logging for different output"""
    def __init__(self):
        self.__config = {'debugfile': None,
                       'logfile': None,
                       'formatstring': '[%(levelname)s]: %(message)s'}
        self.__loglevel = {'console': log.NOTSET,
                         'debug': log.WARN,
                         'log': log.DEBUG}

    @staticmethod
    def __reset_old_settings__():
        """reset old log settings"""
        if log.root:
            del log.root.handlers[:]

    def set(self, key, value):
        """set a key

        Arguments:
        key:    name of the key to set
        value:  the value to set
        """
        self.__config[key] = value

    def get(self, key, default=None):
        """returns the value of a key

        Arguments:
        key:     name of the key
        default: default value

        Return:
        the value of the key (or the default value if the key do not exists)
        """
        return self.__config.get(key, default)

    def set_level(self, handler, level):
        """set a loglevel

        Arguments:
        key:    name of the loglevel
        value:  the value to set
        """
        # TODO validate the loglevel
        self.__loglevel[handler] = level

    def get_level(self, level):
        """returns the value of a key

        Arguments:
        key:     name of the key
        default: default value
        """
        return self.__loglevel.get(level, None)

    @staticmethod
    def _configure_root():
        """configure the root logger

        set the level as low as possible because
        (at least as the lowest configured level
        """
        root_logger = log.getLogger()
        root_logger.setLevel(log.NOTSET)
        return root_logger

    def _configure_console_handler(self, log_formatter):
        """configuration helper for the console handler

        Arguments:
        log_formatter:  formatter object for the logger

        Return:
        the log handler
        """
        log_console_handler = log.StreamHandler()
        log_console_handler.setFormatter(log_formatter)
        log_console_handler.setLevel(self.get_level('console'))

        return log_console_handler

    def _configure_logfile(self, log_formatter):
        """configuration helper for the logfile

        Arguments:
        log_formatter:  formatter object for the logger

        Return:
        the log handler
        """
        log_debug_to_file = log.FileHandler(self.get('debugfile'))
        log_debug_to_file.setFormatter(log_formatter)
        log_debug_to_file.setLevel(self.get_level('debug'))

        return log_debug_to_file

    def _configure_debugfile(self, log_formatter):
        """configuration helper for the debug file

        Arguments:
        log_formatter:  formatter object for the logger

        Return:
        the log handler
        """
        log_log_to_file = log.FileHandler(self.get('logfile'))
        log_log_to_file.setFormatter(log_formatter)
        log_log_to_file.setLevel(self.get_level('log'))

        return log_log_to_file

    def configure(self):
        """set the configured options"""
        # TODO validate all needed options
        log_formatter = log.Formatter(self.get('formatstring'))

        root_logger = self._configure_root()
        root_logger.addHandler(self._configure_console_handler(log_formatter))
        root_logger.addHandler(self._configure_logfile(log_formatter))
        root_logger.addHandler(self._configure_debugfile(log_formatter))


def logger():
    """example for the usage of this class"""
    # definitions
    formatstring = '[%(levelname)s]: alfred: %(message)s'

    debugfile = 'logfile.debug'
    logfile = 'logfile.log'

    debug_loglevel = log.DEBUG
    log_loglevel = log.WARN
    console_loglevel = log.ERROR

    # start configuration
    mylogger = myLogger()

    mylogger.set('formatstring', formatstring)
    mylogger.set('debugfile', debugfile)
    mylogger.set('logfile', logfile)

    mylogger.set_level('debug', debug_loglevel)
    mylogger.set_level('log', log_loglevel)
    mylogger.set_level('console', console_loglevel)

    # activate this stuff
    mylogger.configure()

    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')


if __name__ == '__main__':
    logger()