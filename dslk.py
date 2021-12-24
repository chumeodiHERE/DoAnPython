class Date(object):
	"""docstring for Date"""
	def __init__(self, ngay, thang, nam):
		self.ngay = ngay
		self.thang = thang
		self.nam = nam
		

class KhoHang:
	"""docstring for KhoHang"""
	def __init__(self, maKhoHang, tenKhoHang, diaDiem, taiTrong, loaiHHoa, dateNhapHang, dateXuatHang, taiTrongNhap):
		self.maKhoHang = maKhoHang
		self.tenKhoHang = tenKhoHang
		self.diaDiem = diaDiem
		self.taiTrong = taiTrong
		self.loaiHHoa = loaiHHoa
		self.dateNhapHang = dateNhapHang
		self.dateXuatHang = dateXuatHang
		self.taiTrongNhap = taiTrongNhap
		

class Node:
	"""docstring for Node"""
	def __init__(self, data, next):
		self.data = data
		self.next = None

class list:
	"""docstring for list"""
	def __init__(self):
		self.head = None
		self.tail = None
		

		