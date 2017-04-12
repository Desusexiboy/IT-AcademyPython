'''Test for changing file attributes'''
from logger_for_tests import testinglog

logger = testinglog.logger_init('Main')

class exectest:
    @staticmethod
    def runexectest():
        import os
        testinglog.info_log(logger, '\n### main.py start ###')
        #create custom linux file with 001 permissions - executable
        os.mkdir('exectest', 0001)
        testinglog.info_log(logger, '\n### TC001: {}  ###'.format(os.access('exectest',os.X_OK)))
        #switch file permission to not executable
        os.fchmod('exectest', 0000)
        testinglog.info_log(logger, '\n### TC001: {}  ###'.format(os.access('exectest', os.X_OK)))
        #switch permission to executable
        os.fchmod('exectest', 0001)
        if os.access("exectest", os.X_OK):
            testinglog.info_log(logger, '\n### TC001: passed ###')
        else:
            testinglog.info_log(logger, '\n### TC001: failed ###')
