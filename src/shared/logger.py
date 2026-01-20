import logging
import sys
from pathlib import Path

def setup_logger(name: str = "100days", log_level: int = logging.INFO):
    """
    Sets up a structured logger that outputs to console and file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # dedicated format for nicely aligned logs
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # File Handler
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(logs_dir / "app.log")
    file_handler.setFormatter(formatter)

    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
