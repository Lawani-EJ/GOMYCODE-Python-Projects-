# Temprature converter 
# Author: [Lawani Elyon John]
# Date: [10/14/2024]

# Three elements are needed 
# 1. The temperature value to be converted
# 2. The unit of the temperature value to be converted (Celsius or Fahrenheit)
# 3. The unit to which the temperature value is to be converted (Celsius or Fahrenheit

import tkinter as tk

# Function to convert Fahrenheit to Celsius
def perform_fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        lbl_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        lbl_result.config(text="Invalid Input")


window = tk.Tk()
window.title("A Temperature Converter")
window.resizable(False, False)


frame_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frame_entry, width=10)
lbl_temp = tk.Label(master=frame_entry, text="°F")


ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
frame_entry.grid(row=0, column=0, padx=10, pady=10)


btn_convert = tk.Button(
    master=window,
    text="→",
    command=perform_fahrenheit_to_celsius
)
btn_convert.grid(row=0, column=1, padx=10, pady=10)


lbl_result = tk.Label(master=window, text="°C")
lbl_result.grid(row=0, column=2, padx=10, pady=10)


window.mainloop()
