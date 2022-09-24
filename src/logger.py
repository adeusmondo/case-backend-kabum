from aiologger.logger import Logger as AIOLogger
from aiologger.formatters.base import Formatter
from aiologger.handlers.streams import AsyncStreamHandler

from config import Config


class Logger(AIOLogger):
    def __init__(self) -> None:
        super().__init__(level=Config.LOG_LEVEL)
        formatter = Formatter(fmt='%(asctime)s [%(process)d] [%(funcName)s] [%(levelname)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
        default_handler = AsyncStreamHandler(level=Config.LOG_LEVEL, formatter=formatter)
        self.add_handler(default_handler)
