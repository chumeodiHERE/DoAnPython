class Date(object):
	"""docstring for Date"""
	def __init__(self, ngay=None, thang=None, nam=None):
		self.ngay = ngay
		self.thang = thang
		self.nam = nam
		

class KhoHang:
	"""docstring for KhoHang"""
	def __init__(self, maKhoHang=None, tenKhoHang=None, diaDiem=None, taiTrong=None, loaiHHoa=None, dateNhapHang=None, dateXuatHang=None, taiTrongNhap=None):
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
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

		