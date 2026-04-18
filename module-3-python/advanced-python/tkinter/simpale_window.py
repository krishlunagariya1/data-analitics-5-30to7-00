import tkinter as tk
# create a main window
root = tk.Tk()
# create a windows title
root.title("simple a windows desktop app")
# create a windows size
root.geometry("350x300")
# create a label widget
label = tk.Label(root,text="hello i am Krish", font=("Arial", 19))
#set a position with border and content and provides padding top to bottom
label.pack(pady=25)

# add colour in hello i am krish
label.config(fg="Blue", bg="Yellow")



# print a windows
root.mainloop()
