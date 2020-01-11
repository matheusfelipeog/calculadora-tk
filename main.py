# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtin
import tkinter as tk

# Módulo próprio
from app.calculadora import Calculadora

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    main.start()
