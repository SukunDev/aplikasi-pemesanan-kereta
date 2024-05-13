import customtkinter


class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('925x500')
        self.title("Aplikasi Pemesanan Kereta")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(width=False, height=False)
        customtkinter.set_appearance_mode("light")
