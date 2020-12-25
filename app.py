import tkinter as tk
from tkinter import ttk 
import requests
import awesometkinter as atk

url =

def call_weather():

app = tk.Tk()

styles = ttk.Style()
styles.theme_use("alt")

f1 = atk.Frame3d(app)
f1.pack(side="left", expand=True, fill="both", padx=3, pady=3)

weather_city = tk.Entry()
search = atk.Button3d(app, command=call_weather())
search.pack()

app.mainloop()
