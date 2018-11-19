class 집:
    def __init__(self,member,address):
        self.가족인원=member
        self.주소=address

    def 문을열다(self):
        print("문염")
    def 문을닫다(self):
        print("문닫음")
h=집(4,"경기")
h.문을열다()
h.문을닫다()
print(h.가족인원)
print(h.주소)

