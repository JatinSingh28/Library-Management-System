import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='logs.log', max_file_size=1024*1024, backup_count=5):
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    # Create a rotating file handler
    handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_file_size,
        backupCount=backup_count
    )

    # Create a formatter with more detailed information
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s'
    )

    # Set the formatter for the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger