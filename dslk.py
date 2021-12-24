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
		self.taiTrong = int(taiTrong)
		self.loaiHHoa = loaiHHoa
		self.dateNhapHang = Date(dateNhapHang)
		self.dateXuatHang = Date(dateXuatHang)
		self.taiTrongNhap = int(taiTrongNhap)
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
	
	def inDanhSach(self):
		pass
	#def
		

		