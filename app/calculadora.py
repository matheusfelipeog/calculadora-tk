# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtins
import sys 
import os
import platform

import tkinter as tk
from tkinter import Menu, FALSE

from functools import partial
from json import load as json_load
from json import dump as json_dump

from copy import deepcopy

# Módulos próprios
from .calculador import Calculador


class Calculadora(object):
    """Classe para criação do layout da calculadora, distribuição dos botões
    e a adição de suas funcionalidades.

    Os botões distríbuidos no layout estão conforme o exemplo abaixo:

        C | ( | ) | <
        7 | 8 | 9 | x
        4 | 5 | 6 | -
        1 | 2 | 3 | +
        . | 0 | = | /
          |   | ^ | √

        OBS: É necessário importar o modulo style contido na pacote view,
             e selecionar uma de suas classes de estilo.
    """

    def __init__(self, master):
        self.master = master
        self.calc = Calculador()

        self.settings = self._load_settings()
        
        # Define estilo padrão para macOS, caso seja o sistema operacional utilizado
        if platform.system() == 'Darwin':
            self.theme = self._get_theme('Default Theme For MacOS')
        else:
            self.theme = self._get_theme(self.settings['current_theme'])

        # Edição da Top-Level
        self.master.title('Calculadora Tk')
        self.master.maxsize(width=335, height=415)
        self.master.minsize(width=335, height=415)
        self.master.geometry('-150+100')
        self.master['bg'] = self.theme['master_bg']

        # Área do input
        self._frame_input = tk.Frame(self.master, bg=self.theme['frame_bg'], pady=4)
        self._frame_input.pack()

        # Área dos botões
        self._frame_buttons = tk.Frame(self.master, bg=self.theme['frame_bg'], padx=2)
        self._frame_buttons.pack()

        # Funções de inicialização 
        self._create_input(self._frame_input)
        self._create_buttons(self._frame_buttons)
        self._create_menu(self.master)

    @staticmethod
    def _load_settings():
        """Utilitário para carregar o arquivo de confirgurações da calculadora."""
        with open('./app/settings/settings.json', mode='r', encoding='utf-8') as f:
            settings = json_load(f)
        
        return settings

    def _get_theme(self, name='Dark'):
        """Retorna as configurações de estilo para o theme especificado."""

        list_of_themes = self.settings['themes']

        found_theme = None
        for t in list_of_themes:
            if name == t['name']:
                found_theme = deepcopy(t)
                break
        
        return found_theme
        
    def _create_input(self, master):
        self._entrada = tk.Entry(master, cnf=self.theme['INPUT'])
        self._entrada.insert(0,0)
        self._entrada.pack()

    def _create_menu(self, master):
        self.master.option_add('*tearOff', FALSE)
        calc_menu = Menu(self.master)
        self.master.config(menu=calc_menu)

        #Configuração
        config = Menu(calc_menu)
        theme = Menu(config)
        #Menu tema
        theme_incompatible = ['Default Theme For MacOS']
        for t in self.settings['themes']:

            name = t['name']
            if name in theme_incompatible:  # Ignora os temas não compatíveis.
                continue
            else:
                theme.add_command(label=name, command=partial(self._change_theme_to, name))
        #Configuração
        calc_menu.add_cascade(label='Configuração', menu=config)
        config.add_cascade(label='Tema', menu=theme)

        config.add_separator()
        config.add_command(label='Sair', command=self._exit)

    def _change_theme_to(self, name='Dark'):
        self.settings['current_theme'] = name

        with open('./app/settings/settings.json', 'w') as outfile:
            json_dump(self.settings, outfile, indent=4)

        self._realod_app()
        
    def _create_buttons(self, master):
        """"Metódo responsável pela criação de todos os botões da calculadora,
        indo desde adição de eventos em cada botão à distribuição no layout grid.
        """

        # Seta configurações globais (width, height font etc) no botão especificado.
        self.theme['BTN_NUMERICO'].update(self.settings['global'])

        self._BTN_NUM_0 = tk.Button(master, text=0, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_1 = tk.Button(master, text=1, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_2 = tk.Button(master, text=2, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_3 = tk.Button(master, text=3, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_4 = tk.Button(master, text=4, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_5 = tk.Button(master, text=5, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_6 = tk.Button(master, text=6, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_7 = tk.Button(master, text=7, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_8 = tk.Button(master, text=8, cnf=self.theme['BTN_NUMERICO'])
        self._BTN_NUM_9 = tk.Button(master, text=9, cnf=self.theme['BTN_NUMERICO'])

        # Seta configurações globais (width, height font etc) no botão especificado.
        self.theme['BTN_OPERADOR'].update(self.settings['global'])

        # Instânciação dos botões dos operadores númericos
        self._BTN_SOMA = tk.Button(master, text='+', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_SUB = tk.Button(master, text='-', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_DIV = tk.Button(master, text='/', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_MULT = tk.Button(master, text='*', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_EXP = tk.Button(master, text='^', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_RAIZ = tk.Button(master, text='√', cnf=self.theme['BTN_OPERADOR'])

        # Seta configurações globais (width, height font etc) no botão especificado.
        self.theme['BTN_DEFAULT'].update(self.settings['global'])
        self.theme['BTN_CLEAR'].update(self.settings['global'])

        # Instânciação dos botões de funcionalidades da calculadora
        self._BTN_ABRE_PARENTESE = tk.Button(master, text='(', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_FECHA_PARENTESE = tk.Button(master, text=')', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_CLEAR = tk.Button(master, text='C', cnf=self.theme['BTN_DEFAULT'])
        self._BTN_DEL = tk.Button(master, text='<', cnf=self.theme['BTN_CLEAR'])
        self._BTN_RESULT = tk.Button(master, text='=', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_DOT = tk.Button(master, text='.', cnf=self.theme['BTN_DEFAULT'])

        # Instânciação dos botões vazios, para futura implementação
        self._BTN_VAZIO1 = tk.Button(master, text='', cnf=self.theme['BTN_OPERADOR'])
        self._BTN_VAZIO2 = tk.Button(master, text='', cnf=self.theme['BTN_OPERADOR'])

        # Distribuição dos botões em um gerenciador de layout grid
        # Linha 0
        self._BTN_CLEAR.grid(row=0, column=0, padx=1, pady=1)
        self._BTN_ABRE_PARENTESE.grid(row=0, column=1, padx=1, pady=1)
        self._BTN_FECHA_PARENTESE.grid(row=0, column=2, padx=1, pady=1)
        self._BTN_DEL.grid(row=0, column=3, padx=1, pady=1)

        # Linha 1
        self._BTN_NUM_7.grid(row=1, column=0, padx=1, pady=1)
        self._BTN_NUM_8.grid(row=1, column=1, padx=1, pady=1)
        self._BTN_NUM_9.grid(row=1, column=2, padx=1, pady=1)
        self._BTN_MULT.grid(row=1, column=3, padx=1, pady=1)

        # Linha 2
        self._BTN_NUM_4.grid(row=2, column=0, padx=1, pady=1)
        self._BTN_NUM_5.grid(row=2, column=1, padx=1, pady=1)
        self._BTN_NUM_6.grid(row=2, column=2, padx=1, pady=1)
        self._BTN_SUB.grid(row=2, column=3, padx=1, pady=1)

        # Linha 3
        self._BTN_NUM_1.grid(row=3, column=0, padx=1, pady=1)
        self._BTN_NUM_2.grid(row=3, column=1, padx=1, pady=1)
        self._BTN_NUM_3.grid(row=3, column=2, padx=1, pady=1)
        self._BTN_SOMA.grid(row=3, column=3, padx=1, pady=1)

        # Linha 4
        self._BTN_DOT.grid(row=4, column=0, padx=1, pady=1)
        self._BTN_NUM_0.grid(row=4, column=1, padx=1, pady=1)
        self._BTN_RESULT.grid(row=4, column=2, padx=1, pady=1)
        self._BTN_DIV.grid(row=4, column=3, padx=1, pady=1)

        # Linha 5
        self._BTN_VAZIO1.grid(row=5, column=0, padx=1, pady=1)
        self._BTN_VAZIO2.grid(row=5, column=1, padx=1, pady=1)
        self._BTN_EXP.grid(row=5, column=2, padx=1, pady=1)
        self._BTN_RAIZ.grid(row=5, column=3, padx=1, pady=1)

        # Eventos dos botões númericos
        self._BTN_NUM_0['command'] = partial(self._set_values_in_input, 0)
        self._BTN_NUM_1['command'] = partial(self._set_values_in_input, 1)
        self._BTN_NUM_2['command'] = partial(self._set_values_in_input, 2)
        self._BTN_NUM_3['command'] = partial(self._set_values_in_input, 3)
        self._BTN_NUM_4['command'] = partial(self._set_values_in_input, 4)
        self._BTN_NUM_5['command'] = partial(self._set_values_in_input, 5)
        self._BTN_NUM_6['command'] = partial(self._set_values_in_input, 6)
        self._BTN_NUM_7['command'] = partial(self._set_values_in_input, 7)
        self._BTN_NUM_8['command'] = partial(self._set_values_in_input, 8)
        self._BTN_NUM_9['command'] = partial(self._set_values_in_input, 9)

        # Eventos dos botões de operação matemática
        self._BTN_SOMA['command'] = partial(self._set_operator_in_input, '+')
        self._BTN_SUB['command'] = partial(self._set_operator_in_input, '-')
        self._BTN_MULT['command'] = partial(self._set_operator_in_input, '*')
        self._BTN_DIV['command'] = partial(self._set_operator_in_input, '/')
        self._BTN_EXP['command'] = partial(self._set_operator_in_input, '**')
        self._BTN_RAIZ['command'] = partial(self._set_operator_in_input, '**(1/2)')


        # Eventos dos botões de funcionalidades da calculadora
        self._BTN_DOT['command'] = partial(self._set_dot_in_input, '.')
        self._BTN_ABRE_PARENTESE['command'] = self._set_open_parent
        self._BTN_FECHA_PARENTESE['command'] = self._set_close_parent
        self._BTN_DEL['command'] = self._del_last_value_in_input
        self._BTN_CLEAR['command'] = self._clear_input
        self._BTN_RESULT['command'] = self._get_data_in_input

    def _set_values_in_input(self, value):
        """Metódo responsável por captar o valor númerico clicado e setar no input"""
        if self._entrada.get() == 'Erro':
            self._entrada.delete(0, len(self._entrada.get()))

        if self._entrada.get() == '0':
            self._entrada.delete(0)
            self._entrada.insert(0 ,value)
        elif self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,value)
    
    def _set_dot_in_input(self, dot):
        """Metódo responsável por setar o ponto de separação decimal no valor"""
        if self._entrada.get() == 'Erro':
            return 

        if self._entrada.get()[-1] not in '.+-/*' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,dot)

    def _set_open_parent(self):
        """Metódo para setar a abertura de parenteses no input"""
        if self._entrada.get() == 'Erro':
            return 

        if self._entrada.get() == '0':
            self._entrada.delete(0)
            self._entrada.insert(len(self._entrada.get()), '(')
        elif self._entrada.get()[-1] in '+-/*' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()), '(')
    
    def _set_close_parent(self):
        """Metódo para setar o fechamento de parenteses no input"""
        if self._entrada.get() == 'Erro':
            return

        if self._entrada.get().count('(') <= self._entrada.get().count(')'):
            return
        if self._entrada.get()[-1] not in '+-/*(' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()), ')')

    def _clear_input(self):
        """Reseta o input da calculadora, limpando-o por completo e inserindo o valor 0"""
        self._entrada.delete(0, len(self._entrada.get()))
        self._entrada.insert(0,0)
    
    def _del_last_value_in_input(self):
        """Apaga o último digito contido dentro do input"""
        if self._entrada.get() == 'Erro':
            return

        if len(self._entrada.get()) == 1:
            self._entrada.delete(0)
            self._entrada.insert(0,0)
        else:
            self._entrada.delete(len(self._entrada.get()) - 1)
    
    def _set_operator_in_input(self, operator):
        """Metódo responsável por captar o operador matemático clicado e setar no input"""
        if self._entrada.get() == 'Erro':
            return

        if self._entrada.get() == '':
            # print('\33[91mOperação inválida.\33[m')
            return
        # Evita casos de operadores repetidos sequêncialmente, para evitar erros
        if self._entrada.get()[-1] not in '+-*/' and self._lenght_max(self._entrada.get()):
            self._entrada.insert(len(self._entrada.get()) ,operator)
            
    def _get_data_in_input(self):
        """Pega os dados com todas as operações contidos dentro do input
        para realizar o calculo"""
        if self._entrada.get() == 'Erro':
            return

        result = self.calc.calculation(self._entrada.get())
        self._set_result_in_input(result=result)

    def _set_result_in_input(self, result=0):
        """Seta o resultado de toda a operação dentro do input"""
        if self._entrada.get() == 'Erro':
            return

        self._entrada.delete(0, len(self._entrada.get()))
        self._entrada.insert(0, result)

    def _lenght_max(self, data_in_input):
        """Para verificar se o input atingiu a quantidade de caracteres máxima"""
        if len(str(data_in_input)) >= 15:
            return False
        return True
            
    def start(self):
        print('\33[92mCalculadora Tk Iniciada. . .\33[m\n')
        self.master.mainloop()
    
    def _realod_app(self):
        """Reinicia o aplicativo."""
        python = sys.executable  # Recupera o path do executável do python
        os.execl(python, python, * sys.argv)

    def _exit(self):
        exit()
