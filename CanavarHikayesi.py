
print("""Uzaktan 2 Işıklı Ve Hızlı Bir Şey Yaklaşıyor Ne Yapmalısın:

A:Yolda Kal
B:Kenara Geç
""")

islem = ""
while islem not in ("A", "B", "a", "b"):
    islem = input()

if islem == "A" or islem == "a": 
    print("Öldün")
    exit("Oyun Bitti")
elif islem == "B" or islem == "b":
    yon = input("""Yaşıyorsun Oraya Gİdip Ne Olduğuna Bakacakmısın? 

A:Gidip Bak 
B:Bakma Ve Karanlğa Doğru İlerle  
""")

while yon not in ("A", "B", "a", "b"):
    yon = input()


if yon == "A" or yon == "a":
    print("O Şey 2 Gözlü Bir Canavardı Ve Seni Yedi")
    exit("Oyun Bitti")
elif yon == "B" or  yon == "b":
 islem2 = input("""Karanlıkta 2 Gözlü Bir Canavar Gördün Ne Yapacaksın?  

A:Saldır Ve Kendini Koru 
B:Kaç Ve Kendini Koru 
""")

while islem2 not in ("A", "B", "a", "b"):
    islem2 = input()

if islem2 == "A" or islem2 == "a":
    print("Saldırıların Ona Bir Zarar Vermedi Ve öldün")
    exit("Oyun Bitti")
elif islem2 == "B" or islem2 == "b":
    print("Küçük İnsan Ayakların Onun Hızına Yakın Bile Değildi Ve Yakalanıp Öldün")
    exit("Oyun Bitti")
