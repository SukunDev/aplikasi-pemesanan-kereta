import customtkinter
from PIL import Image

class DetailOrderView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid_columnconfigure(0, weight=3)

        self.header_label = customtkinter.CTkLabel(self, text="Detail Pesanan", font=('Segoe UI', 32), text_color="black")
        self.header_label.grid(row=0, column=0, sticky="ew", pady=30)

        self.card_frame = customtkinter.CTkFrame(self, fg_color="#0083B3", corner_radius=18)
        self.card_frame.grid(row=1, column=0, sticky="ns", pady=(0, 30))

        self.container_frame = customtkinter.CTkFrame(self.card_frame, fg_color="#005778", corner_radius=20)
        self.container_frame.grid(row=0, column=0, columnspan=2, sticky="ewns", padx=20, pady=(20, 10))

        self.image_frame = customtkinter.CTkFrame(self.container_frame, fg_color="#0083B3", corner_radius=20)
        self.image_frame.grid(row=0, column=0, sticky="ewns", padx=20, pady=20)

        self.icon_user_frame = Image.open("./assets/image/icon_user_frame.png")
        self.bg_label = customtkinter.CTkLabel(self.image_frame, image=customtkinter.CTkImage(self.icon_user_frame, size=[140, 140]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10,4))

        self.detail_frame = customtkinter.CTkFrame(self.container_frame, fg_color="#005778", corner_radius=20)
        self.detail_frame.grid(row=0, column=1, sticky="ewns", pady=10, padx=(0, 20))

        self.full_name_label = customtkinter.CTkLabel(self.detail_frame, text="Nama", font=('Segoe UI', 24, "bold"), text_color="white")
        self.full_name_label.grid(row=0, column=1, sticky="wn")
        self.nik_label = customtkinter.CTkLabel(self.detail_frame, text="NKK/NIK", font=('Segoe UI', 18), text_color="white")
        self.nik_label.grid(row=1, column=1, sticky="wn", pady=(3, 0))
        self.train_name_label = customtkinter.CTkLabel(self.detail_frame, text="nama kereta", font=('Segoe UI', 24), text_color="white")
        self.train_name_label.grid(row=2, column=1, sticky="wn", pady=(3, 0))
        self.tempat_duduk_label = customtkinter.CTkLabel(self.detail_frame, text="no kursi", font=('Segoe UI', 18), text_color="white")
        self.tempat_duduk_label.grid(row=3, column=1, sticky="wn", pady=(3, 0))
        self.booking_date_label = customtkinter.CTkLabel(self.detail_frame, text="tanggal", font=('Segoe UI', 18), text_color="white")
        self.booking_date_label.grid(row=4, column=1, sticky="wn", pady=(3, 0))
        
        self.stasiun_awal_label = customtkinter.CTkLabel(self.card_frame, text="stasiun awal", font=('Segoe UI', 18, "bold"), text_color="white")
        self.stasiun_awal_label.grid(row=1, column=0, sticky="wn", padx=20, pady=(0, 10))
        self.stasiun_akhir_label = customtkinter.CTkLabel(self.card_frame, text="stasiun akhir", font=('Segoe UI', 18, "bold"), text_color="white")
        self.stasiun_akhir_label.grid(row=1, column=1, sticky="en", padx=20, pady=(0, 10))

        self.next_btn = customtkinter.CTkButton(self, text="NEXT", font=('Segoe UI', 24, 'bold'), bg_color="white", fg_color="#0083B3", corner_radius=20)
        self.next_btn.place(x=750, y=420)