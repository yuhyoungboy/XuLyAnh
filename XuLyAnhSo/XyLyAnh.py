import numpy as np
import cv2
import streamlit as st
import XuLyAnhSo.Chuong3 as chuong3
import XuLyAnhSo.Chuong4 as chuong4
import XuLyAnhSo.Chuong9 as chuong9

# Thiết lập hàm xử lý ảnh chương 3
def XuLyAnh_Chuong3(name_type, image_in):
    chuong3_Title = ''
    image_title = ''
    image_out = np.empty

    # Thiết lập image_out
    try:
        image_out = np.zeros(image_in.shape, np.uint8)
    except:
        except_Title = '<p style="font-family: Georgia; color: #ffff00; font-size: 40px; font-weight: bold; text-align: center;">Hình ảnh không thích hợp</p>'
        st.markdown(except_Title, unsafe_allow_html=True)
        return

    # Kiểm tra name_type tính năng nào được xử lý
    if name_type == 'Negative':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 1 _ Negative</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Negative: Hàm làm âm ảnh. Kết quả hàm âm ảnh: Trắng thành đen, đen thành trắng</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Negative(image_in, image_out)
    elif name_type == 'Logarit':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 2 _ Logarit</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Logarit: Hàm xử lý ảnh bằng phương pháp Logarit. Kết quả hàm Logarit: Sáng ít thì làm cho sáng nhiều, Đen nhiều thì thành đen ít</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Logarit(image_in, image_out)
    elif name_type == 'Power':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 3 _ Power</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Power: Hàm xử lý ảnh bằng phương pháp lũy thừa ảnh. Kết quả hàm Power: Làm cho ảnh trở trên tối hơn, hay sáng hơn đều được</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Power(image_in, image_out)
    elif name_type == 'PiecewiseLinear':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 4 _ PiecewiseLinear</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng PiecewiseLinear: Hàm xử lý ảnh bằng phương pháp Piecewise. Kết quả hàm PiecewiseLinear: Kéo dài độ tương phản, phạm vi mức cường độ làm sáng hơn</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.PiecewiseLinear(image_in, image_out)
    elif name_type == 'Histogram':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 5 _ Histogram</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng HistogramEqualization: Hàm xử lý ảnh bằng phương pháp Histogram. Kết quả biểu Histogram: là dạng biểu đồ thể hiện tần suất theo dạng cột theo dữ liệu tương ứng, làm cho ảnh đẹp hơn</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Histogram(image_in, image_out)
    elif name_type == 'HistogramEqualization':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 6 _ HistogramEqualization</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng HistogramEqualization: Hàm xử lý ảnh bằng phương pháp HistogramEqualization. Kết quả biểu HistogramEqualization: là dạng biểu đồ thể hiện tần suất theo dạng cột theo dữ liệu tương ứng, làm cho ảnh đẹp hơn, hàm HistogramEqualization tốt hơn Histogram</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.HistogramEqualization(image_in, image_out)
    elif name_type == 'LocalHistogram':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 7 _ LocalHistogram</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng LocalHistogram: Hàm xử lý ảnh bằng phương pháp LocalHistogram. Kết quả hàm LocalHistogram: Làm rõ 1 vùng trong ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.LocalHistogram(image_in, image_out)
    elif name_type == 'HistogramStatistics':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 8 _ HistogramStatistics</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng HistogramStatistics: Hàm xử lý ảnh bằng phương pháp HistogramStatistics. Kết quả hàm HistogramStatistics: Thống kê 1 vùng trong ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.HistogramStatistics(image_in, image_out)
    elif name_type == 'Smoothing':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 9 _ Smoothing</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Smoothing: Hàm xử lý ảnh bằng phương pháp Smoothing. Kết quả hàm Smoothing: Làm trơn, làm nhòe ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Smoothing(image_in)
    elif name_type == 'SmoothingGauss':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 10 _ SmoothingGauss</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng SmoothingGauss: Hàm xử lý ảnh bằng phương pháp SmoothingGauss. Kết quả hàm SmoothingGauss: Làm trơn, làm nhòe ảnh. Thuật toán SmoothingGauss tốt hơn thuật toán Smooth cơ bản</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.SmoothingGauss(image_in)
    elif name_type == 'MedianFilter':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 11 _ MedianFilter</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng MedianFilter: Hàm xử lý ảnh bằng phương pháp MedianFilter. Kết quả hàm MedianFilter: Lọc nhiễu ảnh, lọc các điểm nhiễu ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.MedianFilter(image_in, image_out)
    elif name_type == 'Sharpen':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 12 _ Sharpen</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Sharpen: Hàm xử lý ảnh bằng phương pháp Sharpen. Kết quả hàm Sharpen: Làm nét, bén nhọn các góc của ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Sharpen(image_in)
    elif name_type == 'UnSharpMasking':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 13 _ UnSharpMasking</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng UnSharpMasking: Hàm xử lý ảnh bằng phương pháp UnSharpMasking. Kết quả hàm UnSharpMasking: Làm nét ảnh bằng phương pháp UnSharpMasking</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.UnSharpMasking(image_in)
    elif name_type == 'Gradient':
        # Thiết lập tiêu đề
        chuong3_Title = '<p style="font-family: Georgia; color: #40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 14 _ Gradient</p>'
        st.markdown(chuong3_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong3_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng Gradient: Hàm xử lý ảnh bằng phương pháp Gradient. Kết quả hàm Gradient: Đạo hàm ống kính tách biên của ảnh</p>'
        st.markdown(chuong3_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong3.Gradient(image_in)

    # Hiển thị thông tin image_in
    image_title = '<p style="font-family: Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;"> Hình trước khi thay đổi : </p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_in, width=300)

    # Hiển thị thông tin image_out
    image_title = '<p style="font-family:Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;">Hình sau khi thay đổi :</p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_out, width=300)


# Thiết lập hàm xử lý ảnh chương 4
def XuLyAnh_Chuong4(name_type, image_in):
    chuong4_Title = ''
    image_title = ''
    image_out = np.empty

    # Thiết lập image_out
    try:
        image_out = np.zeros(image_in.shape, np.uint8)
    except:
        except_Title = '<p style="font-family: Georgia; color: #4A235A; font-size: 40px; font-weight: bold; text-align: center;">Hình ảnh không thực hiện chuyển đổi được</p>'
        st.markdown(except_Title, unsafe_allow_html=True)
        return

    # Kiểm tra name_type tính năng nào được xử lý
    if name_type == 'Spectrum':
        # Thiết lập tiêu đề
        chuong4_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 1 _ Spectrum</p>'
        st.markdown(chuong4_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong4_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;;">Xử lý ảnh bằng Spectrum: Hàm xử lý ảnh bằng phương pháp Spectrum. Kết quả hàm Spectrum: Xử lý quang phổ bằng các công thức tần số sóng điện từ, ánh sánh, điểm ảnh</p>'
        st.markdown(chuong4_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong4.Spectrum(image_in)
    elif name_type == 'FrequencyFilter':
        # Thiết lập tiêu đề
        chuong4_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 2 _ FrequencyFilter</p>'
        st.markdown(chuong4_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong4_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng FrequencyFilter: Hàm xử lý ảnh bằng phương pháp FrequencyFilter. Kết quả hàm FrequencyFilter: Bộ lọc cho tín hiệu có tần số thấp hơn tần số cắt đã chọn và làm suy giảm tín hiệu có tần số cao hơn tần số cắt để xử lý ảnh</p>'
        st.markdown(chuong4_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong4.FrequencyFilter(image_in)
    elif name_type == 'DrawFilter':
        # Thiết lập tiêu đề
        chuong4_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 3 _ DrawFilter</p>'
        st.markdown(chuong4_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong4_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng DrawFilter: Hàm xử lý ảnh bằng phương pháp DrawFilter. Kết quả hàm DrawFilter: Xử lý lọc ảnh cơ bản</p>'
        st.markdown(chuong4_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong4.DrawFilter(image_in)
    elif name_type == 'RemoveMoire':
        # Thiết lập tiêu đề
        chuong4_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 4 _ RemoveMoire</p>'
        st.markdown(chuong4_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong4_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng RemoveMoire: Hàm xử lý ảnh bằng phương pháp Moire. Kết quả hàm RemoveMoire: Xóa các điểm nhiễu ảnh</p>'
        st.markdown(chuong4_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong4.RemoveMoire(image_in)

    # Hiển thị thông tin image_in
    image_title = '<p style="font-family: Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;">Hình trước khi thay đổi :</p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_in, width=300)

    # Hiển thị thông tin image_out
    image_title = '<p style="font-family:Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;">Hình sau khi thay đổi :</p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_out, width=300)


# Thiết lập hàm xử lý ảnh chương 9
def XuLyAnh_Chuong9(name_type, image_in):
    chuong9_Title = ''
    image_title = ''
    image_out = np.empty

    # Thiết lập image_out
    try:
        image_out = np.zeros(image_in.shape, np.uint8)
    except:
        except_Title = '<p style="font-family: Georgia; color: #4A235A; font-size: 40px; font-weight: bold; text-align: center;">Hình ảnh không thực hiện chuyển đổi được</p>'
        st.markdown(except_Title, unsafe_allow_html=True)
        return

    # Kiểm tra name_type tính năng nào được xử lý
    if name_type == 'ConnectedComponent':
        # Thiết lập tiêu đề
        chuong9_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 1 _ ConnectedComponent</p>'
        st.markdown(chuong9_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong9_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng ConnectedComponent: Hàm xử lý ảnh bằng phương pháp ConnectedComponent. Kết quả hàm ConnectedComponent: Thành phần liên thông, đếm có bao nhiêu miếng xương gà, tách ảnh</p>'
        st.markdown(chuong9_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong9.ConnectedComponent(image_in)
    elif name_type == 'CountRice':
        # Thiết lập tiêu đề
        chuong9_Title = '<p style="font-family: Georgia; color:#40E0D0; font-size: 40px; font-weight: bold; text-align: center;">Câu 2 _ CountRice</p>'
        st.markdown(chuong9_Title, unsafe_allow_html=True)
        # Thiết lập nội dung
        chuong9_Content = '<p style="font-family: Times; color: #FF6347; font-size: 20px; text-align: justify;">Xử lý ảnh bằng CountRice: Hàm xử lý ảnh bằng phương pháp CountRice. Kết quả hàm CountRice: Đếm có bao nhiêu hạt gạo</p>'
        st.markdown(chuong9_Content, unsafe_allow_html=True)
        # Gọi hàm xử lý
        image_out = chuong9.CountRice(image_in)

    # Hiển thị thông tin image_in
    image_title = '<p style="font-family: Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;">Hình trước khi thay đổi :</p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_in, width=300)

    # Hiển thị thông tin image_out
    image_title = '<p style="font-family:Georgia; color: #FFFF14; font-size: 20px; font-weight: bold;">Hình sau khi thay đổi :</p>'
    st.markdown(image_title, unsafe_allow_html=True)
    st.image(image_out, width=300)


# Thiết lập hàm xử lý Upload File
def XuLyUploadFile(uploaded_files):
    # Kiểm tra file đã được upload rồi mới thực hiện các bước tiếp theo
    if uploaded_files is not None:
        # Thiết lập menu thành phần khi cho file ảnh
        menu_item = st.sidebar.selectbox('Chọn Chương', ['Chương 3', 'Chương 4', 'Chương 9'])

        # Kiểm tra nếu selectbox value là "Chương 3"
        if menu_item == 'Chương 3':
            # Thiết lập image_in
            filepath = 'HinhAnh//Chuong3//' + uploaded_files.name
            image_in = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

            # Thiết lập menu phương thức xử lý ảnh
            chuong3_menu_function = st.sidebar.radio("Các phương pháp xử lý ảnh C3",
                                                     ('Negative', 'Logarit', 'Power', 'PiecewiseLinear', 'Histogram',
                                                      'HistogramEqualization', 'LocalHistogram', 'HistogramStatistics',
                                                      'Smoothing', 'SmoothingGauss', 'MedianFilter', 'Sharpen',
                                                      'UnSharpMasking', 'Gradient'))

            # Kiểm tra radio là tính năng chương 3
            if chuong3_menu_function == 'Negative':
                XuLyAnh_Chuong3('Negative', image_in)
            elif chuong3_menu_function == 'Logarit':
                XuLyAnh_Chuong3('Logarit', image_in)
            elif chuong3_menu_function == 'Power':
                XuLyAnh_Chuong3('Power', image_in)
            elif chuong3_menu_function == 'PiecewiseLinear':
                XuLyAnh_Chuong3('PiecewiseLinear', image_in)
            elif chuong3_menu_function == 'Histogram':
                XuLyAnh_Chuong3('Histogram', image_in)
            elif chuong3_menu_function == 'HistogramEqualization':
                XuLyAnh_Chuong3('HistogramEqualization', image_in)
            elif chuong3_menu_function == 'LocalHistogram':
                XuLyAnh_Chuong3('LocalHistogram', image_in)
            elif chuong3_menu_function == 'HistogramStatistics':
                XuLyAnh_Chuong3('HistogramStatistics', image_in)
            elif chuong3_menu_function == 'Smoothing':
                XuLyAnh_Chuong3('Smoothing', image_in)
            elif chuong3_menu_function == 'SmoothingGauss':
                XuLyAnh_Chuong3('SmoothingGauss', image_in)
            elif chuong3_menu_function == 'MedianFilter':
                XuLyAnh_Chuong3('MedianFilter', image_in)
            elif chuong3_menu_function == 'Sharpen':
                XuLyAnh_Chuong3('Sharpen', image_in)
            elif chuong3_menu_function == 'UnSharpMasking':
                XuLyAnh_Chuong3('UnSharpMasking', image_in)
            elif chuong3_menu_function == 'Gradient':
                XuLyAnh_Chuong3('Gradient', image_in)

        elif menu_item == 'Chương 4':
            # Thiết lập image_in
            filepath = 'HinhAnh//Chuong4//' + uploaded_files.name
            image_in = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

            # Thiết lập menu phương thức xử lý ảnh
            chuong4_menu_function = st.sidebar.radio("Các phương pháp xử lý ảnh C4",
                                                     ('Spectrum', 'FrequencyFilter', 'DrawFilter', 'RemoveMoire'))

            # Kiểm tra radio là tính năng chương 4
            if chuong4_menu_function == 'Spectrum':
                XuLyAnh_Chuong4('Spectrum', image_in)
            elif chuong4_menu_function == 'FrequencyFilter':
                XuLyAnh_Chuong4('FrequencyFilter', image_in)
            elif chuong4_menu_function == 'DrawFilter':
                XuLyAnh_Chuong4('DrawFilter', image_in)
            elif chuong4_menu_function == 'RemoveMoire':
                XuLyAnh_Chuong4('RemoveMoire', image_in)

        elif menu_item == 'Chương 9':
            # Thiết lập image_in
            filepath = 'HinhAnh//Chuong9//' + uploaded_files.name
            image_in = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

            # Thiết lập menu phương thức xử lý ảnh
            chuong9_menu_function = st.sidebar.radio("Các phương pháp xử lý ảnh C9",
                                                     ('ConnectedComponent',
                                                      'CountRice'))

            # Kiểm tra radio là tính năng chương 9
            if chuong9_menu_function == 'ConnectedComponent':
                XuLyAnh_Chuong9('ConnectedComponent', image_in)
            elif chuong9_menu_function == 'CountRice':
                XuLyAnh_Chuong9('CountRice', image_in)

    else:
        cau1_Title = '<p style="font-family: Times New Roman; color: #6E2C00; font-size: 40px; font-weight: bold; text-align: center;">Chọn hình ảnh</p>'
        st.markdown(cau1_Title, unsafe_allow_html=True)