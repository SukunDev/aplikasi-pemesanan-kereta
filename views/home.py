import customtkinter
from PIL import Image

class HomeView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.bg_image = Image.open("./assets/image/home_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.frame = customtkinter.CTkFrame(self, fg_color="#005778", bg_color="#005778")
        self.frame.place(x=385, y=180)

        self.icon_train = Image.open("./assets/image/icon_train.png")
        self.icon_train_image = customtkinter.CTkImage(self.icon_train, size=[94, 94])

        self.logo_local = customtkinter.CTkLabel(self.frame, text="", image=self.icon_train_image)
        self.logo_local.grid(row=1, column=0, pady=10, sticky="ew")
        self.logo_kota = customtkinter.CTkLabel(self.frame, text="", image=self.icon_train_image)
        self.logo_kota.grid(row=1, column=1, pady=10, sticky="ew")

        self.antar_kota_btn = customtkinter.CTkButton(self.frame, text="ANTAR KOTA", font=('Segoe UI', 20, 'bold'), width=165, corner_radius=18, fg_color="white", bg_color="transparent", hover_color="grey", text_color="black")
        self.antar_kota_btn.grid(row=2, column=0, pady=10, padx=30, sticky="w")
        self.local_btn = customtkinter.CTkButton(self.frame, text="LOKAL", font=('Segoe UI', 20, 'bold'), width=165, corner_radius=18, fg_color="#0083B3")
        self.local_btn.grid(row=2, column=1, pady=10, padx=30, sticky="w")
