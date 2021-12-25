from dslk import *

def menu():
    print("#------------------------------------------------#")
    print("|                      MENU                      |")
    print("#------------------------------------------------#")
    print("|    1. Doc du lieu tu file                      |")
    print("|    2. Hien thi tat ca thong tin kho            |")
    print("|    3. Them 1 Kho Hang va luu vao file          |")
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
            print("Fuckk")
            listKhoHang.ghiFile()
        else:
            return 0
#def


def main():
    process()
#def

if __name__ == '__main__':
    main()
#if