"""
Logger configuration module for console output with OTEL integration.

This module sets up the standard console logger and attaches the OTEL handler
(from otel_handler.py) so that logs are both printed to the console and sent
to the OpenTelemetry Collector in a structured format.
"""

import logging

from bot.config.logging import logging_config
from bot.utils.otel_handler import otel_handler

# creates logger
console_logger = logging.getLogger(logging_config.logger_prefix)

# sets log level to info
log_level_num = getattr(logging, logging_config.logger_level, logging.INFO)
console_logger.setLevel(log_level_num)

# formats logger output
formatter = logging.Formatter(logging_config.logger_format)

# sets the formatter
otel_handler.setFormatter(formatter)
console_logger.addHandler(otel_handler)

console_logger.info("✅ Logger is successfully configured.")
