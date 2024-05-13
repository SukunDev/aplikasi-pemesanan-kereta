import customtkinter
from PIL import Image

class SignUpView(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        self.bg_image = Image.open("./assets/image/signup_back.png")
        self.bg_label = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(self.bg_image, size=[925, 500]), text="")
        self.bg_label.grid(row=0, column=0, sticky="nsew")
        
        self.formFrame = customtkinter.CTkFrame(self, fg_color="#005778", bg_color="#005778")
        self.formFrame.place(x=200, y=235)

        self.username_label = customtkinter.CTkLabel(self.formFrame, text="Username", text_color="white")
        self.username_input = customtkinter.CTkEntry(self.formFrame, width=225)
        self.username_label.grid(row=1, column=0, pady=10, sticky="w")
        self.username_input.grid(row=1, column=1, padx=(10, 0), sticky="ew")

        self.password_label = customtkinter.CTkLabel(self.formFrame, text="Password", text_color="white")
        self.password_input = customtkinter.CTkEntry(self.formFrame, show="*", width=225)
        self.password_label.grid(row=2, column=0, sticky="w")
        self.password_input.grid(row=2, column=1, padx=(10, 0), sticky="ew")

        self.confirm_label = customtkinter.CTkLabel(self.formFrame, text="Confirm", text_color="white")
        self.confirm_input = customtkinter.CTkEntry(self.formFrame, show="*", width=225)
        self.confirm_label.grid(row=3, column=0, pady=10, sticky="w")
        self.confirm_input.grid(row=3, column=1, padx=(10, 0), sticky="ew")


        self.signin_btn = customtkinter.CTkButton(self, text="Sign In", fg_color="white", bg_color="transparent", hover_color="grey", text_color="black", corner_radius=0)
        self.signin_btn.place(x=200, y=380)
