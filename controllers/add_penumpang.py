from models.main import Model
from views.main import View
from tkinter import messagebox



class AddPenumpangController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["add_penumpang"]
        
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.finish_btn.configure(command=self.finish_btn)

    def finish_btn(self):
        nama = self.frame.nama_input.get()
        nik = self.frame.nik_input.get()
        if len(nama) < 1:
            messagebox.showinfo('Empty Field', 'Nama field can\'t empty')
        elif len(nik) < 1:
            messagebox.showinfo('Empty Field', 'NIK field can\'t empty')
        else:
            data = {
                "full_name": nama,
                "nik": nik,
            }
            self.model.userModel.add_penumpang_btn(data)
        self.view.switch('order')