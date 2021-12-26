# -*- coding: utf-8 -*-
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
	#def

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
		return data
	#def

	def docFile(slist):
		try:
			f = open('ThTinKho.txt', mode ='r+')
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

	def ghiFile(slist):
		try:
			node = slist.them1KhoHang()		#Node trở thành 1 list chứa các thuộc tính của đối tượng vừa thêm
			f = open('ThTinKho.txt', mode ='a+')
			f.write("\n{} {} {} {} {} {} {} {}".format(node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]))
			f.close()
			print(">> Them va luu kho thanh cong!! <<")
			return True
		except:
			return False
	#def

	def __sort__(self):	#In ra danh sách
		if self.head == None:
			print("Chua co danh sach")
			return None
		else:
			data_p = self.head
			while data_p != None:
				data_q = data_p.next
				while data_q != None:
					if data_p.data.taiTrong < data_q.data.taiTrong:
						data_p.data, data_q.data = data_q.data, data_p.data
					data_q = data_q.next
				data_p = data_p.next
			print(">>Success<<")		
	#def

	def deleteKho(self, maKhoHang):
		if self.head == None:
			return None
		else:
			node = self.head
			if node.data.maKhoHang == maKhoHang:
				self.head = (
					node.next
				)
				return node.data
			while node.next != None:
				if (
					node.next.data.maKhoHang == maKhoHang
				):
					node.next = (
						node.next.next
					)
					return node.data
				node = node.next
		return None
	#def

	def findKhoTh10(self):		#Hàm tìm các kho được nhập vào tháng 10/2021
		if self.head == None:
			return None
		else:
			dateNhapHang = '/10/2021'
			print("\t\t\t\t\tDANH SACH KHO HANG NHAP VAO THANG 10/2021")
			node = self.head
			print(row)
			print(header)
			print(row)
			while node != None:
				if dateNhapHang in node.data.dateNhapHang:
					print(node.data.__str__())
				node = node.next
			print(row)
			return None
	#def

	def findKhoTrong(self):		#Hàm tìm các kho còn trống (tải trọng nhập < tải trọng sẵn có của kho)
		if self.head == None:
			return None
		else:
			node = self.head
			print("\t\t\t\t\t\tDANH SACH KHO HANG CON TRONG")
			print(row)
			print(header)
			print(row)
			while node != None:
				if node.data.taiTrongNhap < node.data.taiTrong:
					print(node.data.__str__())
				node = node.next
			print(row)
			return None
	#def

	def findHangDongLanh(self):
		if self.head == None:
			return None
		else:
			loaiDongLanh = 'Dong-Lanh'
			node = self.head
			print("\t\t\t\t\t\tDANH SACH KHO HANG DONG LANH")
			print(row)
			print(header)
			print(row)
			while node != None:
				if loaiDongLanh in node.data.loaiHHoa:
					print(node.data.__str__())
				node = node.next
			print(row)
			return None
	#def

	def avgKhoDN(self):
		if self.head == None:
			return None
		else:
			maKH = 'DONG-NAI'
			sumTaiTrong = 0
			count = 0
			node = self.head
			print("\t\t\t\t\t\tDANH SACH KHO HANG O DONG NAI")
			print(row)
			print(header)
			print(row)
			while node != None:
				if maKH in node.data.maKhoHang:
					print(node.data.__str__())
					sumTaiTrong += node.data.taiTrong
					count += 1
				node = node.next
			avg = sumTaiTrong / count
			ketqua = round(avg, 2)
			print(row)
			print("\n\n>> Tai trong trung binh cua cac kho hang o DONG NAI: " + str(ketqua))
			return None
	#def
#class


		

		