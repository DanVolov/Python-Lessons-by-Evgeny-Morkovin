#Систему логирования с различными обработчиками
# (Warning, error, debug, info)

class Log_level:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

class Log:
    def __init__(self, message, level=Log_level.DEBUG):
        self.message = message
        self.level = level


class File_log(Log):
    def __init__(self, filename, message, level=Log_level.DEBUG):
        self.filename = filename
        super().__init__(message, level)

    def write(self):
        with open(self.filename, 'a') as f:
            f.write(self.message + '\n')


filelog = File_log('log.txt', 'Igbrdb', Log_level.INFO)
filelog.write()