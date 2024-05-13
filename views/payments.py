import customtkinter
from PIL import Image

class PaymentsView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        
        self.bg_image = Image.open("./assets/image/payments_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.next_btn = customtkinter.CTkButton(self, text="NEXT", font=('Segoe UI', 24, 'bold'), bg_color="white", fg_color="#0083B3", corner_radius=20)
        self.next_btn.place(x=750, y=420)
