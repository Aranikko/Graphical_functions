import customtkinter as ctk
from PIL import Image
import functions
app = ctk.CTk()
app.geometry("810x484")
app.resizable(False, False)


def select_theme(choise):
    if choise == "white":
        ctk.set_appearance_mode("light")
        print("white")
        app.update()
    else:
        ctk.set_appearance_mode("dark")


theme_dd = ctk.CTkComboBox(app, values=['black', 'white'], command=select_theme, state='readonly')
theme_dd.place(relx=0.821, rely=0.025)
theme_dd.set("Select theme")

my_image = ctk.CTkImage(light_image=Image.open("Graph.png"),
                                  dark_image=Image.open("Graph.png"),
                                  size=(640, 480))

image_label = ctk.CTkLabel(app, image=my_image, text="") 
image_label.place(relx=0.005, rely=0)

x =ctk.CTkEntry(app, placeholder_text="x:")
k =ctk.CTkEntry(app, placeholder_text="k:")
b =ctk.CTkEntry(app, placeholder_text="b:")

def submit():
    global image_label, my_image
    
    image_label.place_forget()
    
    functions.linear(x.get(), k.get(), b.get(), theme_dd.get())
    
    my_image = ctk.CTkImage(light_image=Image.open("Graph.png"),
                                  dark_image=Image.open("Graph.png"),
                                  size=(640, 480))
    
    image_label = ctk.CTkLabel(app, image=my_image, text="") 
    
    image_label.place(relx=0.005, rely=0)

    pass

submit_b=ctk.CTkButton(app, text="Submit", command=submit)

def combobox_callback(choice):
    if choice == "y=kx+b":

        x.place(relx=0.821, rely=0.175)
        
        k.place(relx=0.821, rely=0.250)
        
        b.place(relx=0.821, rely=0.325)
        
        submit_b.place(relx=0.821, rely=0.400)
    else:
        x.place_forget()
        k.place_forget()
        b.place_forget()
        submit_b.place_forget()
        

# Create a list of options for the options
options = ["y=kx+b", "y=x^n", "Option 3"]

# Create the CTkCombobox widgeta
options = ctk.CTkComboBox(app,state='readonly', values=options,command=combobox_callback)
options.place(relx=0.821, rely=0.100)
options.set("Select")
app.mainloop()