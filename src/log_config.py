import logging
import sys

LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s]: %(message)s"
LOG_LEVEL = "INFO"

def setup_logging(level: str = LOG_LEVEL, log_format: str = LOG_FORMAT, log_file: str = None) -> None:
    """
    Configura logging global para o projeto Codex CLI.
    Por padrão, loga para o console. Se log_file for fornecido, loga também em arquivo.
    """
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=log_format,
        handlers=handlers,
        force=True
    )

# Exemplo de uso:
# from src.log_config import setup_logging
# setup_logging(level="DEBUG", log_file="codex.log")
