gun = input("Lütfen bu gün ayın kaçı olduğunu yazın: ")
gun = int(gun)

if gun == 12:
    print("Doğum Gününüz Kutlu Olsun Dayıı")
elif gun >= 31:
    print("Böyle Bir Gün Yok")
else:
    print("Normal Bir Gün")
