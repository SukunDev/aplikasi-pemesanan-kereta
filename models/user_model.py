from .base import ObservableModel
from .user import User, Base as userBase
from .user_schedule import UserSchedule, Base as userScheduleBase
from .train import Train
from .train_schedule import TrainSchedule
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from tkinter import messagebox
from utils.helper import encode_md5
from datetime import datetime


class UserModel(ObservableModel):
    def __init__(self):
        super().__init__()
        engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_TRACK_MODIFICATIONS)
        userBase.metadata.create_all(engine)
        userScheduleBase.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.is_logged_in = False
        self.current_user = None

    def login(self, data) -> None:
        check_user = self.__get_user_by_username(username=data['username'])
        if check_user is None:
            messagebox.showerror('User Not Found', 'Username not found, please Sign Up before Sign In')
            return

        user = check_user.serialize
        if user['password'] != encode_md5(data['password']):
            messagebox.showerror('Invalid Password', 'Invalid Password')
            return
        
        self.is_logged_in = True
        self.current_user = check_user.serialize
        self.trigger_event("auth_changed")

    def register(self, data):
        check_user = self.__get_user_by_username(username=data['username'])
        if check_user is not None:
            messagebox.showerror('User Found', 'Username has been registered')

        try:
            new_user = User(username=data['username'], password=encode_md5(data['password']), created_at=datetime.today())
            self.session.add(new_user)
            self.session.commit()
            self.is_logged_in = True
            self.current_user = new_user.serialize
            self.trigger_event("auth_changed")
        except Exception as e:
            messagebox.showerror('Error', str(e))
        
    def welcome_next_btn(self) -> None:
        self.__update_is_new_user(username=self.current_user['username'])

    def add_penumpang_btn(self, data) -> None:
        self.__update_full_name(username=self.current_user['username'], full_name=data['full_name'], nik=data['nik'])

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")

    def create_user_schedule(self, data, no_gerbong, no_chair):
            try:
                new_schedule = UserSchedule(
                    user_id=self.current_user['id'],
                    train_id=data['id'],
                    stasiun_awal_train_schedules_id=data['stasiun_awal']['id'],
                    stasiun_akhir_train_schedules_id=data['stasiun_akhir']['id'],
                    no_gerbong=no_gerbong,
                    no_chair=no_chair,
                    created_at=datetime.strptime(data['booking_date'], "%B, %d %Y")
                )
                self.session.add(new_schedule)
                self.session.commit()
                return new_schedule.id
            except Exception as e:
                print(e)

    def get_user_schedule(self, user_id):
        data = None
        for schedule in self.session.query(UserSchedule).filter_by(has_been_pay=False, user_id=user_id).all():
            if datetime.now().date() <= schedule.created_at:
                train = self.session.query(Train).filter_by(id=schedule.train_id).first()
                stasiun_awal = self.session.query(TrainSchedule).filter_by(id=schedule.stasiun_awal_train_schedules_id).first()
                stasiun_akhir = self.session.query(TrainSchedule).filter_by(id=schedule.stasiun_akhir_train_schedules_id).first()
                data = {
                    "id": schedule.train_id,
                    "schedule_id": schedule.id,
                    "name": train.name,
                    "name_code": train.name_code,
                    "total_gerbong": train.total_gerbong,
                    "total_chair": train.total_chair,
                    "stasiun_awal": {
                        "id": stasiun_awal.id,
                        "name": stasiun_awal.station,
                        "arrival": stasiun_awal.arrival.strftime("%H:%M"),
                        "departure": stasiun_awal.departure.strftime("%H:%M")
                    },
                    "stasiun_akhir": {
                        "id": stasiun_akhir.id,
                        "name": stasiun_akhir.station,
                        "arrival": stasiun_akhir.arrival.strftime("%H:%M"),
                        "departure": stasiun_akhir.departure.strftime("%H:%M")
                    },
                    "booking_date": schedule.created_at.strftime("%B, %d %Y"),
                    "no_gerbong": schedule.no_gerbong,
                    "no_chair": schedule.no_chair
                }
        return data

    def get_booking_schedule(self, booking_date, dari, ke):
        data = []
        for schedule in self.session.query(UserSchedule).filter_by(created_at=datetime.strptime(booking_date, '%B, %d %Y').date()).all():
            train = self.session.query(Train).filter_by(id=schedule.train_id).first()
            stasiun_awal = self.session.query(TrainSchedule).filter_by(id=schedule.stasiun_awal_train_schedules_id).first()
            stasiun_akhir = self.session.query(TrainSchedule).filter_by(id=schedule.stasiun_akhir_train_schedules_id).first()
            if dari == stasiun_awal.station and ke == stasiun_akhir.station:
                data.append({
                    "id": schedule.train_id,
                    "schedule_id": schedule.id,
                    "name": train.name,
                    "name_code": train.name_code,
                    "total_gerbong": train.total_gerbong,
                    "total_chair": train.total_chair,
                    "stasiun_awal": {
                        "id": stasiun_awal.id,
                        "name": stasiun_awal.station,
                        "arrival": stasiun_awal.arrival.strftime("%H:%M"),
                        "departure": stasiun_awal.departure.strftime("%H:%M")
                    },
                    "stasiun_akhir": {
                        "id": stasiun_akhir.id,
                        "name": stasiun_akhir.station,
                        "arrival": stasiun_akhir.arrival.strftime("%H:%M"),
                        "departure": stasiun_akhir.departure.strftime("%H:%M")
                    },
                    "booking_date": schedule.created_at.strftime("%B, %d %Y"),
                    "no_gerbong": schedule.no_gerbong,
                    "no_chair": schedule.no_chair
                })
                
        return data

    def update_schedule(self, schedule_id):
        schedule_to_update = self.session.query(UserSchedule).filter_by(id=schedule_id).first()
        if schedule_to_update:
            schedule_to_update.has_been_pay = True
            self.session.merge(schedule_to_update)
            self.session.commit()

    def __get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()
    
    def __update_is_new_user(self, username):
        user_to_update = self.session.query(User).filter_by(username=username).first()
        if user_to_update:
            user_to_update.is_new_user = False
            self.session.merge(user_to_update)
            self.session.commit()
        self.current_user = user_to_update.serialize
        self.trigger_event("auth_changed")
    
    def __update_full_name(self, username, full_name, nik):
        user_to_update = self.session.query(User).filter_by(username=username).first()
        if user_to_update:
            user_to_update.full_name = full_name
            user_to_update.nik = nik
            self.session.merge(user_to_update)
            self.session.commit()
        self.current_user = user_to_update.serialize
        self.trigger_event("auth_changed")
