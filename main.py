import customtkinter as ctk
from PIL import Image
import functions
app = ctk.CTk()
app.geometry("810x484")
app.resizable(False, False)

x =ctk.CTkEntry(app, placeholder_text="x:")
k =ctk.CTkEntry(app, placeholder_text="k:")
b =ctk.CTkEntry(app, placeholder_text="b:")
n =ctk.CTkEntry(app, placeholder_text="n:")

def combobox_callback(choice):
    if choice == "y=kx+b":

        x.place_forget()
        n.place_forget()
        b.place_forget()
        k.place_forget()
        submit_b.place_forget()
        
        x.delete(0, 'end')
        k.delete(0, 'end')
        b.delete(0, 'end')
        n.delete(0, 'end')
        
        x.insert(0, 'x:')
        k.insert(0, 'k:')
        b.insert(0, 'b:')
        n.insert(0, 'n:')

        x.place(relx=0.821, rely=0.175)
        
        k.place(relx=0.821, rely=0.250)
        
        b.place(relx=0.821, rely=0.325)
        
        submit_b.place(relx=0.821, rely=0.400)
    elif choice == "y=x^n":
        x.place_forget()
        n.place_forget()
        b.place_forget()
        k.place_forget()
        
        x.delete(0, 'end')
        k.delete(0, 'end')
        b.delete(0, 'end')
        n.delete(0, 'end')
        
        x.insert(0, 'x:')
        n.insert(0, 'n:')
        
        submit_b.place_forget()
        
        x.place(relx=0.821, rely=0.175)
        
        n.place(relx=0.821, rely=0.250)
        
        submit_b.place(relx=0.821, rely=0.325)
    else:
        x.place_forget()
        n.place_forget()
        b.place_forget()
        submit_b.place_forget()

options = ctk.CTkComboBox(app,state='readonly', values=["y=kx+b", "y=x^n", "Option 3"],command=combobox_callback)

if functions.check_file_availability("Graph.png"):
    my_image = ctk.CTkImage(light_image=Image.open("Graph.png"),
                                    dark_image=Image.open("Graph.png"),
                                    size=(640, 480))
    image_label = ctk.CTkLabel(app, image=my_image, text="")
else:
    image_label = ctk.CTkLabel(app, text="")
    
def select_theme(choise):
    if choise == "white":
        ctk.set_appearance_mode("light")
        app.update()
    else:
        ctk.set_appearance_mode("dark")
        app.update()

theme_dd = ctk.CTkComboBox(app, values=['black', 'white'], command=select_theme, state='readonly')
theme_dd.place(relx=0.821, rely=0.025)
theme_dd.set("Select theme")

image_label.place(relx=0.005, rely=0)

def submit():
    global image_label, my_image
    
    image_label.place_forget()
    
    if options.get() == 'y=kx+b':
        functions.linear(x.get(), k.get(), b.get(), theme_dd.get())
    elif options.get() == 'y=x^n':
        functions.quadratic(x.get(),n.get())
        
    my_image = ctk.CTkImage(light_image=Image.open("Graph.png"),
                                dark_image=Image.open("Graph.png"),
                                size=(640, 480))
    
    image_label = ctk.CTkLabel(app, image=my_image, text="") 
    
    image_label.place(relx=0.005, rely=0)

    pass

submit_b=ctk.CTkButton(app, text="Submit", command=submit)



options.place(relx=0.821, rely=0.100)
options.set("Select")
app.mainloop()