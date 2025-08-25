🍄 Mushroom Classification Web App
📌 Giới thiệu

Mushroom Classification Web App là một ứng dụng web đơn giản nhưng trực quan, được thiết kế để dự đoán xem một loại nấm là ăn được hay độc hại dựa trên một số đặc trưng cơ bản. Ứng dụng này minh họa cách kết hợp giữa mô hình học máy (Machine Learning) và web framework Flask, nhằm mang lại trải nghiệm trực tiếp cho người dùng mà không cần kiến thức chuyên sâu về lập trình hay trí tuệ nhân tạo.

Ứng dụng lấy cảm hứng từ nhu cầu phân loại nấm trong tự nhiên – một chủ đề vừa thú vị vừa thiết thực, khi có nhiều loài nấm có hình dáng gần giống nhau nhưng mức độ an toàn lại rất khác biệt.

🔎 Chức năng chính

Ứng dụng cho phép người dùng lựa chọn các đặc điểm của nấm thông qua biểu mẫu trên giao diện web, bao gồm:

Mùi (odor) – đặc trưng về hương thơm, có thể là thơm, khó chịu hoặc không mùi.

Màu mũ nấm (cap-color) – màu sắc của phần mũ, chẳng hạn như nâu, đỏ, vàng, trắng,…

Màu phiến nấm (gill-color) – màu của các phiến dưới mũ nấm, giúp phân biệt rõ hơn giữa các loài.

Dựa trên các thông tin mà người dùng cung cấp, mô hình cây quyết định đã huấn luyện sẵn sẽ đưa ra kết quả:

🍄 Edible → Nấm ăn được, an toàn

☠️ Poisonous → Nấm độc, nguy hiểm

⚠️ Unknown → Không thể xác định với dữ liệu hiện có

✨ Giao diện người dùng

Giao diện web được thiết kế dựa trên Bootstrap 5, mang lại sự gọn gàng, dễ nhìn và tương thích tốt trên cả máy tính và thiết bị di động. Người dùng chỉ cần chọn giá trị từ các hộp chọn (dropdown) và nhấn nút “Dự đoán”. Ngay sau đó, kết quả sẽ hiển thị rõ ràng với biểu tượng trực quan (🍄, ☠️, ⚠️).

Điểm nhấn của ứng dụng nằm ở sự đơn giản và dễ sử dụng: chỉ vài thao tác cơ bản, người dùng đã có thể trải nghiệm một mô hình học máy chạy trực tiếp trên nền web.

⚙️ Công nghệ sử dụng

Python 3 – ngôn ngữ lập trình chính để xây dựng ứng dụng.

Flask – framework nhẹ cho web backend, xử lý request/response và render giao diện.

Bootstrap 5 – hỗ trợ xây dựng giao diện đẹp, responsive và thân thiện với người dùng.

Pickle – thư viện Python dùng để lưu trữ và tải lại mô hình cây quyết định đã huấn luyện.

Decision Tree Model – mô hình học máy đơn giản, trực quan, phù hợp cho bài toán phân loại nấm.

🎯 Ý nghĩa và Ứng dụng

Mặc dù ứng dụng không nhằm mục đích sử dụng trong thực tế để xác định nấm ăn được ngoài tự nhiên (do vấn đề an toàn sinh học), nhưng nó mang lại những giá trị quan trọng:

Minh họa học thuật – Đây là ví dụ điển hình cho việc áp dụng Machine Learning vào một ứng dụng web trực quan.

Thực hành kỹ năng lập trình – Người học có thể làm quen với quy trình: huấn luyện mô hình → lưu mô hình → tích hợp vào Flask → triển khai web app.

Trực quan hóa kết quả – Thay vì chạy mô hình trong terminal khô khan, ứng dụng này giúp kết quả hiển thị sinh động và dễ hiểu hơn.

Mở rộng nghiên cứu – Cấu trúc ứng dụng có thể dễ dàng mở rộng thêm các thuộc tính khác của nấm hoặc thay đổi sang mô hình Machine Learning khác (Random Forest, SVM, Neural Network).

