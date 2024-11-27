import sys

from loguru import logger
from rich.console import Console

console = Console(color_system="auto")


def setup_logging(*, log_level: str = "INFO") -> None:
    logger.remove()
    logger.add(
        sys.stderr,
        level=log_level,
        format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - {message}",
        colorize=True,
    )
