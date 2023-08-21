import logging

class CustomLogging():

    def Create_Logger(self, logger_name):

        logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
        logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

        file_handler = logging.FileHandler(logger_name) # Indicamos el nombre del archivo
        file_handler.setFormatter(formatter) # Configuramos el formato

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler) # Agregamos el archivo
        logger.addHandler(stream_handler)

        return logger