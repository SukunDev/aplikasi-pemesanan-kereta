import customtkinter
from PIL import Image

class ChooseChairView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=3)

        self.header_label = customtkinter.CTkLabel(self, text="PILIH GERBONG", font=('Segoe UI', 32, 'bold'), width=340, text_color="black")
        self.header_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))

        self.frame_1 = customtkinter.CTkFrame(self, fg_color="white", bg_color="transparent")
        self.frame_1.grid(row=1, column=0, sticky="wsn", padx=10)

        self.frame_2 = customtkinter.CTkFrame(self, fg_color="white", bg_color="transparent")
        self.frame_2.grid(row=1, column=1, sticky="esn", padx=10)

        self.prev_button = customtkinter.CTkButton(self, text="PREV", width=200, height=30, corner_radius=20)
        self.prev_button.grid(row=2, column=0, sticky="e", padx=5, pady=(15, 5))
        self.next_button = customtkinter.CTkButton(self, text="NEXT", width=200, height=30, corner_radius=20)
        self.next_button.grid(row=2, column=1, sticky="w", padx=5, pady=(15, 5))

        self.choose_chair_btn = []

    
    def add_kursi(self, total_chair):
        total = int(total_chair / 2)
        total_row = int(total / 3)
        chair_num = 0
        for kiri in range(total_row):
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_1, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kiri+1), column=0, sticky="w", padx=10, pady=5)
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_1, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kiri+1), column=1, sticky="w", padx=10, pady=5)
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_1, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kiri+1), column=2, sticky="w", padx=10, pady=5)

        for kanan in range(total_row):
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_2, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kanan+1), column=0, sticky="w", padx=10, pady=5)
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_2, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kanan+1), column=1, sticky="w", padx=10, pady=5)
            self.choose_chair_btn.append(customtkinter.CTkButton(self.frame_2, text="", width=70, height=55, corner_radius=18))
            self.choose_chair_btn[chair_num-1].grid(row=int(kanan+1), column=2, sticky="w", padx=10, pady=5)
            