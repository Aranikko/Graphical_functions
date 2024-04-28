import customtkinter as ctk
from PIL import Image
import functions
app = ctk.CTk()
app.geometry("810x484")
app.resizable(False, False)
app.title("graphical functions")

x =ctk.CTkEntry(app, placeholder_text="x:")

y = ctk.CTkEntry(app, placeholder_text="y:")

k =ctk.CTkEntry(app, placeholder_text="k:")

a = ctk.CTkEntry(app, placeholder_text="a:")

b =ctk.CTkEntry(app, placeholder_text="b:")

c = ctk.CTkEntry(app, placeholder_text="c:")


def Enter_box_show(x_show:bool, y_show:bool, k_show:bool, a_show:bool, b_show:bool, c_show:bool):
    
    cons_add_y = 0.075
    counter = 0
    
    x.place_forget()
    b.place_forget()
    k.place_forget()
    submit_b.place_forget()
    y.place_forget()
    c.place_forget()
    a.place_forget()
    
    
    x.delete(0, 'end')
    k.delete(0, 'end')
    b.delete(0, 'end')
    y.delete(0, 'end')
    c.delete(0, "end")
    a.delete(0, "end")
    
    if x_show:
        x.place(relx=0.821, rely=0.175)
        counter+=1
        
    if y_show:
        y.place(relx=0.821, rely=0.175+(cons_add_y*counter))
        counter+=1
        
    if k_show:
        k.place(relx=0.821, rely=0.175+(cons_add_y*counter))
        counter+=1
    if a_show:
        a.place(relx=0.821, rely=0.175+(cons_add_y*counter))
        counter+=1
        
    if b_show:
        b.place(relx=0.821, rely=0.175+(cons_add_y*counter))
        counter+=1
        
    if c_show:
        c.place(relx=0.821, rely=0.175+(cons_add_y*counter))
        counter+=1
        
    
    submit_b.place(relx=0.821, rely=0.175+(cons_add_y*counter))

def combobox_callback(choice): # add GUI
    if choice == "y=ax+b":

        Enter_box_show(1,0,0,1,1,0)
        
    elif choice == " y=kx+b":
        
        Enter_box_show(1,0,1,0,1,0)
        
    elif choice == "y = ax^2 + bx + c":
        
        Enter_box_show(1,0,0,1,1,1)
        
    elif choice == "y = x^3":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = sqrt(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = 1/x":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = lg(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = sin(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = tg(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = ctg(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = ctg(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = arcsin(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "y = arccos(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "z = x*y":
        
        Enter_box_show(1,1,0,0,0,0)
        
    elif choice == "z = sin(x)":
        
        Enter_box_show(1,0,0,0,0,0)
        
    elif choice == "z = sin(x)cos(y)":
        Enter_box_show(1,1,0,0,0,0)
    elif choice == "z = x2y2+2":
        
        Enter_box_show(1,1,0,0,0,0)

options = ctk.CTkComboBox(app,state='readonly', values=[ # sellect
                                                        "y=ax+b", "y = ax^2 + bx + c", "y = x^3",
                                                        "y = sqrt(x)", "y = 1/x", "y = lg(x)",
                                                        "y = sin(x)", "y = tg(x)", "y = ctg(x)",
                                                        "y = arcsin(x)", "y = arccos(x)", "z = x*y",
                                                        "z = sin(x)", "z = sin(x)cos(y)", "z = x2y2+2"
                                                        ],command=combobox_callback)

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


image_name = ctk.CTkEntry(app, placeholder_text="Image name", )
image_name.place(relx=0.821, rely=0.925)
image_name.insert(0, "Image_name")

def submit():
    global image_label, my_image
    
    image_label.place_forget()
    
    if options.get() == 'y=ax+b':
        functions.linear(x.get(), a.get(), b.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = ax^2 + bx + c':
        functions.quadratic_equation(x.get(), a.get(),b.get(),c.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = x^3':
        functions.cubic_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = sqrt(x)':
        functions.square_root_function(x.get(), theme_dd.get(), image_name.get())  
    elif options.get() == 'y = 1/x':
        functions.reciprocal_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = lg(x)':
        functions.natural_log_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = sin(x)':
        functions.sine_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = tg(x)':
        functions.tangent_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = ctg(x)':
        functions.cotangent_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = arcsin(x)':
        functions.arcsine_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'y = arccos(x)':
        functions.arccosine_function(x.get(), theme_dd.get(), image_name.get())
    elif options.get() == 'z = x*y':
        functions.product_function(x.get(), y.get(), image_name.get())
    elif options.get() == 'z = sin(x)':
        functions.sine_product_function(x.get(), image_name.get())
    elif options.get() == 'z = sin(x)cos(y)':
        functions.sine_cosine_product_function(x.get(), y.get(), image_name.get())
    elif options.get() == 'z = x2y2+2':
        functions.quadratic_product_function(x.get(), y.get(), image_name.get())
    my_image = ctk.CTkImage(light_image=Image.open(f"{image_name.get()}.png"),
                                dark_image=Image.open(f"{image_name.get()}.png"),
                                size=(640, 480))
    
    image_label = ctk.CTkLabel(app, image=my_image, text="") 
    
    image_label.place(relx=0.005, rely=0)

    pass

submit_b=ctk.CTkButton(app, text="Submit", command=submit)


options.place(relx=0.821, rely=0.100)
options.set("Select")
app.mainloop()