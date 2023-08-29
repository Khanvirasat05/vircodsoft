import tkinter as tk


def update_display(value):
    current = display_var.get()
    display_var.set(current + str(value))


def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")


def clear():
    display_var.set("")


vir = tk.Tk()
vir.title("Calculator")


display_var = tk.StringVar()


display = tk.Entry(vir, textvariable=display_var, font=("Helvetica", 20), justify="right")
display.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(vir, text=button, padx=20, pady=20, font=("Helvetica", 15),
              command=lambda b=button: update_display(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


tk.Button(vir, text="C", padx=20, pady=20, font=("Helvetica", 15), command=clear).grid(row=row_val, column=col_val)


vir.mainloop()