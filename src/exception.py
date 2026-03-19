import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        error_message: the message you want to show
        error_detail: usually sys module to extract traceback info
        """
        super().__init__(error_message)
        self.error_message = self.get_error_message(error_message, error_detail)

    def get_error_message(self, error_message, error_detail: sys):
        """
        Creates a formatted error message with traceback
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown line"

        return f"Error in script: {file_name} at line {line_number} -> {error_message}"

    def __str__(self):
        return self.error_message