import logging


class Logger:
    def __init__(self, file, line_no):
        self.logger = logging.getLogger(file)
        self.file_name = file
        self.line_no = line_no
        # Create handlers
        self.stream_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler('file.log')

    def log_warning(self, message):
        # Configure level and formatter and add it to handlers
        self.stream_handler.setLevel(logging.WARNING)  # warning and above is logged to the stream
        self.file_handler.setLevel(logging.WARNING)  # error and above is logged to a file

        stream_format = logging.Formatter(f'%(name)s : {self.line_no} - %(levelname)s - %(message)s')
        file_format = logging.Formatter(f'%(asctime)s - %(name)s : {self.line_no} - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(stream_format)
        self.file_handler.setFormatter(file_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.logger.warning(message)

    def log_info(self, message):
        # Configure level and formatter and add it to handlers
        self.stream_handler.setLevel(logging.INFO)  # warning and above is logged to the stream
        self.file_handler.setLevel(logging.INFO)  # error and above is logged to a file

        stream_format = logging.Formatter(f'%(name)s : {self.line_no} - %(levelname)s - %(message)s')
        file_format = logging.Formatter(f'%(asctime)s - %(name)s : {self.line_no} - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(stream_format)
        self.file_handler.setFormatter(file_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.logger.info(message)

    def log_debug(self, message):
        self.stream_handler.setLevel(logging.DEBUG)  # warning and above is logged to the stream
        self.file_handler.setLevel(logging.DEBUG)  # error and above is logged to a file

        stream_format = logging.Formatter(f'%(name)s : {self.line_no} - %(levelname)s - %(message)s')
        file_format = logging.Formatter(f'%(asctime)s - %(name)s : {self.line_no} - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(stream_format)
        self.file_handler.setFormatter(file_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.logger.debug(message)

    def log_error(self, message):
        self.stream_handler.setLevel(logging.ERROR)  # warning and above is logged to the stream
        self.file_handler.setLevel(logging.ERROR)  # error and above is logged to a file

        stream_format = logging.Formatter(f'%(name)s : {self.line_no} - %(levelname)s - %(message)s')
        file_format = logging.Formatter(f'%(asctime)s - %(name)s : {self.line_no} - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(stream_format)
        self.file_handler.setFormatter(file_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.logger.error(message)

    def log_critical(self, message):
        self.stream_handler.setLevel(logging.CRITICAL)  # warning and above is logged to the stream
        self.file_handler.setLevel(logging.CRITICAL)  # error and above is logged to a file

        stream_format = logging.Formatter(f'%(name)s : {self.line_no} - %(levelname)s - %(message)s')
        file_format = logging.Formatter(f'%(asctime)s - %(name)s : {self.line_no} - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(stream_format)
        self.file_handler.setFormatter(file_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.logger.critical(message)
