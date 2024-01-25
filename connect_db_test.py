import pymongo

# Thay thế URI bằng thông tin kết nối MongoDB Atlas của bạn
client = pymongo.MongoClient("mongodb+srv://pknstudio2704:nguyenitdev270440@cluster0.xafk9pw.mongodb.net/SGUETNews?retryWrites=true&w=majority")

# Kiểm tra kết nối thành công và in thông báo
if client:
    print("Kết nối MongoDB Atlas thành công!")
else:
    print("Kết nối MongoDB Atlas không thành công!")

# Đóng kết nối đến MongoDB Atlas
client.close()
