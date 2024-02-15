# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtin
import tkinter as tk

# Módulo próprio
from app.calculadora import Calculadora

if __name__ == '__main__':
    master = tk.Tk()
    master.iconbitmap("resources/calculator_ico.ico")
    main = Calculadora(master)
    main.start()
