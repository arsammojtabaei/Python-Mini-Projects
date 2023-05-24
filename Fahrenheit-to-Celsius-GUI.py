import tkinter as tk
from tkinter import ttk
window = tk.Tk()

fahrenheit_val = tk.StringVar()

lbl_result = ttk.Label(
    window,
    text='Enter Your Number...',
    font=('times', 12)
)

def convert_fahrenheit_to_celsius(*args):
    fahrenheit_input = fahrenheit_val.get()
    try:
        fahrenheit_value = float(fahrenheit_input)
        lbl_result['text'] = (fahrenheit_value - 32)* 5/9

    except ValueError:
        if fahrenheit_input != '':
            lbl_result['text'] = 'You should enter a number'
        else:
            lbl_result['text'] = 'Your input is empty'

window.bind('<Return>', convert_fahrenheit_to_celsius)
lbl_fahrenheit = ttk.Label(
    window,
    text='Fahrenheit',
    font=('times', 12)
)

ent_fahrenheit = ttk.Entry(
    window,
    width=50,
    textvariable=fahrenheit_val,
)

btn_calc = ttk.Button(
    window,
    text='Calc',
    command=convert_fahrenheit_to_celsius,
)

lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

lbl_celsius = ttk.Label(
    window,
    text='Celsius',
    font=('times', 12)
)


lbl_celsius.grid(row=1, column=0,pady=(10, 20))
lbl_result.grid(row=1, column=1,pady=(10, 20))


window.title('Fahrenheit To Celsius App')
window.mainloop()