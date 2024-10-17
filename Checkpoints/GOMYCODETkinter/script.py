import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and display the result."""
    fahrenheit = float(ent_temperature.get())
    celsius = (fahrenheit - 32) * 5 / 9
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create a frame for the entry widget and the label
frm_entry = tk.Frame(master=window)

# Entry widget to accept temperature in Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)
ent_temperature.grid(row=0, column=0, sticky="e")

# Label to display Fahrenheit symbol
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
lbl_temp.grid(row=0, column=1, sticky="w")

# Layout the frame in the window
frm_entry.grid(row=0, column=0, padx=10)

# Button to trigger the conversion
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
btn_convert.grid(row=0, column=1, pady=10)

# Label to display the result in Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_result.grid(row=0, column=2, padx=10)

# Start the application
window.mainloop()
