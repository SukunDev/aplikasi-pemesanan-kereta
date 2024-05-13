import customtkinter
from PIL import Image

class AddPenumpangView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.bg_image = Image.open("./assets/image/order_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        self.header_label = customtkinter.CTkLabel(self, text="ADD PENUMPANG", font=('Segoe UI', 32, 'bold'), width=340, fg_color="#0083B3", bg_color="#0083B3", text_color="white")
        self.header_label.place(x=490, y=45)

        self.frame = customtkinter.CTkFrame(self, fg_color="#005778", bg_color="#005778")
        self.frame.place(x=365, y=140)

        self.nama_label = customtkinter.CTkLabel(self.frame, text="NAMA", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.nama_label.grid(row=0, column=0, sticky="w")
        self.nama_input = customtkinter.CTkEntry(self.frame, width=330)
        self.nama_input.grid(row=1, column=0, sticky="w", pady=(10, 0))

        self.nik_label = customtkinter.CTkLabel(self.frame, text="NIK", font=('Segoe UI', 24, 'bold'), text_color="white")
        self.nik_label.grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.nik_input = customtkinter.CTkEntry(self.frame, width=330)
        self.nik_input.grid(row=3, column=0, sticky="w", pady=(10, 0))

        self.finish_btn = customtkinter.CTkButton(self, text="FINISH", font=('Segoe UI', 24, 'bold'), bg_color="#005778", fg_color="#0083B3", corner_radius=20)
        self.finish_btn.place(x=750, y=420)