header = "|{:^10}|{:^15}|{:^20}|{:^15}|{:^10}|{:^15}|{:^15}|{:^20}|".format(
    "MA KHO", "TEN KHO", "DIA DIEM", "TAI TRONG(KG)", "LOAI", "DATE NHAP", "DATE XUAT", "TAI TRONG NHAP(KG)"
)

row = "#{:-^10}#{:-^15}#{:-^20}#{:-^15}#{:-^10}#{:-^15}#{:-^15}#{:-^20}#".format("", "", "", "", "", "", "", "")

class Date:
	"""docstring for Date"""
	def __init__(self, ngay, thang, nam):
		self.ngay = ngay
		self.thang = thang
		self.nam = nam
	#def
		

class KhoHang:
	"""docstring for KhoHang"""
	def __init__(self, maKhoHang, tenKhoHang, diaDiem, taiTrong, loaiHHoa, dateNhapHang, dateXuatHang, taiTrongNhap):
		self.maKhoHang = maKhoHang
		self.tenKhoHang = tenKhoHang
		self.diaDiem = diaDiem
		self.taiTrong = float(taiTrong)
		self.loaiHHoa = loaiHHoa
		self.dateNhapHang = Date(dateNhapHang)
		self.dateXuatHang = Date(dateXuatHang)
		self.taiTrongNhap = float(taiTrongNhap)
	#def

	def __str__(self):
		return "|{:^10}|{:^15}|{:^20}|{:^15}|{:^10}|{:^15}|{:^15}|{:^20}|".format(
            self.maKhoHang, self.tenKhoHang, self.diaDiem, self.taiTrong, self.loaiHHoa, self.dateNhapHang.ngay +"-"+self.dateNhapHang.thang+"-"+self.dateNhapHang.nam, self.dateXuatHang.ngay+"-"+self.dateXuatHang.thang+"-"+self.dateXuatHang.nam, self.taiTrongNhap
        )
	#def
		

class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None
	#def

class list:
	"""docstring for list"""
	def __init__(self):
		self.head = None
		self.tail = None
	#def
	
	def inDanhSach(self):	#In ra danh sách
		if self.head is None:
			print("Chua co danh sach")
			return
		node = self.head
		print(row)
		print(header)
		print(row)
		while node is not None:
			print(node.data.__str__())
	#def

	def themKhoHang(self, data):	#Thêm Kho hàng từ bàn phím
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
	#def


		

		