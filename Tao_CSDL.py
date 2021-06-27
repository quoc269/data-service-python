from JSON_XL_3L import*
import sqlite3

Ten_CSDL = "QLNV.sqlite"
Thu_Muc_Du_lieu = "./Du_lieu"
Duong_dan_CSDL = f'''{Thu_Muc_Du_lieu}/{Ten_CSDL} '''

def Tao_Cau_truc_CSDL_QLNV():
    Ket_noi = sqlite3.connect(Duong_dan_CSDL)    
    Lenh = "CREATE TABLE if not exists NHAN_VIEN(Ma_so,Chuoi_JSON)"
    Ket_noi.execute(Lenh)
    Lenh = "CREATE TABLE if not exists CONG_TY(Ma_so,Chuoi_JSON)"    
    Ket_noi.execute(Lenh)
    Ket_noi.commit()
    Ket_noi.close()

def Chuyen_Du_lieu_CSDL_QLNV():
    Ket_noi = sqlite3.connect(Duong_dan_CSDL)
    Danh_sach_Nhan_vien = Doc_Danh_sach_Nhan_vien()
    for Nhan_vien in Danh_sach_Nhan_vien:
        Ma_so = Nhan_vien['Ma_so']
        Chuoi_JSON = json.dumps(Nhan_vien)
        Lenh = f'''INSERT INTO NHAN_VIEN VALUES('{Ma_so}', '{Chuoi_JSON}')'''
        Ket_noi.execute(Lenh)
        Ket_noi.commit()
    Cong_ty = Doc_Cong_ty()
    Ma_so = Cong_ty['Ma_so']
    Chuoi_JSON = json.dumps(Cong_ty)
    Lenh = f'''INSERT INTO CONG_TY VALUES('{Ma_so}', '{Chuoi_JSON}')'''
    Ket_noi.execute(Lenh)
    Ket_noi.commit()
    Ket_noi.close()

Tao_Cau_truc_CSDL_QLNV()
Chuyen_Du_lieu_CSDL_QLNV()





