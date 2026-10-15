# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

import re


class Calculador(object):
    """Classe responsável por realizar todos os calculos da calculadora"""

    def calculation(self, calc):
        """Responsável por receber o calculo a ser realizado, retornando
        o resultado ou uma mensagem de erro em caso de falha.
        """
        return self.__calculation_validation(calc=calc)

    def __calculation_validation(self, calc):
        """Responsável por verificar se o calculo informado é possível ser feito"""

        # Обработка процента с учётом контекста
        calc = self.__apply_percent(calc)

        try:
            result = eval(calc)
            return self.__format_result(result=result)
        except (NameError, ZeroDivisionError, SyntaxError, ValueError, TypeError):
            return 'Erro'

    @staticmethod
    def __apply_percent(calc):
        """Преобразует запись с процентом в корректное математическое выражение.

        Правила:
            100 + 5%  ->  100 + (100 * 5 / 100)   = 105
            100 - 5%  ->  100 - (100 * 5 / 100)   = 95
            100 * 5%  ->  100 * (5 / 100)         = 5
            100 / 5%  ->  100 / (5 / 100)         = 2000
            50%       ->  50 / 100                = 0.5

        Поддерживаются цепочки: 100 + 10% - 5% + 20%
        """
        # Шаблон: <левое_число> <оператор> <правое_число>%
        # Ищем "A op B%" и заменяем на "A op (A*B/100)" для + и -,
        # а для * и / — на "A op (B/100)".
        pattern = re.compile(
            r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)%'
        )

        def replace(match):
            left = match.group(1)
            op = match.group(2)
            right = match.group(3)

            if op in ('+', '-'):
                # Процент от левого числа
                return '{left} {op} ({left}*{right}/100)'.format(
                    left=left, op=op, right=right
                )
            else:
                # Для умножения и деления — просто делим на 100
                return '{left} {op} ({right}/100)'.format(
                    left=left, op=op, right=right
                )

        # Применяем замену в цикле, чтобы обработать цепочки вида "100 + 10% + 5%"
        prev = None
        while prev != calc:
            prev = calc
            calc = pattern.sub(replace, calc)

        # Оставшиеся одиночные проценты (например, "50%" в начале)
        # превращаем в "(50/100)"
        calc = re.sub(r'(\d+(?:\.\d+)?)%', r'(\1/100)', calc)

        return calc

    def __format_result(self, result):
        """Formata o resultado em notação cientifica caso seja muito grande
        e retorna o valor formatado em tipo string"""

        result = str(result)
        if len(result) > 15:
            result = '{:5.5E}'.format(float(result))

        return result