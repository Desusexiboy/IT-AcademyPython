class testinglog:
    '''Custom logger to store all testing results.'''
    @staticmethod
    def logger_init(some_str):
        ''' Initialise new logger '''
        import logging
        logger = logging.getLogger(some_str)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('rsyncer.log')
        formatter = logging.Formatter('[%(asctime)s] - %(name)11s - %(levelname)6s : %(message)s',
                                      datefmt='%d-%m-%y %H:%M')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def info_log(logger, infostr):
        ''' Log result info message '''
        logger.info(infostr)
