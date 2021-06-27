from flask import Flask, request,jsonify
from flask.globals import session
from JSON_XL_3L import*

#--THẦY ƠI, DO DUNG LƯỢNG TẬP TIN VƯỢT QUÁ 10M, EM BỎ FOLDER ENVIROMENT FLASK,
#  KHI CHẠY THẦY CÀI LẠI GIÚP EM. CẢM ƠN THẦY!

DichVu = Flask(__name__, static_url_path="/Media", static_folder="Media")
DichVu.secret_key = "QuocNguyenViet" 

#--EndPoint khởi động
@DichVu.route("/Doc_Khung_HTML", methods = ["POST"])
def XL_Doc_Khung_HTML(): 
    Doi_tuong_A = request.get_json() 
    Doi_tuong_B = {'Kq': 'OK'}
    Doi_tuong_B['Chuoi_HTML'] = docKhungHTML()   
    return jsonify(Doi_tuong_B)
#--EndPoit /Doc_Cong_ty
@DichVu.route("/Doc_Cong_ty", methods =["POST"])
def XL_Doc_Cong_ty():
    Doi_tuong_A = request.get_json() 
    Doi_tuong_B = {'Kq': 'OK'}
    Doi_tuong_B['Cong_ty'] = Doc_Cong_ty()     
    return jsonify(Doi_tuong_B)
#--Endpoint /Doc_Danh_sach_Nhan_vien
@DichVu.route("/Doc_Danh_sach_Nhan_vien", methods=["POST"])
def XL_Doc_Danh_sach_Nhan_vien():
    Doi_tuong_A = request.get_json()
    Doi_tuong_B = {'Kq': 'OK'}
    Doi_tuong_B["Danh_sach_Nhan_vien"] = Doc_Danh_sach_Nhan_vien()
    return jsonify(Doi_tuong_B)
#--Endpoint /Ghi_Nhan_vien
@DichVu.route("/Ghi_Nhan_vien", methods=["POST"])
def XL_Ghi_Nhan_vien():
    Doi_tuong_A = request.get_json()
    Nhan_vien = Doi_tuong_A["Nhan_vien"]
    Ghi_Nhan_vien(Nhan_vien)
    Doi_tuong_B = {'Kq': 'OK'}   
    return jsonify(Doi_tuong_B)
#--Endpoint /Ghi_Hinh_Nhan_vien
@DichVu.route("/Ghi_Hinh_Nhan_vien", methods=["POST"])
def XL_Ghi_Hinh_Nhan_vien():
    Doi_tuong_A = request.get_json()
    Nhan_vien = Doi_tuong_A["Nhan_vien"]
    Hinh = Doi_tuong_A["Hinh"]     
    Ghi_Hinh_Nhan_vien(Nhan_vien, Hinh)
    Doi_tuong_B = {'Kq': 'OK'}   
    return jsonify(Doi_tuong_B)
#--Xóa cache browser
@DichVu.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


#--Run chuong trinh
if __name__ == '__main__':
   DichVu.run()
