import datetime
from pathlib import Path
import json
import base64

#--XỬ LÝ LƯU TRỮ
thuMucDuLieu = Path("./Du_lieu")
thuMucCongTy = thuMucDuLieu/"Cong_ty"
thuMucHTML = thuMucDuLieu/"HTML"
thuMucNhanVien = thuMucDuLieu/"Nhan_vien"

# CAC HAM XU LY LUU TRU 
#-----Doc khung html
def docKhungHTML():
        chuoiHTML = ""       
        duongDan = thuMucHTML/"Khung.html"
        chuoiHTML = duongDan.read_text("utf-8")        
        return chuoiHTML
#-----Doc Cong ty
def Doc_Cong_ty():
  Duong_dan = thuMucCongTy/"Cong_ty.json"
  Chuoi_Json = Duong_dan.read_text("utf-8")
  Cong_ty = json.loads(Chuoi_Json)
  return Cong_ty
#----Doc Danh sach nhan vien 
def Doc_Danh_sach_Nhan_vien():
    Danh_sach_Nhan_vien = []
    for Duong_dan in thuMucNhanVien.glob("*.json"):
        Chuoi_Json = Duong_dan.read_text("utf-8")
        nv = json.loads(Chuoi_Json)
        Danh_sach_Nhan_vien.append(nv)
    return Danh_sach_Nhan_vien
#---Ghi thong tin cap nhat
def Ghi_Nhan_vien(Nhan_vien):     
   Duong_dan = thuMucNhanVien/f'''{Nhan_vien["Ma_so"]}.json'''
   Chuoi_JSON = json.dumps(Nhan_vien,ensure_ascii=False, indent=1)
   Tap_tin = open(Duong_dan,'w', encoding='utf-8')
   Tap_tin.write(Chuoi_JSON)
   Tap_tin.close()
#---Ghi Hình Nhân viên
def Ghi_Hinh_Nhan_vien(Nhan_vien, Hinh):
  Duong_dan = f'''Media/{Nhan_vien["Ma_so"]}.png''' 
  Hinh_bytes = Hinh.encode('utf-8')
  decoded_image_data = base64.decodebytes(Hinh_bytes)
  with open(Duong_dan, 'wb') as Hinh_moi: 
    Hinh_moi.write(decoded_image_data)
    Hinh_moi.close()
  
      



  
