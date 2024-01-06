import flet as ft


def main(page: ft.Page):
    
    page.window_max_width = 850
    page.window_max_height = 800
    page.window_min_width = 850
    page.window_min_height = 800
    
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()
    

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("y=kx+b"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "pls enter x"
            page.update()
        else:
            name = txt_name.value
            print(type(name))

    txt_name = ft.TextField(label="X")

    page.add(txt_name, ft.ElevatedButton("enter", on_click=btn_click))
    
    page.add(ft.Image(src=f"my_plot.png"))

ft.app(target=main)