import string
import numpy as np
from utilities.custom_logging import CustomLogging

logger = CustomLogging()
logger = logger.Create_Logger('calculator.log')

#logger2 = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
#logger2.setLevel(logging.DEBUG) # Configuramos el nivel de logging

#formatter2 = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

#file_handler2 = logging.FileHandler('calculator.log') # Indicamos el nombre del archivo

#file_handler2.setFormatter(formatter2) # Configuramos el formato

#logger2.addHandler(file_handler2) # Agregamos el archivo



class Calculator:
    def get_fractions(self, frac_str: (int or float or string)) -> (int or float):
        """Checks a number and returns to float type.

        Parameters
        ----------
        frac_str : int or float or string
            Number in int, float or string type.

        Returns
        -------
        float
            Fixed float type number.
        """
        
        if isinstance(frac_str, (int, float)):
            return frac_str

        if "/" not in frac_str:
            return float(frac_str)
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac


    def sum(self, a: any, b: any) -> (int or float):
        """Gets two numbers, adds them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the sum.
        """

        logger.info("'sum' was called.")
        sum_a = self.get_fractions(a)
        sum_b = self.get_fractions(b)
        return np.sum([sum_a, sum_b])


    def subtract(self, a: any, b: any) -> (int or float):
        """Gets two numbers, subtracts the second from the first,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the substraction.
        """

        logger.info("'substract' was called.")
        minuend = self.get_fractions(a)
        subtrahend = self.get_fractions(b)
        return minuend - subtrahend


    def multiply(self, a: any, b: any) -> (int or float):
        """Gets two numbers, multiplies them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the multiplication.
        """

        logger.info("'multiply' was called.")
        multiplicand = self.get_fractions(a)
        multiplier = self.get_fractions(b)
        return multiplicand * multiplier


    def divide(self, a: any, b: any) -> (int or float):
        """Gets two numbers, divide the first by the second,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the division.
        """

        logger.info("'divide' was called.")
        dividend = self.get_fractions(a)
        divider = self.get_fractions(b)
        
        try:
            return dividend/divider #np.divide(dividend, divider)
        except ValueError:
            logger.error("Error while executing division.")
            return "Error while executing division."
        except ZeroDivisionError:
            logger.error("Division by zero is not allowed!")
            return "Division by zero is not allowed!"
        