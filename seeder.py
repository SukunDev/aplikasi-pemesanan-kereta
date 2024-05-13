import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.user import User, Base as userBase
from models.user_schedule import UserSchedule, Base as userScheduleBase
from models.train import Train, Base as trainBase
from models.train_schedule import TrainSchedule, Base as trainScheduleBase
from models.action import Action, Base as actionBase

# Buat engine SQLAlchemy
engine = create_engine('sqlite:///database.db')

# Buat tabel-tabel dalam basis data
userBase.metadata.create_all(engine)
userScheduleBase.metadata.create_all(engine)
trainBase.metadata.create_all(engine)
trainScheduleBase.metadata.create_all(engine)
actionBase.metadata.create_all(engine)

# Buat SessionMaker
Session = sessionmaker(bind=engine)
session = Session()

# Data Jadwal Kereta
train_schedules = [
  {
    "name": "KERETA API COMMUTER EXPRESS",
    "name_code": "300",
    "type": "lokal",
    "total_gerbong": 5,
    "total_chair": 36,
    "stasiun": [
      {
        "nama": "SURABAYA KOTA",
        "jam_datang": "10:00",
        "jam_berangkat": "10:35"
      },
      {
        "nama": "SURABAYA GUBENG",
        "jam_datang": "10:40",
        "jam_berangkat": "10:48"
      },
      {
        "nama": "WONOKROMO",
        "jam_datang": "10:55",
        "jam_berangkat": "10:58"
      },
      {
        "nama": "SEPANJANG",
        "jam_datang": "11:00",
        "jam_berangkat": "11:07"
      },
      {
        "nama": "BOHARAN",
        "jam_datang": "Tidak Berhenti",
        "jam_berangkat": "Tidak Berhenti"
      },
      {
        "nama": "KRIAN",
        "jam_datang": "11:20",
        "jam_berangkat": "11:50"
      },
      {
        "nama": "KEDINDING",
        "jam_datang": "12:00",
        "jam_berangkat": "12:04"
      },
      {
        "nama": "TARIK",
        "jam_datang": "12:10",
        "jam_berangkat": "12:12"
      },
      {
        "nama": "MOJOKERTO",
        "jam_datang": "12:20",
        "jam_berangkat": "12:23"
      },
      {
        "nama": "CURAHMALANG",
        "jam_datang": "12:28",
        "jam_berangkat": "12:32"
      },
      {
        "nama": "SUMOBITO",
        "jam_datang": "12:40",
        "jam_berangkat": "12:44"
      },
      {
        "nama": "PETERONGAN",
        "jam_datang": "12:50",
        "jam_berangkat": "12:57"
      },
      {
        "nama": "JOMBANG",
        "jam_datang": "13:30",
        "jam_berangkat": "13:40"
      },
      {
        "nama": "SEMBUNG",
        "jam_datang": "13:40",
        "jam_berangkat": "13:52"
      },
      {
        "nama": "KERTOSONO",
        "jam_datang": "14:00",
        "jam_berangkat": "14:05"
      },
      {
        "nama": "PURWOASRI",
        "jam_datang": "14:10",
        "jam_berangkat": "14:15"
      },
      {
        "nama": "PAPAR",
        "jam_datang": "14:15",
        "jam_berangkat": "14:30"
      },
      {
        "nama": "MINGGIRAN",
        "jam_datang": "14:40",
        "jam_berangkat": "14:45"
      },
      {
        "nama": "SUSUHAN",
        "jam_datang": "14:47",
        "jam_berangkat": "14:50"
      },
      {
        "nama": "KEDIRI",
        "jam_datang": "14:58",
        "jam_berangkat": "15:00"
      },
      {
        "nama": "NGADILUWIH",
        "jam_datang": "15:05",
        "jam_berangkat": "15:10"
      },
      {
        "nama": "KRAS",
        "jam_datang": "15:15",
        "jam_berangkat": "15:25"
      },
      {
        "nama": "NGUJANG",
        "jam_datang": "15:20",
        "jam_berangkat": "15:35"
      },
      {
        "nama": "TULUNGAGUNG",
        "jam_datang": "15:40",
        "jam_berangkat": "15:50"
      },
      {
        "nama": "SUMBERGEMPOL",
        "jam_datang": "15:55",
        "jam_berangkat": "16:00"
      },
      {
        "nama": "NGUNUT",
        "jam_datang": "16:10",
        "jam_berangkat": "16:20"
      },
      {
        "nama": "REJOTANGAN",
        "jam_datang": "16:15",
        "jam_berangkat": "16:25"
      },
      {
        "nama": "BLITAR",
        "jam_datang": "16:30",
        "jam_berangkat": "16:45"
      }
    ]
  },
  {
    "name": "KERETA API COMMUTER CINTA",
    "name_code": "445",
    "type": "lokal",
    "total_gerbong": 5,
    "total_chair": 36,
    "stasiun": [
      {
        "nama": "SURABAYA KOTA",
        "jam_datang": "04:00",
        "jam_berangkat": "04:30"
      },
      {
        "nama": "SURABAYA GUBENG",
        "jam_datang": "04:38",
        "jam_berangkat": "04:41"
      },
      {
        "nama": "WONOKROMO",
        "jam_datang": "04:48",
        "jam_berangkat": "04:50"
      },
      {
        "nama": "WARU",
        "jam_datang": "04:58",
        "jam_berangkat": "05:00"
      },
      {
        "nama": "GEDANGAN",
        "jam_datang": "05:06",
        "jam_berangkat": "05:08"
      },
      {
        "nama": "SIDOARJO",
        "jam_datang": "05:18",
        "jam_berangkat": "05:22"
      },
      {
        "nama": "TANGGULANGIN",
        "jam_datang": "05:29",
        "jam_berangkat": "05:36"
      },
      {
        "nama": "PORONG",
        "jam_datang": "05:40",
        "jam_berangkat": "05:47"
      },
      {
        "nama": "BANGIL",
        "jam_datang": "06:00",
        "jam_berangkat": "06:05"
      },
      {
        "nama": "WONOKERTO",
        "jam_datang": "Tidak Berhenti",
        "jam_berangkat": "Tidak Berhenti"
      },
      {
        "nama": "SUKOREJO",
        "jam_datang": "Tidak Berhenti",
        "jam_berangkat": "Tidak Berhenti"
      },
      {
        "nama": "SENGON",
        "jam_datang": "Tidak Berhenti",
        "jam_berangkat": "Tidak Berhenti"
      },
      {
        "nama": "LAWANG",
        "jam_datang": "06:39",
        "jam_berangkat": "06:42"
      },
      {
        "nama": "SINGOSARI",
        "jam_datang": "06:52",
        "jam_berangkat": "06:54"
      },
      {
        "nama": "BLIMBING",
        "jam_datang": "07:02",
        "jam_berangkat": "07:04"
      },
      {
        "nama": "MALANG",
        "jam_datang": "07:11",
        "jam_berangkat": "07:15"
      },
      {
        "nama": "MALANG KOTALAMA",
        "jam_datang": "07:21",
        "jam_berangkat": "07:23"
      },
      {
        "nama": "PAKISAJI",
        "jam_datang": "07:33",
        "jam_berangkat": "07:35"
      },
      {
        "nama": "KEPANJEN",
        "jam_datang": "07:44",
        "jam_berangkat": "07:56"
      },
      {
        "nama": "NGEBRUK",
        "jam_datang": "07:54",
        "jam_berangkat": "07:58"
      },
      {
        "nama": "SUMBERPUCUNG",
        "jam_datang": "08:02",
        "jam_berangkat": "08:04"
      },
      {
        "nama": "POGAJIH",
        "jam_datang": "08:14",
        "jam_berangkat": "08:16"
      },
      {
        "nama": "KESAMBEN",
        "jam_datang": "08:25",
        "jam_berangkat": "08:27"
      },
      {
        "nama": "WLINGIH",
        "jam_datang": "08:38",
        "jam_berangkat": "08:40"
      },
      {
        "nama": "TALUN",
        "jam_datang": "08:46",
        "jam_berangkat": "08:48"
      },
      {
        "nama": "GARUM",
        "jam_datang": "08:58",
        "jam_berangkat": "09:00"
      },
      {
        "nama": "BLITAR",
        "jam_datang": "09:10",
        "jam_berangkat": "09:35"
      }
    ]
  },
  {
    "name": "KERETA API PROBOWANGGI",
    "name_code": "SURABAYA-KETAPANG",
    "type": "antar_kota",
    "total_gerbong": 5,
    "total_chair": 36,
    "stasiun": [
      {
        "nama": "SURABAYA GUBENG",
        "jam_datang": "04:25",
        "jam_berangkat": "05:35"
      },
      {
        "nama": "WONOKROMO",
        "jam_datang": "05:42",
        "jam_berangkat": "05:48"
      },
      {
        "nama": "WARU",
        "jam_datang": "05:55",
        "jam_berangkat": "05:57"
      },
      {
        "nama": "SIDOARJO KOTA",
        "jam_datang": "06:10",
        "jam_berangkat": "06:16"
      },
      {
        "nama": "BANGIL",
        "jam_datang": "06:38",
        "jam_berangkat": "06:44"
      },
      {
        "nama": "PASURUAN",
        "jam_datang": "07:02",
        "jam_berangkat": "07:04"
      },
      {
        "nama": "GRATI",
        "jam_datang": "TIDAK BERHENTI",
        "jam_berangkat": "TIDAK BERHENTI"
      },
      {
        "nama": "PROBOLINGGO",
        "jam_datang": "07:49",
        "jam_berangkat": "08:01"
      },
      {
        "nama": "LECES",
        "jam_datang": "TIDAK BERHENTI",
        "jam_berangkat": "TIDAK BERHENTI"
      },
      {
        "nama": "KLAKAH",
        "jam_datang": "08:36",
        "jam_berangkat": "08:38"
      },
      {
        "nama": "TANGGUL",
        "jam_datang": "09:10",
        "jam_berangkat": "09:12"
      },
      {
        "nama": "RAMBIPUJI",
        "jam_datang": "09:34",
        "jam_berangkat": "09:44"
      },
      {
        "nama": "JEMBER",
        "jam_datang": "09:57",
        "jam_berangkat": "10:05"
      },
      {
        "nama": "KALISAT",
        "jam_datang": "10:24",
        "jam_berangkat": "10:32"
      },
      {
        "nama": "KALIBARU",
        "jam_datang": "11:17",
        "jam_berangkat": "11:21"
      },
      {
        "nama": "BANYUWANGI KOTA",
        "jam_datang": "12:28",
        "jam_berangkat": "12:30"
      },
      {
        "nama": "KETAPANG",
        "jam_datang": "12:45",
        "jam_berangkat": "13:00"
      }
    ]
  },
  {
    "name": "KERETA API PROBOWANGGI",
    "name_code": "KETAPANG-SURABAYA",
    "type": "antar_kota",
    "total_gerbong": 5,
    "total_chair": 36,
    "stasiun": [
      {
        "nama": "SURABAYA GUBENG",
        "jam_datang": "23:10",
        "jam_berangkat": "23:40"
      },
      {
        "nama": "WONOKROMO",
        "jam_datang": "22:55",
        "jam_berangkat": "23:05"
      },
      {
        "nama": "WARU",
        "jam_datang": "22:45",
        "jam_berangkat": "22:50"
      },
      {
        "nama": "SIDOARJO KOTA",
        "jam_datang": "22:25",
        "jam_berangkat": "22:30"
      },
      {
        "nama": "BANGIL",
        "jam_datang": "21:33",
        "jam_berangkat": "21:37"
      },
      {
        "nama": "PASURUAN",
        "jam_datang": "21:13",
        "jam_berangkat": "21:15"
      },
      {
        "nama": "GRATI",
        "jam_datang": "TIDAK BERHENTI",
        "jam_berangkat": "TIDAK BERHENTI"
      },
      {
        "nama": "PROBOLINGGO",
        "jam_datang": "20:33",
        "jam_berangkat": "20:38"
      },
      {
        "nama": "LECES",
        "jam_datang": "TIDAK BERHENTI",
        "jam_berangkat": "TIDAK BERHENTI"
      },
      {
        "nama": "KLAKAH",
        "jam_datang": "19:55",
        "jam_berangkat": "19:59"
      },
      {
        "nama": "TANGGUL",
        "jam_datang": "19:12",
        "jam_berangkat": "19:14"
      },
      {
        "nama": "RAMBIPUJI",
        "jam_datang": "18:50",
        "jam_berangkat": "18:52"
      },
      {
        "nama": "JEMBER",
        "jam_datang": "18:30",
        "jam_berangkat": "18:38"
      },
      {
        "nama": "KALISAT",
        "jam_datang": "18:02",
        "jam_berangkat": "18:11"
      },
      {
        "nama": "KALIBARU",
        "jam_datang": "17:15",
        "jam_berangkat": "17:17"
      },
      {
        "nama": "BANYUWANGI KOTA",
        "jam_datang": "16:14",
        "jam_berangkat": "16:16"
      },
      {
        "nama": "KETAPANG",
        "jam_datang": "15:50",
        "jam_berangkat": "16:10"
      }
    ]
  }
]

def encode_md5(input_string):
    # Mengonversi string menjadi byte
    byte_string = input_string.encode('utf-8')
    
    # Membuat objek hash MD5
    md5_hash = hashlib.md5()
    
    # Mengupdate hash dengan byte string
    md5_hash.update(byte_string)
    
    # Mendapatkan hash dalam format hexademisal
    encoded_string = md5_hash.hexdigest()
    
    return encoded_string

def parse_time(time_str):
    try:
        hasil_jam = datetime.strptime(time_str, '%H:%M').time()
        return hasil_jam
    except Exception as e:
        return None

def empty_action():
    # Kosongkang Database
    session.query(Action).delete()
    session.commit()

def seed_user():
    # Kosongkang Database
    session.query(User).delete()
    session.commit()
    session.query(UserSchedule).delete()
    session.commit()

    # Insert User
    new_user = User(username="admin", password=encode_md5("123456"), created_at=datetime.now().date())
    session.add(new_user)
    session.commit()

    print("Seeding data berhasil.")

def seed_train():
    # Kosongkang Database
    session.query(Train).delete()
    session.commit()
    session.query(TrainSchedule).delete()
    session.commit()
    for schedule in train_schedules:
        # Insert Train
        new_train = Train(name=schedule['name'], name_code=schedule['name_code'], type=schedule['type'], total_gerbong=schedule["total_gerbong"], total_chair=schedule["total_chair"], created_at=datetime.now().date())
        session.add(new_train)
        session.commit()
        for station in schedule['stasiun']:
            # Insert Train Schedule
            new_train_schedule = TrainSchedule(train_id=new_train.id, station=station['nama'], arrival=parse_time(station['jam_datang']), departure=parse_time(station['jam_berangkat']), created_at=datetime.now().date())
            session.add(new_train_schedule)
            session.commit()

    print("Seeding data berhasil.")



# Panggil fungsi seed_data untuk menambahkan data ke dalam tabel
empty_action()
seed_user()
seed_train()



# Tutup sesi setelah selesai
session.close()
