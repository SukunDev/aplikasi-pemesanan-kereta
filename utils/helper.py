import hashlib
from datetime import datetime, timedelta


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


def get_days():
    tanggal_hari_ini = datetime.now().date()
    tanggal_list = []
    for i in range(10):
        tanggal_list.append(tanggal_hari_ini + timedelta(days=i))

    return tanggal_list
