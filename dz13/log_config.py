[loggers]
keys = root, loggerServer

[handlers]
keys = fileHandler 

[formatters]
keys = logFormatter

[logger_root]
level = DEBUG
handlers = fileHandler

[logger_loggerServer]
level = DEBUG
qualname = loggerServer
handlers = fileHandler

[handler_fileHandler]
class = FileHandler
level = DEBUG
formatter = logFormatter
args = ('log.txt', 'a')

[formatter_logFormatter]
format = %(asctime)s - %(levelname)s - %(name)s - %(message)s
datefmt = %d-%b-%y %H:%M:%S



