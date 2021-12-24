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
    luachon = 1
    while luachon != 0:
        menu()
        print("\n")
        print(">> Nhap chuc nang: ")
        luachon = int(input())

        if luachon == 1:
            if listKhoHang.docFile() == True:
                print("Doc file thanh cong")
            else:
                print("Doc file that bai")
        elif luachon == 2:
            listKhoHang.inDanhSach()
        else:
            return
#def


def main(self):
    process()
#def

if __name__ == '__main__':
    main()
#if