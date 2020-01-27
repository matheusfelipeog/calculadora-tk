# -*- coding: utf-8 -*-

class Dark(object):
    def __init__(self):
        self.master_bg = '#252729'
        self.frame_bg = '#252729'

        self.INPUT = {
            'bg': '#252729',
            'fg': 'white',
            'borderwidth': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'bg': '#050505',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#0097e6',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#d63031',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

class DefaultStyleForMacOS(object):
    """Classe criada para ambientes macOS para corrigir bug de estilo."""
    def __init__(self):
        self.master_bg = ''
        self.frame_bg = ''

        self.INPUT = {
            'borderwidth': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'activeforeground': 'light blue',
            'borderwidth': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'activeforeground': 'light blue',
            'borderwidth': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'activeforeground': 'light blue',
            'borderwidth': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'activeforeground': 'light blue',
            'borderwidth': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }
        