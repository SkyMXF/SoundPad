import os
import logging
from logging.handlers import RotatingFileHandler


LOG_DIR_PATH = os.path.join("logs")
Logger = logging.getLogger("Sound Pad")


def init_logger(level: int = logging.DEBUG):

    logger = Logger
    logger.setLevel(level)

    # rotate file handler
    if not os.path.isdir(LOG_DIR_PATH):
        os.makedirs(LOG_DIR_PATH)
    handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR_PATH, "running.log"),
        maxBytes=1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # cmd handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
