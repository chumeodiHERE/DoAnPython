
header = "|{:^10}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}|{:^20}|".format(
    "MA KHO", "TEN KHO", "DIA DIEM", "TAI TRONG(KG)", "LOAI", "DATE NHAP", "DATE XUAT", "TAI TRONG NHAP(KG)"
)

row = "#{:-^10}#{:-^15}#{:-^20}#{:-^15}#{:-^15}#{:-^15}#{:-^15}#{:-^20}#".format("", "", "", "", "", "", "", "")


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
		return "|{:^10}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}|{:^20}|".format(
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

	def them1KhoHang(slist):
		data = ['1', '2', '3', 4.5, '5', '6', '7', 8.5]		#Đặt giá trị tượng trưng vì không muốn list rỗng
		data[0] = str(input("Nhap ma Kho Hang: "))
		data[1] = str(input("Nhap ten Kho Hang: "))
		data[2] = str(input("Nhap dia diem: "))
		data[3] = float(input("Nhap tai trong: "))
		data[4] = str(input("Nhap loai Hang Hoa: "))
		data[5] = str(input("Nhap ngay nhap hang: "))
		data[6] = str(input("Nhap ngay xuat hang: "))
		data[7] = float(input("Nhap tai trong hang nhap vao kho: "))
		slist.createNode(KhoHang(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
		# return data
	#def

	def docFile(slist):
		try:
			f = open('ThTinKho.txt', 'r')
			datalist = f.readlines()
			for line in datalist:
				data = line.split()
				if len(data) == 8:
					slist.createNode(KhoHang(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
			f.close()
			print("Doc file thanh cong!!")
			return True
		except:
			return False
	#def

	# def ghiFile(slist):
	# 	try:
	# 		node = slist.them1KhoHang()		#Node trở thành 1 list chứa các thuộc tính của đối tượng vừa thêm
	# 		f = open('ThTinKho.txt', 'a')
	# 		f.write("{} {} {} {} {} {} {} {}\n".format(node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]))
	# 		f.close()
	# 		print(">> Them va luu kho thanh cong!! <<")
	# 		return True
	# 	except:
	# 		return False
	# #def

#class


		

		