import customtkinter
from PIL import Image

class WelcomeView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bg_image = Image.open("./assets/image/welcome_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.frame = customtkinter.CTkFrame(self, fg_color="white", bg_color="white")
        self.frame.place(x=0, y=0)
        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)

        self.header = customtkinter.CTkLabel(self.frame, text="Welcome to Ease Trip", width=925, font=('Segoe UI', 34, 'bold'), fg_color="white")
        self.header.grid(row=0, column=0, sticky="ew", pady=(10, 20))

        self.description = customtkinter.CTkLabel(self.frame, text="Program pembelian tiket kereta api online adalah sebuah platform digital \nyang memungkinkan pengguna untuk melakukan pembelian tiket perjalanan kereta \napi melalui internet. memberikan kemudahan bagi pengguna dengan menyediakan \nberbagai fitur seperti pencarian jadwal perjalanan, pemilihan kursi, serta \nberbagai pilihan metode pembayaran yang aman dan nyaman.", font=('Microsoft YaHei UI Light', 20, 'bold'), fg_color="white")
        self.description.grid(row=1, column=0, sticky="ew")

        self.next_btn = customtkinter.CTkButton(self.frame, text="Next", font=('Segoe UI', 25, 'bold'))
        self.next_btn.grid(row=2, column=0, sticky="w", pady=(40, 0), padx=(150, 0))