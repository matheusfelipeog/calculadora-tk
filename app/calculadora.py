# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: githuc.com/matheusfelipeog

# Builtins
import tkinter as tk
from functools import partial

# Módulos próprios
from app.calculador import Calculador
import app.style as style


class Calculadora(object):
    """Classe para criação do layout da calculadora, distribuição dos botões
    e a adição de suas funcionalidades.

    Os botões distríbuidos no layout estão conforme o exemplo abaixo:

        C | ( | ) | <
        7 | 8 | 9 | x
        4 | 5 | 6 | -
        1 | 2 | 3 | +
        . | 0 | = | /

        OBS: É necessário importar o modulo style contido na pacote view,
             e selecionar uma de suas classes de estilo.
    """

    def __init__(self, master):
        self.master = master
        self.calc = Calculador()
        self.style = style.Dark()

        # Edição da Top-Level
        self.master.title('Calculadora Tk')
        self.master.maxsize(width=335, height=355)
        self.master.minsize(width=335, height=355)
        self.master.geometry('-150+100')
        self.master['bg'] = '#252729'

        # Área do input
        self.__frame_input = tk.Frame(self.master, bg='#252729', pady=4)
        self.__frame_input.pack()

        # Área dos botões
        self.__frame_buttons = tk.Frame(self.master, bg='#252729', padx=2)
        self.__frame_buttons.pack()

        # Funções de inicialização 
        self.__create_input(self.__frame_input)
        self.__create_buttons(self.__frame_buttons)

    def __create_input(self, master):
        self.__entrada = tk.Entry(master, cnf=self.style.INPUT)
        self.__entrada.insert(0,0)
        self.__entrada.pack()

    def __create_buttons(self, master):
        """"Metódo responsável pela criação de todos os botões da calculadora,
        indo desde adição de eventos em cada botão à distribuição no layout grid.
        """
        self.__BTN_NUM_0 = tk.Button(master, text=0, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_1 = tk.Button(master, text=1, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_2 = tk.Button(master, text=2, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_3 = tk.Button(master, text=3, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_4 = tk.Button(master, text=4, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_5 = tk.Button(master, text=5, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_6 = tk.Button(master, text=6, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_7 = tk.Button(master, text=7, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_8 = tk.Button(master, text=8, cnf=self.style.BTN_NUMERICO)
        self.__BTN_NUM_9 = tk.Button(master, text=9, cnf=self.style.BTN_NUMERICO)

        # Instânciação dos botões dos operadores númericos
        self.__BTN_SOMA = tk.Button(master, text='+', cnf=self.style.BTN_OPERADOR)
        self.__BTN_SUB = tk.Button(master, text='-', cnf=self.style.BTN_OPERADOR)
        self.__BTN_DIV = tk.Button(master, text='/', cnf=self.style.BTN_OPERADOR)
        self.__BTN_MULT = tk.Button(master, text='*', cnf=self.style.BTN_OPERADOR)

        # Instânciação dos botões de funcionalidades da calculadora
        self.__BTN_ABRE_PARENTESE = tk.Button(master, text='(', cnf=self.style.BTN_DEFAULT)
        self.__BTN_FECHA_PARENTESE = tk.Button(master, text=')', cnf=self.style.BTN_DEFAULT)
        self.__BTN_CLEAR = tk.Button(master, text='C', cnf=self.style.BTN_DEFAULT)
        self.__BTN_DEL = tk.Button(master, text='<', cnf=self.style.BTN_CLEAR)
        self.__BTN_RESULT = tk.Button(master, text='=', cnf=self.style.BTN_OPERADOR)
        self.__BTN_DOT = tk.Button(master, text='.', cnf=self.style.BTN_DEFAULT)

        # Distribuição dos botões em um gerenciador de layout grid
        # Linha 0
        self.__BTN_CLEAR.grid(row=0, column=0, padx=1, pady=1)
        self.__BTN_ABRE_PARENTESE.grid(row=0, column=1, padx=1, pady=1)
        self.__BTN_FECHA_PARENTESE.grid(row=0, column=2, padx=1, pady=1)
        self.__BTN_DEL.grid(row=0, column=3, padx=1, pady=1)

        # Linha 1
        self.__BTN_NUM_7.grid(row=1, column=0, padx=1, pady=1)
        self.__BTN_NUM_8.grid(row=1, column=1, padx=1, pady=1)
        self.__BTN_NUM_9.grid(row=1, column=2, padx=1, pady=1)
        self.__BTN_MULT.grid(row=1, column=3, padx=1, pady=1)

        # Linha 2
        self.__BTN_NUM_4.grid(row=2, column=0, padx=1, pady=1)
        self.__BTN_NUM_5.grid(row=2, column=1, padx=1, pady=1)
        self.__BTN_NUM_6.grid(row=2, column=2, padx=1, pady=1)
        self.__BTN_SUB.grid(row=2, column=3, padx=1, pady=1)

        # Linha 3
        self.__BTN_NUM_1.grid(row=3, column=0, padx=1, pady=1)
        self.__BTN_NUM_2.grid(row=3, column=1, padx=1, pady=1)
        self.__BTN_NUM_3.grid(row=3, column=2, padx=1, pady=1)
        self.__BTN_SOMA.grid(row=3, column=3, padx=1, pady=1)

        # Linha 4
        self.__BTN_DOT.grid(row=4, column=0, padx=1, pady=1)
        self.__BTN_NUM_0.grid(row=4, column=1, padx=1, pady=1)
        self.__BTN_RESULT.grid(row=4, column=2, padx=1, pady=1)
        self.__BTN_DIV.grid(row=4, column=3, padx=1, pady=1)

        # Eventos dos botões númericos
        self.__BTN_NUM_0['command'] = partial(self.__set_values_in_input, 0)
        self.__BTN_NUM_1['command'] = partial(self.__set_values_in_input, 1)
        self.__BTN_NUM_2['command'] = partial(self.__set_values_in_input, 2)
        self.__BTN_NUM_3['command'] = partial(self.__set_values_in_input, 3)
        self.__BTN_NUM_4['command'] = partial(self.__set_values_in_input, 4)
        self.__BTN_NUM_5['command'] = partial(self.__set_values_in_input, 5)
        self.__BTN_NUM_6['command'] = partial(self.__set_values_in_input, 6)
        self.__BTN_NUM_7['command'] = partial(self.__set_values_in_input, 7)
        self.__BTN_NUM_8['command'] = partial(self.__set_values_in_input, 8)
        self.__BTN_NUM_9['command'] = partial(self.__set_values_in_input, 9)

        # Eventos dos botões de operação matemática
        self.__BTN_SOMA['command'] = partial(self.__set_operator_in_input, '+')
        self.__BTN_SUB['command'] = partial(self.__set_operator_in_input, '-')
        self.__BTN_MULT['command'] = partial(self.__set_operator_in_input, '*')
        self.__BTN_DIV['command'] = partial(self.__set_operator_in_input, '/')

        # Eventos dos botões de funcionalidades da calculadora
        self.__BTN_DOT['command'] = partial(self.__set_dot_in_input, '.')
        self.__BTN_ABRE_PARENTESE['command'] = self.__set_open_parent
        self.__BTN_FECHA_PARENTESE['command'] = self.__set_close_parent
        self.__BTN_DEL['command'] = self.__del_last_value_in_input
        self.__BTN_CLEAR['command'] = self.__clear_input
        self.__BTN_RESULT['command'] = self.__get_data_in_input

    def __set_values_in_input(self, value):
        """Metódo responsável por captar o valor númerico clicado e setar no input"""
        if self.__entrada.get() == 'Erro':
            self.__entrada.delete(0, len(self.__entrada.get()))

        if self.__entrada.get() == '0':
            self.__entrada.delete(0)
            self.__entrada.insert(0 ,value)
        elif self.__lenght_max(self.__entrada.get()):
            self.__entrada.insert(len(self.__entrada.get()) ,value)
    
    def __set_dot_in_input(self, dot):
        """Metódo responsável por setar o ponto de separação decimal no valor"""
        if self.__entrada.get() == 'Erro':
            return 

        if self.__entrada.get()[-1] not in '.+-/*' and self.__lenght_max(self.__entrada.get()):
            self.__entrada.insert(len(self.__entrada.get()) ,dot)

    def __set_open_parent(self):
        """Metódo para setar a abertura de parenteses no input"""
        if self.__entrada.get() == 'Erro':
            return 

        if self.__entrada.get() == '0':
            self.__entrada.delete(0)
            self.__entrada.insert(len(self.__entrada.get()), '(')
        elif self.__entrada.get()[-1] in '+-/*' and self.__lenght_max(self.__entrada.get()):
            self.__entrada.insert(len(self.__entrada.get()), '(')
    
    def __set_close_parent(self):
        """Metódo para setar o fechamento de parenteses no input"""
        if self.__entrada.get() == 'Erro':
            return

        if self.__entrada.get().count('(') <= self.__entrada.get().count(')'):
            return
        if self.__entrada.get()[-1] not in '+-/*(' and self.__lenght_max(self.__entrada.get()):
            self.__entrada.insert(len(self.__entrada.get()), ')')

    def __clear_input(self):
        """Reseta o input da calculadora, limpando-o por completo e inserindo o valor 0"""
        self.__entrada.delete(0, len(self.__entrada.get()))
        self.__entrada.insert(0,0)
    
    def __del_last_value_in_input(self):
        """Apaga o último digito contido dentro do input"""
        if self.__entrada.get() == 'Erro':
            return

        if len(self.__entrada.get()) == 1:
            self.__entrada.delete(0)
            self.__entrada.insert(0,0)
        else:
            self.__entrada.delete(len(self.__entrada.get()) - 1)
    
    def __set_operator_in_input(self, operator):
        """Metódo responsável por captar o operador matemático clicado e setar no input"""
        if self.__entrada.get() == 'Erro':
            return

        if self.__entrada.get() == '':
            # print('\33[91mOperação inválida.\33[m')
            return
        # Evita casos de operadores repetidos sequêncialmente, para evitar erros
        if self.__entrada.get()[-1] not in '+-*/' and self.__lenght_max(self.__entrada.get()):
            self.__entrada.insert(len(self.__entrada.get()) ,operator)
            
    def __get_data_in_input(self):
        """Pega os dados com todas as operações contidos dentro do input
        para realizar o calculo"""
        if self.__entrada.get() == 'Erro':
            return

        result = self.calc.calculation(self.__entrada.get())
        self.__set_result_in_input(result=result)

    def __set_result_in_input(self, result=0):
        """Seta o resultado de toda a operação dentro do input"""
        if self.__entrada.get() == 'Erro':
            return

        self.__entrada.delete(0, len(self.__entrada.get()))
        self.__entrada.insert(0, result)

    def __lenght_max(self, data_in_input):
        """Para verificar se o input atingiu a quantidade de caracteres máxima"""
        if len(str(data_in_input)) > 15:
            return False
        return True
            
    def start(self):
        print('\33[92mCalculadora Tk Iniciada. . .\33[m\n')
        self.master.mainloop()
