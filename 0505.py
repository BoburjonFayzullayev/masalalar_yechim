import math
import functools

# print('"nexia" , "tico", "damas" ko`rganlar qilar havas')
# print(22%4)

#
# # Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
# a = 125
# S = a**2
# P = 4*a
# print("Kvadratning yuzi ", a**2, "ga va perimetri esa ", P, "ga teng")

# # Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( deb oling)oling
# a = 12
# PI = 3.14
# print("Doiraning yuzi ", a*PI , "ga teng")

# # Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
# a=6
# b=7
# c=(a**2)+(b**2)
# print("Gepatinuza", c ,"ga teng")

#
# # Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#
# son = input("istalgan son kiriting -> ")
# print( f"{son} ning kvadrati ",  int(son)**2,  "ga teng")
# print( f"{son} ning kubi ",  int(son)**3,  "ga teng")

# # Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
# yosh = input("yoshingiz nechada -> ")
# yil = 2023 - int(yosh)
# print(f"siz {yil}-yilda tug`ilgansiz")
#

# # Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
#
# son1 = int(input("birinchi sonni kiriting -> "))
# son2 = int(input("ikkinchi sonni kiriting -> "))
#
# print(f"{son1} + {son2} = ", son1+son2 )
# print(f"{son1} - {son2} = ", son1-son2 )
# print(f"{son1} * {son2} = ", son1*son2 )
# print(f"{son1} / {son2} = ", son1/son2 )

#   #ismlar degan royxat yarating va kamida 3 ta yaqin dostingizning ismini kiriting
#    #Royxatdagi har bir dostingizga qisqa xabar yozib konsolga chiqaring:
#
# ismlar = [ 'dilshod', 'erali', 'ozod']
#
# print(ismlar[0], "fudbol uynaymizmi")
# print(" qayerdasan", ismlar[1])
# print("bugun ", ismlar[2], "ni anaqasiykan")


# #sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# #Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
#
# sonlar = [20, 16, -6, 3.2 ,50]
#
# sons = sonlar[0] + sonlar[2]
# print(sons)
#
# sonlar[3]=sonlar[3]+0.8
# print(sonlar)
# sonlar[4]=15
# print(sonlar)


#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

# t_shaxslar =[]
# t_shaxslar.append("Amir Temur")
# t_shaxslar.append("Mirzo Ulug`bek")
# t_shaxslar.append("Z.M.Bobur")
# t_shaxslar.append("Al-Xorazmiy")
# z_shaxslar = []
# z_shaxslar.append("Bobur")
# z_shaxslar.append("Shavkat Mirziyoyev")
# z_shaxslar.append("Ozodbek Nazarbekoov")
#
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan va zamonaviy shaxslardan {z_shaxslar.pop(0)} bilan kurishgan bulardim")
#
#
#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends =[]
friends.append("dilshod")
friends.append("erali")
friends.append("ozod")
friends.append('zufar')
friends.append('maruf')
friends.append('shaxzod')
friends.remove('shaxzod')
friends.insert(2,'asad')
friends.insert(8, 'usar')

print(friends)




#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#Ro'yxatning uzunligini konsolga chiqaring
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#Asl ro'yxatni qaytadan konsolga chiqaring
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

# davlatlar = ['aqsh', 'rossiya', 'xitoy', 'germaniya', 'britaniya']
#
# print(davlatlar)
# print(len(davlatlar))
# print("sorted yordamida tariblangan", sorted(davlatlar))
# print("teskari tartibda konsolga chiqarish", sorted(davlatlar, reverse=True))
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print("alifbo buyicha", davlatlar)
# davlatlar.sort(reverse=True)
# print("teskari alifbo", davlatlar)
#

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#Ro'yxatdagi elementlar sonini hisoblang
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#
# sonlar = list(range(120,1200,2))
# print(sonlar)
# son = sum(sonlar)
# print(son)
# a=max(sonlar)
# b=min(sonlar)
# print(a-b)
# print(len(sonlar))
#
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])


#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

# sonlar = list(range(11, 100, 2))
#
# for n in sonlar:
#     print(n**3)
#
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

suxbat =input("bugun nechta odam bilan suxbat qildingiz -> ")
suxbat = int(suxbat)
odam =[]
for n in range(suxbat):
    odam.append(input(f"{n+1} - suxbat qilgan odamingiz -> "))
print(odam)



#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car.lower()=="gm":
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car.lower()!="gm":
#         print(car.title())
#     else:
#         print(car.upper())


#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

# login = input("Loginingizni kiriting -> ")
# if login.lower() == "admin":
#     print(f" Xush kelibsiz, {login.title()}. Foydalanuvchilar ruyxatini kurasizmi? ")
# else:
#     print(f"Xush kelipsiz {login.title()} ")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# son1 = int(input("Ikkita son kiriting. 1-son ->"))
# son2= int(input("2-son"))
# if son1 == son2:
#     print("sonlar teng")

# #Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son = int(input("Istalgan son kiriting -> "))
# if son>0:
#     print('musbat son')
# else:
#     print('manfiy son')

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = int(input("Istalgan son kiriting -> "))
if son<0:
    print("musbat son kiriting")
else:
    print(son**(1/2))
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("juft son kiriting -> "))
# if son%2==0:
#     print("rahmat")
# else:
#     print("bu juft son emas")
#

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#gar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("yshingiz nechada -> "))
# if yosh<=4:
#     print("sizga bepul")
# elif yosh<=18:
#     print("10000 sum ")
# elif yosh<=60:
#     print("20000 sum")
# elif yosh>60:
#     print("bepul")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son = int(input("1-son -> "))
# son2= int(input("2-son -> "))
# if son>son2:
#     print(f"{son}>{son2}")
# elif son<son2:
#     print(f"{son}<{son2}")
# elif son==son2:
#     print('sonlar teng')

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['olma', 'anor', 'nok', 'banan', 'pomidor', 'non', 'suv', 'olcha', 'gilos', 'mandarin']
# savat = []
# print("savatga 5 ta mahsulot kiriting:")
# for n in list(range(5)):
#     savat.append(input(f"savatga {n+1}-mahsulotni qushing ->").lower())
# for buyurtma  in savat:
#     if buyurtma in mahsulotlar:
#         print(f" dukonimizda {buyurtma} bor")
#     else:
#         print(f" dukonimizda {buyurtma} yuq")

mahsulotlar = ['olma', 'anor', 'nok', 'banan', 'pomidor', 'non', 'suv', 'olcha', 'gilos', 'mandarin']
savat = []
print("savatga 5 ta mahsulot kiriting:")
for n in list(range(5)):
    savat.append(input(f"savatga {n+1}-mahsulotni qushing ->").lower())
bor_mahsulot=[]
mavjud_emas=[]

for buyurtma in savat:
    if buyurtma in mahsulotlar:
        bor_mahsulot.append(buyurtma)



    else:
        mavjud_emas.append(buyurtma)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

diction = {
    'integer': 'butun sonlar',
    'float': 'haqiqiy sonlar',
    'string': 'matnlar',
    'for': 'uchun',
    'if': 'agar',
    'else': 'aks holda',
    'list': 'ruyxat',
}

# dictt = diction.get(input('Kalit suz kiriting -> '), 'Bunday suz yuq')
#
# print(dictt)
surov = input(' kalit suz kiriting -> ')
javob = diction.get(surov)
if javob==None:
    print("bunday suz yuq")
else:
    print(f" {surov.title()} suzini tarjimasi {javob}")
