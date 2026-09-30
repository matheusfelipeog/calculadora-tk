# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

import ast
import math


class Calculador(object):
    """Classe responsável por realizar todos os calculos da calculadora"""

    _functions = {
        'sin': lambda value: math.sin(math.radians(value)),
        'cos': lambda value: math.cos(math.radians(value)),
        'sqrt': math.sqrt,
        'log': math.log10,
        'ln': math.log,
        'factorial': math.factorial,
    }
    _constants = {'pi': math.pi, 'e': math.e}
    _operators = {
        ast.Add: lambda left, right: left + right,
        ast.Sub: lambda left, right: left - right,
        ast.Mult: lambda left, right: left * right,
        ast.Div: lambda left, right: left / right,
        ast.Pow: lambda left, right: left ** right,
    }
    
    def calculation(self, calc):
        """Responsável por receber o calculo a ser realizado, retornando
        o resultado ou uma mensagem de erro em caso de falha.

        """
        return self.__calculation_validation(calc=calc)

    def __calculation_validation(self, calc):
        """Responsável por verificar se o calculo informado é possível ser feito"""

        try:
            expression = ast.parse(calc, mode='eval')
            result = self.__evaluate(expression.body)
            return self.__format_result(result=result)
        except (ArithmeticError, OverflowError, SyntaxError, TypeError, ValueError):
            return 'Erro' 

    def __evaluate(self, node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.Name) and node.id in self._constants:
            return self._constants[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in self._operators:
            left = self.__evaluate(node.left)
            right = self.__evaluate(node.right)
            return self._operators[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = self.__evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in self._functions and len(node.args) == 1
                and not node.keywords):
            return self._functions[node.func.id](self.__evaluate(node.args[0]))
        raise ValueError('Expressão não permitida')

    def __format_result(self, result):
        """Formata o resultado em notação cientifica caso seja muito grande
        e retorna o valor formatado em tipo string"""

        result = str(result)
        if len(result) > 15:
            result = '{:.8E}'.format(float(result))
            
        return result
