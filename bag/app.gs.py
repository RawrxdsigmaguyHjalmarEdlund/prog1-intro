import tkinter

item = []
max=10
main = tkinter.Tk()
def open_popup():
   top= tkinter.Toplevel(main)
   top.geometry("200x200")
   top.title("Child Window")
   top.configure(bg='black') 
   tkinter.Label(top, bg='black', fg='red', text= "Påsen är full med max 10 saker (T_T)",).place(x=0,y=0)
main.geometry("800x600")
main.configure(bg='gray28') 

label = tkinter.Label(main, text="Välkommen till påsen")
label.pack(pady=20)
label.configure(bg='gray28') 
text_box = tkinter.Text(main, fg='green2', height=10)
text_box.pack()
text_box.configure(bg='black') 
input_text = tkinter.Entry(main, fg='green2')
input_text.pack(pady=20)
input_text.configure(bg='black')
def add_to_bag(event=None):
    if len(item) >= max:
        open_popup()
    else:
        value = input_text.get().strip()
        if not value:
            return
        item.append(value)
        input_text.delete(0, tkinter.END)
        text_box.delete("1.0", tkinter.END)
        text_box.insert(tkinter.END, "\n".join(item) + "\n")
input_text.bind("<Return>", add_to_bag)
add_button = tkinter.Button(main, text="Spara i påsen", command=add_to_bag)
add_button.pack(pady=20)
quit_button = tkinter.Button(main, text = "Avsluta", command=quit)
quit_button.pack(pady = 20)

main.mainloop()