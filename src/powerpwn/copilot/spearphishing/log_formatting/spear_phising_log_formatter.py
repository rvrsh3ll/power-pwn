from powerpwn.copilot.spearphishing.log_formatting.log_type_enum import LogType


class SpearPhishingLogFormatter:
    """
    A class for formatting log messages from spearpishing tool
    """

    def format(self, message: str, log_type: LogType) -> str:
        if log_type == LogType.none:
            return message
        if log_type == LogType.tool:
            return f"[TOOL]: {message}"
        if log_type == LogType.prompt:
            return f"[PROMPT]: {message}"
        return f"[RESPONSE]: {message}"
