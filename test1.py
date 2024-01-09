from PIL import Image
import customtkinter as ctk

app = ctk.CTk()
app.geometry("680x680")

# Create a CTkImage object with a larger size
my_image = ctk.CTkImage(light_image=Image.open("my_plot.png"), dark_image=Image.open("my_plot.png"), size=(640, 480))

# Use the image with a button


image_label = ctk.CTkLabel(app, image=my_image, text="") 
image_label.pack()

app.mainloop()