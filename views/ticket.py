import customtkinter
from PIL import Image

class TicketView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        
        self.bg_image = Image.open("./assets/image/tiket_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.booking_date_label = customtkinter.CTkLabel(self, text="", font=('Segoe UI', 18, "bold"), text_color="white", fg_color="#00AEEF", bg_color="#00AEEF")
        self.booking_date_label.place(x=510, y=127)
        

        self.detail_frame = customtkinter.CTkFrame(self, fg_color="#00AEEF", bg_color="#00AEEF")
        self.detail_frame.place(x=320, y=310)
        self.full_name_label = customtkinter.CTkLabel(self.detail_frame, text="", font=('Segoe UI', 24, "bold"), text_color="white")
        self.full_name_label.grid(row=0, column=1, sticky="wn")
        self.nik_label = customtkinter.CTkLabel(self.detail_frame, text="", font=('Segoe UI', 18), text_color="white")
        self.nik_label.grid(row=1, column=1, sticky="wn", pady=(3, 0))
        self.stasiun_akhir_label = customtkinter.CTkLabel(self.detail_frame, text="", font=('Segoe UI', 24), text_color="white")
        self.stasiun_akhir_label.grid(row=2, column=1, sticky="wn", pady=(3, 0))
        self.tempat_duduk_label = customtkinter.CTkLabel(self.detail_frame, text="", font=('Segoe UI', 18), text_color="white")
        self.tempat_duduk_label.grid(row=3, column=1, sticky="wn", pady=(3, 0))