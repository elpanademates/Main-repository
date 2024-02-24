import tkinter as tk
from tkinter import ttk
#from time import sleep as slp

m_km = 1.609344
p_kg = 2.20462
ft_m = 0.3048
cel_fah = 32
fah_cel = 5/9

WIN = tk.Tk()
WIN.title("Unit Converter")
WIN.geometry("300x200")




def check():
    dropdown_text = menu.get()
    dropdown2_text = menu2.get()
    entry = var.get()

    global label

    label = tk.Label(WIN, text=f"Answer: {entry}", font=("Arial", 15))

    if dropdown_text == "Miles" and dropdown2_text == "Kilometers":
        label = tk.Label(WIN, text=f"Answer: {entry * m_km}", font=("Arial", 15))
        label.pack(pady=5)

    elif dropdown_text == "Kilometers" and dropdown2_text == "Miles":
        label.config(text=f"Answer: {entry / m_km}",)
        label.pack(pady=5)

    elif dropdown_text == "Pounds" and dropdown2_text == "Kilograms":
        label.config(text=f"Answer: {entry / p_kg}")
        label.pack(pady=5)

    elif dropdown_text == "Kilograms" and dropdown2_text == "Pounds":
        label.config(text=f"Answer: {entry * p_kg}")
        label.pack(pady=5)

    elif dropdown_text == "Feet" and dropdown2_text == "Meters":
        label.config(text=f"Answer: {entry * ft_m}")
        label.pack(pady=5)

    elif dropdown_text == "Meters" and dropdown2_text == "Feet":
        label.config(text=f"Answer: {entry / ft_m}")
        label.pack(pady=5)

    elif dropdown_text == "Celsius" and dropdown2_text == "Fahrenheit":
        label.config(text=f"Answer: {(entry * 9/5) + cel_fah}")
        label.pack(pady=5)

    elif dropdown_text == "Fahrenheit" and dropdown2_text == "Celsius":
        label.config(text=f"Answer: {(entry -32) * fah_cel}")
        label.pack(pady=5)

    else:
        label.config(text="Value Error!", font=("Arial", 30))
        label.pack(pady=5)


def continue_button_click():
    label.destroy()
    continue_button.place_forget()

def place_continue_button():
    continue_button.place(x=20, y=165)

options = ["Miles", "Kilometers", "Kilograms", "Pounds", "Feet", "Meters", "Celsius", "Fahrenheit"]
menu = ttk.Combobox(WIN, values=options)
menu.place(x=20, y=120, width=80)

menu2 = ttk.Combobox(WIN, values=options)
menu2.place(x=165, y=120, width=80)

dropdown_text = menu.get
dropdown2_text = menu2.get

button = tk.Button(WIN, text="Show Answer", command=lambda: (check(), place_continue_button()))
button.place(x=100, y=170)

var = tk.IntVar()
entry = tk.Entry(WIN, textvariable=var, width=15)
entry.place(x=70, y=70)

continue_button = tk.Button(WIN, text="Continue", command=continue_button_click)


if __name__ == "__main__":
    WIN.mainloop()