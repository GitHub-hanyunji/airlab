#main.py
# 6번

from module6 import Person
def main():
    p1=Person("Kim",o="1234567",e="kim@company.com")
    p2=Person("Park",o="2345678")
    print("p1=",p1)
    print("p2=",p2)
    p2.setEmail("park@company.com")
    print(f"p2.setEmail(\"{p2.getEmail()}\")")
if __name__ == "__main__":
    main()  