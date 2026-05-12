import tkinter as tk

def calculate(operation):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())

        if operation == "+":
            result = n1 + n2

        elif operation == "-":
            result = n1 - n2

        elif operation == "*":
            result = n1 * n2

        elif operation == "/":
            if n2 == 0:
                output.config(text="Cannot divide by zero")
                return
            result = n1 / n2

        elif operation == "^":
            result = n1 ** n2

        output.config(text=f"Result: {result}")

    except:
        output.config(text="Invalid input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    output.config(text="Result will appear here")

window = tk.Tk()
window.title("GUI Calculator")
window.geometry("300x250")

tk.Label(window, text="First Number").pack(pady=5)

entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Second Number").pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Add", width=15,
command=lambda: calculate("+")).pack(pady=5)

tk.Button(window, text="Subtract", width=15,
command=lambda: calculate("-")).pack(pady=5)

tk.Button(window, text="Multiply", width=15,
command=lambda: calculate("*")).pack(pady=5)

tk.Button(window, text="Divide", width=15,
command=lambda: calculate("/")).pack(pady=5)

tk.Button(window, text="Power", width=15,
command=lambda: calculate("^")).pack(pady=5)

tk.Button(window, text="Clear", width=15,
command=clear).pack(pady=5)

output = tk.Label(
    window,
    text="Result will appear here",
    font=("Arial", 12)
)

output.pack(pady=10)

# Run App
window.mainloop()
