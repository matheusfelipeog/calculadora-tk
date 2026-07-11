# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

import ast
from platform import node

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
            # WARNING: The security vulnerability is right here!
            # result = eval(calc)

            #Uses ast to turn the string into a traversable tree
            tree = ast.parse(calc, mode='eval')

            #Pass the tree to the helper function I setup to read the tree and return a result
            result = self.input_check(tree.body)

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

    """Recursively checks the AST nodes to ensure that only safe operations are performed."""
    def input_check(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left_val = self.input_check(node.left)
            right_val = self.input_check(node.right)

            # Check for the operator and return the value
            if isinstance(node.op, ast.Add):
                return left_val + right_val
            elif isinstance(node.op, ast.Sub):
                return left_val - right_val
            elif isinstance(node.op, ast.Mult):
                return left_val * right_val
            elif isinstance(node.op, ast.Div):
                return left_val / right_val
            elif isinstance(node.op, ast.Pow):
                return left_val ** right_val
            else:
                raise ValueError("Unsupported binary operator")
        elif isinstance(node, ast.UnaryOp):
            operand_val = self.input_check(node.operand)

            if isinstance(node.op, ast.USub):
                return -operand_val
            elif isinstance(node.op, ast.UAdd):
                return +operand_val
            else:
                raise ValueError("Unsupported unary operator")
        else:
            # Security shield triggers if it's an ast.Call or anything else
            raise ValueError("Unsafe code element detected!")
