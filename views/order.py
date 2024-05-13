import customtkinter
from PIL import Image

class OrderView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        self.bg_image = Image.open("./assets/image/order_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.header_label = customtkinter.CTkLabel(self, text="", font=('Segoe UI', 32, 'bold'), width=340, fg_color="#0083B3", bg_color="#0083B3", text_color="white")
        self.header_label.place(x=490, y=45)

        self.frame = customtkinter.CTkFrame(self, fg_color="#005778", bg_color="#005778")
        self.frame.place(x=365, y=135)

        self.dari_label = customtkinter.CTkLabel(self.frame, text="DARI", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.dari_label.grid(row=0, column=0, sticky="w")

        self.frame_2 = customtkinter.CTkFrame(self.frame, fg_color="#005778", bg_color="#005778")
        self.frame_2.grid(row=1, column=0, sticky="w")
        self.icon_location = Image.open("./assets/image/icon_location.png")
        self.dari_icon = customtkinter.CTkLabel(self.frame_2, image=customtkinter.CTkImage(self.icon_location, size=[32, 32]), text="", fg_color="#005778")
        self.dari_icon.grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.dari_combobox = customtkinter.CTkComboBox(self.frame_2, values=["Pilih Lokasi"], width=485)
        self.dari_combobox.grid(row=1, column=1, sticky="e", pady=(10, 0), padx=(10, 0))

        self.ke_label = customtkinter.CTkLabel(self.frame, text="KE", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.ke_label.grid(row=2, column=0, sticky="w", pady=(10, 0))

        self.frame_3 = customtkinter.CTkFrame(self.frame, fg_color="#005778", bg_color="#005778")
        self.frame_3.grid(row=3, column=0, sticky="w")
        self.icon_location = Image.open("./assets/image/icon_location.png")
        self.ke_icon = customtkinter.CTkLabel(self.frame_3, image=customtkinter.CTkImage(self.icon_location, size=[32, 32]), text="", fg_color="#005778")
        self.ke_icon.grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.ke_combobox = customtkinter.CTkComboBox(self.frame_3, values=["Pilih Lokasi"], width=485)
        self.ke_combobox.grid(row=0, column=1, sticky="e", pady=(10, 0), padx=(10, 0))

        self.tanggal_label = customtkinter.CTkLabel(self.frame, text="TANGGAL", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.tanggal_label.grid(row=4, column=0, sticky="w", pady=(10, 0))

        self.frame_4 = customtkinter.CTkFrame(self.frame, fg_color="#005778", bg_color="#005778")
        self.frame_4.grid(row=5, column=0, sticky="w")
        self.icon_calendar = Image.open("./assets/image/icon_calendar.png")
        self.tanggal_icon = customtkinter.CTkLabel(self.frame_4, image=customtkinter.CTkImage(self.icon_calendar, size=[32, 32]), text="", fg_color="#005778")
        self.tanggal_icon.grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.tanggal_combobox = customtkinter.CTkComboBox(self.frame_4, values=["Pilih Tanggal"], width=485)
        self.tanggal_combobox.grid(row=0, column=1, sticky="e", pady=(10, 0), padx=(10, 0))

        self.penumpang_label = customtkinter.CTkLabel(self.frame, text="PENUMPANG", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.penumpang_label.grid(row=6, column=0, sticky="w", pady=(10, 0))

        self.frame_5 = customtkinter.CTkFrame(self.frame, fg_color="#005778", bg_color="#005778")
        self.frame_5.grid(row=7, column=0, sticky="w")
        self.icon_user = Image.open("./assets/image/icon_user.png")
        self.penumpang_icon = customtkinter.CTkLabel(self.frame_5, image=customtkinter.CTkImage(self.icon_user, size=[32, 32]), text="", fg_color="#005778")
        self.penumpang_icon.grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.add_penumpang_btn = customtkinter.CTkButton(self.frame_5, text="ADD PENUMPANG")
        self.add_penumpang_btn.grid(row=0, column=1, sticky="e", pady=(10, 0), padx=10)
        self.full_name = customtkinter.CTkLabel(self.frame_5, text="", font=('Segoe UI', 20, 'bold'), text_color="white")
        self.full_name.grid(row=0, column=1, sticky="e", pady=(10, 0), padx=10)

        self.next_btn = customtkinter.CTkButton(self, text="NEXT", font=('Segoe UI', 20, 'bold'), bg_color="#005778", corner_radius=22)
        self.next_btn.place(x=745, y=425)