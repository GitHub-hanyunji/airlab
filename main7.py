#main.py
#7번

from module7 import PhoneBook

def main():
    obj=PhoneBook()
    obj.add("kim",office="1234567",email="kim@company.com")
    obj.add("Park",office="2345678",email="park@company.com")
    print(obj)
if __name__ == "__main__":
    main()