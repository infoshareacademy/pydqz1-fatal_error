import create_nick_email

osoba = create_nick_email.create_person()
imie = create_nick_email.name_random()
nazwisko = create_nick_email.surname_random()
niczek = create_nick_email.nickname_random()
imejl = create_nick_email.email_random()
adresik = create_nick_email.address_random()

dane = [imie, nazwisko, niczek, imejl, adresik]
print(osoba)

print("1")
for datac in osoba:
    print(" {} : {} ".format(datac, osoba[datac]))
print("2")

for data in dane:
    print(data)
print("3")