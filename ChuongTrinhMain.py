from dslk import *

def menu(self):
    print("#------------------------------------------------#")
    print("|                      MENU                      |")
    print("#------------------------------------------------#")
    print("|    1. Doc du lieu tu file                      |")
    print("|    2. Hien thi tat ca thong tin kho            |")
    print("|    3. them 1 xe X vao stack                    |")
    print("|    0.                THOAT                     |")
#def

def process(self):
    listKhoHang = SList()
    luachon = -1
    while luachon != 0:
        menu()
        print("\n")
        print(">> Nhap chuc nang: ")
        luachon = int(input())

        if luachon == 1:
            listKhoHang.docFile()
            listKhoHang.inDanhSach()
#def


def main(self):
    process()
#def

if __name__ == '__name__':
    main()