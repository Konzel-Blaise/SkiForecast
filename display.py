#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 21:05:57 2025
@author: blazer
This code recieves data from Weather_main.py and displays it in a GUI
"""

##- testing GUI presenting

import tkinter as tk
from tkinter import ttk
import pandas as pd

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

def display_text(df):
    # # intialize window
    root = tk.Tk()
    root.title("Too Snowy to Work")
    # treeview
    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    # columns
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")  # control width and alignment
    # rows
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack(expand=True, fill="both")

    root.mainloop()

