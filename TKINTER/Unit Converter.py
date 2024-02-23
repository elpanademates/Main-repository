import tkinter as tk
from tkinter import ttk

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
    dropdown2_text = dropdown2.get()
    entry = var.get()

    if dropdown_text == "Miles" and dropdown2_text == "Kilometers":
        label = tk.Label(WIN, text=f"Answer: {entry * m_km}", font=("Arial", 15))
        label.pack(pady=5)

    elif dropdown_text == "Kilometers" and dropdown2_text == "Miles":
        label2 = tk.Label(WIN, text=f"Answer: {entry / m_km}", font=("Arial", 15))
        label2.pack(pady=5)

    elif dropdown_text == "Pounds" and dropdown2_text == "Kilograms":
        label3 = tk.Label(WIN, text=f"Answer: {entry / p_kg}", font=("Arial", 15))
        label3.pack(pady=5)

    elif dropdown_text == "Kilograms" and dropdown2_text == "Pounds":
        label4 = tk.Label(WIN, text=f"Answer: {entry * p_kg}", font=("Arial", 15))
        label4.pack(pady=5)

    elif dropdown_text == "Feet" and dropdown2_text == "Meters":
        label5 = tk.Label(WIN, text=f"Answer: {entry * ft_m}", font=("Arial", 15))
        label5.pack(pady=5)

    elif dropdown_text == "Meters" and dropdown2_text == "Feet":
        label6 = tk.Label(WIN, text=f"Answer: {entry / ft_m}", font=("Arial", 15))
        label6.pack(pady=5)

    elif dropdown_text == "Celsius" and dropdown2_text == "Fahrenheit":
        label7 = tk.Label(WIN, text=f"Answer: {(entry * 9/5) + cel_fah}", font=("Arial", 15))
        label7.pack(pady=5)

    elif dropdown_text == "Fahrenheit" and dropdown2_text == "Celsius":
        label8 = tk.Label(WIN, text=f"Answer: {(entry -32) * fah_cel}", font=("Arial", 15))
        label8.pack(pady=5)

    else:
        label9 = tk.Label(WIN, text="Value Error!", font=("Arial", 20))
        label9.pack(pady=5)

    
options = ["Miles", "Kilometers", "Kilograms", "Pounds", "Feet", "Meters", "Celsius", "Fahrenheit"]
menu = ttk.Combobox(WIN, values=options)
menu.place(x=20, y=120, width=80)

dropdown2 = ttk.Combobox(WIN, values=options)
dropdown2.place(x=165, y=120, width=80)

dropdown_text = menu.get
dropdown2_text = dropdown2.get

button = tk.Button(WIN, text="Show Answer", command=check)
button.place(x=100, y=170)

var = tk.IntVar()
entry = tk.Entry(WIN, textvariable=var, width=15)
entry.place(x=70, y=70)


WIN.mainloop()