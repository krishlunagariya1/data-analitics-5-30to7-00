import tkinter as tk
import tkinter.messagebox as messagebox

# Function to calculate addition
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        result = num1 + num2
        
        messagebox.showinfo("Result", f"Addition = {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Addition App")
root.geometry("350x300")

# Label
label = tk.Label(root, text="Enter two numbers:", font=("Arial", 16))
label.pack(pady=10)

# Input fields
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=10)

# Button
button = tk.Button(root, text="Add", font=("Arial", 14), command=add_numbers)
button.pack(pady=20)

# Run app
root.mainloop()