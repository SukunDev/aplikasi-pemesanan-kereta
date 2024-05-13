from .train import Train, Base as trainBase
from .train_schedule import TrainSchedule, Base as trainScheduleBase
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS



class TrainModel:
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_TRACK_MODIFICATIONS)
        trainBase.metadata.create_all(engine)
        trainScheduleBase.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all_station(self, train_type = "lokal"):
        all_train = self.session.query(Train).filter_by(type=train_type).all()
        stations = []
        for train in all_train:
            all_station = self.session.query(TrainSchedule).filter_by(train_id=train.id).all()
            for station in all_station:
                if station.station in stations:
                    continue
                stations.append(station.station)
        return stations
    
    def get_stasiun_akhir(self, train_type, dari):
        all_train = self.session.query(Train).filter_by(type=train_type).all()
        stations = []
        for train in all_train:
            all_schedule = self.session.query(TrainSchedule).filter_by(train_id=train.id).all()
            for schedule in all_schedule:
                stasiun_awal = self.session.query(TrainSchedule).filter(and_(TrainSchedule.train_id==train.id, TrainSchedule.station==dari)).all()
                for check in stasiun_awal:
                    try:
                        if check.departure <= schedule.arrival:
                            if schedule.station in stations:
                                continue
                            stations.append(schedule.station)
                    except:
                        pass
        return stations
    
    def get_schedule(self, train_type, dari, ke):
        all_train = self.session.query(Train).filter_by(type=train_type).all()
        schedules = []
        for train in all_train:
            kereta =  {}
            stasiun_awal = self.session.query(TrainSchedule).filter(and_(TrainSchedule.train_id==train.id, TrainSchedule.station==dari)).first()
            stasiun_akhir = self.session.query(TrainSchedule).filter(and_(TrainSchedule.train_id==train.id, TrainSchedule.station==ke)).first()
            if stasiun_awal is not None and stasiun_akhir is not None:
                if stasiun_awal.departure <= stasiun_akhir.arrival:
                    continue
                kereta.update({
                    "id": train.id,
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
                    }
                })
                schedules.append(kereta)
        return schedules