from dslk import *

def menu():
    print("#------------------------------------------------#")
    print("|                      MENU                      |")
    print("#------------------------------------------------#")
    print("|    1. Doc du lieu tu file                      |")
    print("|    2. Hien thi tat ca thong tin kho            |")
    print("|    3. Them 1 Kho Hang va luu vao file          |")
    print("|    4. Sap xep Kho Hang theo Tai Trong          |")
    print("|    5. Xoa kho hang dua theo maKH (xoa bat ki)  |")
    print("|    6. Tim kho hang nhap vao 10/2021            |")
    print("|    7. Tim cac kho hang con trong               |")
    print("|    8. Tim cac kho hang dong lanh               |")
    print("|    9. Tinh tai trong tb cua kho hang DONG NAI  |")
    print("|    10. Dem so kho hang co ten bat dau la 'KH'  |")
    print("|    11. Them Kho hang dua vao tai trong         |")
    print("|    0.                THOAT                     |")
    print("|________________________________________________|")
#def

def process():
    listKhoHang = SList()
    luachon = 1
    while luachon != 0:
        menu()
        print("\n")
        luachon = int(input(">> Nhap chuc nang: "))
        if luachon == 1:
            listKhoHang.docFile()
        elif luachon == 2:
            listKhoHang.inDanhSach()
        elif luachon == 3:
            listKhoHang.ghiFile()
        elif luachon == 4:
            listKhoHang.__sort__()
        elif luachon == 5:
            maKH = str(input("Nhap ma Kho Hang can xoa: "))
            listKhoHang.deleteKho(maKH)
            print("Danh sach sau khi xoa: ")
            listKhoHang.inDanhSach()
        elif luachon == 6:
            listKhoHang.findKhoTh10()
        elif luachon == 7:
            listKhoHang.findKhoTrong()
        elif luachon == 8:
            listKhoHang.findHangDongLanh()
        elif luachon == 9:
            listKhoHang.avgKhoDN()
        elif luachon == 10:
            listKhoHang.countKhoHangKH()
        elif luachon == 11:
            add_obj = listKhoHang.Add_Kho()
            listKhoHang.__AddSort__(add_obj)
        else:
            return 0
#def


def main():
    process()
#def

if __name__ == '__main__':
    main()
#if