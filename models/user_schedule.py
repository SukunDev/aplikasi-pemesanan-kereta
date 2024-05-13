from sqlalchemy import Column, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserSchedule(Base):
    __tablename__ = 'user_schedules'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    train_id = Column(Integer)
    stasiun_awal_train_schedules_id = Column(Integer)
    stasiun_akhir_train_schedules_id = Column(Integer)
    no_gerbong = Column(Integer)
    no_chair = Column(Integer)
    has_been_pay = Column(Boolean, default=False)
    created_at = Column(Date)

    def __repr__(self):
        return f"<UserSchedule(id='{self.id}', user_id='{self.user_id}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'train_id': self.train_id,
            'stasiun_awal_train_schedules_id': self.stasiun_awal_train_schedules_id,
            'stasiun_akhir_train_schedules_id': self.stasiun_akhir_train_schedules_id,
            'no_gerbong': self.no_gerbong,
            'no_chair': self.no_chair,
            'has_been_pay': self.has_been_pay,
            'created_at': self.created_at.isoformat(),
        }
