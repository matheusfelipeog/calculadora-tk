# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

class Calculador(object):
    """Classe responsável por realizar todos os calculos da calculadora"""
    
    def calculation(self, calc):
        """Responsável por receber o calculo a ser realizado, retornando
        o resultado ou uma mensagem de erro em caso de falha.

        """
        return self.__calculation_validation(calc=calc)

    def __calculation_validation(self, calc):
        """Responsável por verificar se o calculo informado é possível ser feito"""

        try:
            result = eval(calc)

            return self.__format_result(result=result)
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            return 'Erro' 

    def __format_result(self, result):
        """Formata o resultado em notação cientifica caso seja muito grande
        e retorna o valor formatado em tipo string"""

        result = str(result)
        if len(result) > 15:
            result = '{:5.5E}'.format(float(result))
            
        return result
