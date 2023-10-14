import tkinter as tk
from time import strftime

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()  # Initial call to update the time
root.mainloop()


