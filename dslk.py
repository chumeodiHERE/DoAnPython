header = "|{:^10}|{:^15}|{:^20}|{:^15}|{:^10}|{:^15}|{:^15}|{:^20}|".format(
    "MA KHO", "TEN KHO", "DIA DIEM", "TAI TRONG(KG)", "LOAI", "DATE NHAP", "DATE XUAT", "TAI TRONG NHAP(KG)"
)

row = "#{:-^10}#{:-^15}#{:-^20}#{:-^15}#{:-^10}#{:-^15}#{:-^15}#{:-^20}#".format("", "", "", "", "", "", "", "")


class KhoHang:
	def __init__(self, maKhoHang, tenKhoHang, diaDiem, taiTrong, loaiHHoa, dateNhapHang, dateXuatHang, taiTrongNhap):
		self.maKhoHang = maKhoHang
		self.tenKhoHang = tenKhoHang
		self.diaDiem = diaDiem
		self.taiTrong = float(taiTrong)
		self.loaiHHoa = loaiHHoa
		self.dateNhapHang = dateNhapHang
		self.dateXuatHang = dateXuatHang
		self.taiTrongNhap = float(taiTrongNhap)
	#def

	def __str__(self):
		return "|{:^10}|{:^15}|{:^20}|{:^15}|{:^10}|{:^15}|{:^15}|{:^20}|".format(
            self.maKhoHang, self.tenKhoHang, self.diaDiem, self.taiTrong, self.loaiHHoa, self.dateNhapHang, self.dateXuatHang, self.taiTrongNhap
        )
	#def
#class
		

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	#def
#class

class SList:
	def __init__(self):
		self.head = None
		self.tail = None
	#def
	
	def createNode(self, data):		#Hàm để tạo node mới (Them cuối)
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
	#def
	
	def inDanhSach(self):	#In ra danh sách
		if self.head == None:
			print("Chua co danh sach")
			return
		node = self.head
		print(row)
		print(header)
		print(row)
		while node != None:
			print(node.data.__str__())
			node = node.next
		print(row)
	#def
	def addHead(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def them1KhoHang(self):
		maKH = input("Nhap ma Kho Hang: ")
		tenKH = input("Nhap ten Kho Hang: ")
		diaDiem = input("Nhap dia diem: ")
		taiTrong = float(input("Nhap tai trong: "))
		loaiHH = input("Nhap loai Hang Hoa: ")
		dateNhap = input("Nhap ngay nhap hang: ")
		dateXuat = input("Nhap ngay xuat hang: ")
		taiTrongNhap = float(input("Nhap tai trong hang nhap vao kho: "))

		self.createNode(KhoHang(maKH, tenKH, diaDiem, taiTrong, loaiHH, dateNhap, dateXuat, taiTrongNhap))
		print("THEM THANH CONG!!")
	#def

	def docFile(slist):
		try:
			f = open('ThTinKho.txt', 'r')
			datalist = f.readlines()
			for line in datalist:
				data = line.split()
				if len(data) == 8:
					slist.addHead(KhoHang(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
			f.close()
			print("Doc file thanh cong!!")
			return True
		except:
			return False
	#def
#class


		

		