import tkinter as tk
#pass a massage in windows
import tkinter.messagebox as messagebox
#create a function for user input
def input_user():
    user_input = entry.get()
    #messagebox.showinfo("Input Received", f"Your name is: {user_input}")
    # pass a massage in windows
    return messagebox.showinfo("User Input :",f"hello, {user_input}")
# create a main window
root = tk.Tk()
# create a windows title
root.title("simple a windows desktop app")
# create a windows size
root.geometry("350x300")

#create a lable 
lable = tk.Label(root,text="Enter your name: ", font=("Arial", 17))
#create a input
entry = tk.Entry(root, font=("Arial", 17))
entry.pack(pady=20)

#create a padding in lable
lable.pack(pady=20)

#create a button widget
button = tk.Button(root, text="Submit", command= input_user)
button.pack(pady=20)




root.mainloop()
