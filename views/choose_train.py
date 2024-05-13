import customtkinter
from PIL import Image

class ChooseTrainView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame = customtkinter.CTkScrollableFrame(self, fg_color="white")
        self.frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)
        
        self.pilih_btn = []

        self.header_label = customtkinter.CTkLabel(self.frame, text="PILIHAN KERETA", font=('Segoe UI', 32, 'bold'), width=340, text_color="black")
        self.header_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 30))


    def add_schdule(self, trains):
        
        loop_index = 1
        for train in trains:
            frame = customtkinter.CTkFrame(self.frame, fg_color="#0083B3", bg_color="transparent", corner_radius=16)
            frame.grid(row=loop_index, column=0, columnspan=2, sticky="ew", pady=(0, 10))
            nama_train = customtkinter.CTkLabel(frame, text=train['name'], font=('Segoe UI', 18, 'bold'), text_color="white")
            nama_train.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))
            name_code_train = customtkinter.CTkLabel(frame, text=f"({train['name_code']})", font=('Segoe UI', 16), text_color="white")
            name_code_train.grid(row=0, column=1, sticky="w", pady=(10, 0))

            stasiun_awal_frame = customtkinter.CTkFrame(frame, fg_color="#0083B3", bg_color="transparent")
            stasiun_awal_frame.grid(row=1, column=0, sticky="ew")
            icon_location = Image.open("./assets/image/icon_location.png")
            dari_icon = customtkinter.CTkLabel(stasiun_awal_frame, image=customtkinter.CTkImage(icon_location, size=[20, 20]), text="", fg_color="#0083B3")
            dari_icon.grid(row=0, column=0, sticky="w", padx=(10, 0))
            arrival = customtkinter.CTkLabel(stasiun_awal_frame, text=train['stasiun_awal']['departure'], font=('Segoe UI', 18, 'bold'), text_color="white")
            arrival.grid(row=0, column=1, sticky="w", padx=(10, 0))
            stasiun_awal = customtkinter.CTkLabel(stasiun_awal_frame, text=f"{train['stasiun_awal']['name']}", font=('Segoe UI', 16, 'bold'), text_color="white")
            stasiun_awal.grid(row=0, column=2, sticky="w", padx=(10, 0))

            stasiun_akhir_frame = customtkinter.CTkFrame(frame, fg_color="#0083B3", bg_color="transparent")
            stasiun_akhir_frame.grid(row=2, column=0, sticky="ew", pady=(20, 0))
            icon_train = Image.open("./assets/image/icon_train.png")
            dari_icon = customtkinter.CTkLabel(stasiun_akhir_frame, image=customtkinter.CTkImage(icon_train, size=[20, 20]), text="", fg_color="#0083B3")
            dari_icon.grid(row=0, column=0, sticky="w", padx=(10, 0))
            arrival = customtkinter.CTkLabel(stasiun_akhir_frame, text=train['stasiun_akhir']['departure'], font=('Segoe UI', 18, 'bold'), text_color="white")
            arrival.grid(row=0, column=1, sticky="w", padx=(10, 0))
            stasiun_akhir = customtkinter.CTkLabel(stasiun_akhir_frame, text=f"{train['stasiun_akhir']['name']}", font=('Segoe UI', 16, 'bold'), text_color="white")
            stasiun_akhir.grid(row=0, column=2, sticky="w", padx=(10, 0))

            self.pilih_btn.append(customtkinter.CTkButton(frame, text="PILIH"))
            self.pilih_btn[loop_index - 1].grid(row=3, column=0, sticky="w", pady=(10, 10), padx=10)
            
            loop_index += 1