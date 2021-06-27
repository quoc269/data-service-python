import json 
import glob
import sqlite3
import base64
from pathlib import Path

Ten_CSDL = "QLNV.sqlite"
Thu_Muc_Du_lieu = "./Du_lieu"
Duong_dan_CSDL = f'''{Thu_Muc_Du_lieu}/{Ten_CSDL}'''

#-----Doc khung html
def docKhungHTML():
    thuMucDuLieu = Path("./Du_lieu")
    thuMucHTML = thuMucDuLieu/"HTML"
    chuoiHTML = ""       
    duongDan = thuMucHTML/"Khung.html"
    chuoiHTML = duongDan.read_text("utf-8")        
    return chuoiHTML
#-----Doc cong ty
def Doc_Cong_ty():
    Cong_ty = {}
    Ket_noi = sqlite3.connect(Duong_dan_CSDL)
    Lenh = "SELECT * FROM CONG_TY"
    for Dong in Ket_noi.execute(Lenh) :
        Chuoi_JSON = Dong[1]
        Cong_ty = json.loads(Chuoi_JSON)
    Ket_noi.close()
    return Cong_ty
#----Doc Danh sach Nhan vien
def Doc_Danh_sach_Nhan_vien():
    Danh_sach_Nhan_vien =[]
    Ket_noi = sqlite3.connect(Duong_dan_CSDL)
    Lenh = "SELECT * FROM NHAN_VIEN"
    for Dong in Ket_noi.execute(Lenh):
        Chuoi_JSON = Dong[1]
        Nhan_vien = json.loads(Chuoi_JSON)
        Danh_sach_Nhan_vien.append(Nhan_vien)
    Ket_noi.close()
    return Danh_sach_Nhan_vien
#----Ghi nhan vien 
def Ghi_Nhan_vien(Nhan_vien): 
    Ket_noi = sqlite3.connect(Duong_dan_CSDL)
    Ma_so = Nhan_vien['Ma_so']
    Chuoi_JSON = json.dumps(Nhan_vien)
    Lenh = f"UPDATE NHAN_VIEN set Chuoi_JSON = '{Chuoi_JSON}' where Ma_so = '{Ma_so}'"
    Ket_noi.execute(Lenh)
    Ket_noi.commit()
    Ket_noi.close()
#----Ghi Hinh Nhan vien
def Ghi_Hinh_Nhan_vien(Nhan_vien, Hinh):
    Duong_dan = f'''Media/{Nhan_vien["Ma_so"]}.png''' 
    Hinh_bytes = Hinh.encode('utf-8')
    Decoded_Hinh_bytes = base64.decodebytes(Hinh_bytes)
    with open(Duong_dan, 'wb') as Hinh_moi: 
        Hinh_moi.write(Decoded_Hinh_bytes)
        Hinh_moi.close()



        






