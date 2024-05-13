from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    full_name = Column(String, default="")
    nik = Column(String, default="")
    is_new_user = Column(Boolean, default=True)
    created_at = Column(Date)

    def __repr__(self):
        return f"<User(id='{self.id}', username='{self.username}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'full_name': self.full_name,
            'nik': self.nik,
            'is_new_user': self.is_new_user,
            'created_at': self.created_at.isoformat(),
        }
