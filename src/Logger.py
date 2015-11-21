class Log():
    _loggermethod = None

    @staticmethod
    def set_logger(logger):
        Log._loggermethod = logger

    @staticmethod
    def log(msg):
        Log._loggermethod(str(msg))
