from models.main import Model
from models.train_model import TrainModel
from models.actions_model import ActionModel
from views.main import View
from utils.helper import get_days
from tkinter import messagebox


class OderController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["order"]
        self.data = {
            "dari": "",
            "ke": "",
            "tanggal": "",
        }

        self.date_field = []
        for date in get_days():
            self.date_field.append(date.strftime("%B, %d %Y"))

        self.train = TrainModel()
        self.all_station = ["Pilih Lokasi"]
        self.all_stasiun_akhir = ["Pilih Lokasi"]
        self._bind()
        self.model.action.add_event_listener("actions", self.action_state_listener)
        
    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.dari_combobox.configure(command=self.dari_combobox, values=self.all_station)
        self.frame.ke_combobox.configure(command=self.ke_combobox, values=self.all_stasiun_akhir)
        self.frame.tanggal_combobox.configure(command=self.tanggal_combobox, values=self.date_field)
        self.frame.add_penumpang_btn.configure(command=self.add_penumpang_btn)
        self.frame.next_btn.configure(command=self.next_btn)

    def action_state_listener(self, props: ActionModel) -> None:
        action = props.get()
        if action is not None:
            if action['type'] == "order":
                self.frame.header_label.configure(text=action['data']['message'])
                self.all_station = self.train.get_all_station(train_type=action['data']['type'])
                self.all_stasiun_akhir = self.train.get_all_station(train_type=action['data']['type'])
                self.data.update({"type": action['data']['type']})
                self._bind()

    def dari_combobox(self, choice):
        if choice == self.data['ke']:
            messagebox.showinfo('Location Error', 'Stasiun Awal dan Stasiun Akhir tidak boleh sama')
            self.frame.dari_combobox.set("Pilih Lokasi")
            return
        self.data.update({"dari": choice})
        self.data.update({"ke": ""})
        self.frame.ke_combobox.set("Pilih Lokasi")

        self.all_stasiun_akhir =  self.train.get_stasiun_akhir(train_type=self.data['type'], dari=choice)
        self._bind()

    def ke_combobox(self, choice):
        if len(self.data['dari']) < 1:
            messagebox.showinfo('Location Error', 'Anda harus memilih Stasiun Awal Terlebih dahulu')
            self.frame.ke_combobox.set("Pilih Lokasi")
            return
        if choice == self.data['dari']:
            messagebox.showinfo('Location Error', 'Stasiun Awal dan Stasiun Akhir tidak boleh sama')
            self.frame.ke_combobox.set("Pilih Lokasi")
            return
        self.data.update({"ke": choice})

    def tanggal_combobox(self, choice):
        self.data.update({"tanggal": choice})

    def add_penumpang_btn(self):
        self.view.switch('add_penumpang')

    def next_btn(self):
        if len(self.data['dari']) < 1:
            messagebox.showinfo('Field Error', 'Stasiun Awal tidak boleh kosong')
        elif len(self.data['ke']) < 1:
            messagebox.showinfo('Field Error', 'Stasiun Akhir tidak boleh kosong')
        elif len(self.data['tanggal']) < 1:
            messagebox.showinfo('Field Error', 'Tanggal tidak boleh kosong')
        else:
            self.model.action.set(type="choose_train", data=self.data)
            self.view.switch("choose_train")