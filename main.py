from subprocess import call


def open_my_file(fileOpen):
    call(["python", fileOpen])


from streamlit_option_menu import option_menu
import streamlit as st
import NhanDangKhuonMat.Buoc1.get_face as get_face
import NhanDangKhuonMat.Buoc3.predict as predict
import XuLyAnhSo.XyLyAnh as xulyanh



class Main():
    def __init__(self):
        self.initUI()

    def initUI(self):
        with st.sidebar:
            st.sidebar.header = "Menu"
            selected = option_menu("Trang chủ", ["Nhận dạng khuôn mặt", "Phát hiện khuôn mặt", "Xử lý hình ảnh"],
                                   icons=['person lines fill', 'book', 'camera fill'], menu_icon="grid-1x2-fill", default_index=0)

        if selected == "Nhận dạng khuôn mặt":
            st.title("Nhận dạng khuôn mặt")
            col1, col2 = st.columns([0.5, 0.5], gap="large")
            st.write("Nhận diện khuôn mặt qua model đã train")
            predict.runPredict()

        if selected == "Xử lý hình ảnh":
            # Chọn thông tin file image
            uploaded_files = st.sidebar.file_uploader("Chọn file image", type=['csv', 'png', 'tif', 'jpg'])
            # Gọi hàm thực thi xử lý tính năng
            xulyanh.XuLyUploadFile(uploaded_files)
        
        if selected == "Phát hiện khuôn mặt":
            st.title("Phát hiện khuôn mặt")
            col1, col2 = st.columns([0.5, 0.5], gap="large")
            st.write("Phát hiện khuôn mặt thông qua camera")
            get_face.runGetFace()

p = Main()
