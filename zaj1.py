# kurs_ang_dr={"teacher":"Malinowski","students":[1],"about":"ten kurt jest o angielsik ble ble ble"}
# kurs_pro_kom={"teacher":"Komorowkis","students":[1,2],"about":"ten kurt jest o programowaniu ble ble ble",}
# kursy={0:kurs_ang_dr,1:kurs_pro_kom}
# studenci={1:{"name":"Jakub","family":"Siedlecki","age":"15"},
#           2:{"name":"Michał","family":"Salmanowicz","age":"16"}}

kursy={}
studenci={}


def dodawanie_kursu(kursydef):
    teacher=input("Kto uczy? ")
    students=[]
    while True:
        select=int(input("Numery indeksów (-1 Aby skończyć)"))
        if select>0:
            students.append(select)
        else:
            break
    about=input("Podaj opis: ")
    inf_numer=int(input("Podaj numer kursu: "))
    kursydef[inf_numer]={"teacher":teacher,"students":students,"about":about}
    return kursydef

def dodaj_na_kurs(kursydef):
    select1=int(input("Kogo chcesz dodać (numer inex): "))
    select2=int(input("Na jaki chcesz dodać kurs (numer): "))

    kursydef[select2]["students"].append(select1)

    return kursydef

def wyswitlanie_kursy(kursydef):
    for i in kursydef:
        print("-----------KOLEJNY KURS------------")
        print("Kto prodzadzi",kursydef[i]["teacher"])
        print(f"Numer kursu {i}")
        print("Na kursie jest",len(kursydef[i]["students"]) ,"osób")
        print("Opis:",kursydef[i]["about"]) 
        print()

def wypisze_info_o_kursie(kursydef):
    numer=int(input("O któym kursie chcesz się dowiedzeć: "))
    print("Prodzadzący:",kursydef[numer]["teacher"])
    print("Opis:",kursydef[numer]["about"])
    print("Numery indeksów osób które ucześczszają", kursydef[numer]["students"])

    for i in kursydef[numer]["students"]:
        print("----------KOLEJNY STUDENT----------")
        print(f"Jego imię i nazwisko to",studenci[i]["name"],studenci[i]["family"])
        print(f"Mam",studenci[i]["age"],"lat")

def usuwanie_z_kursu(kursydef):
    inf_numer=int(input("Na którym kursie chcesz kodoś wypisać:"))
    kursydef[inf_numer]["students"].remove(int(input("Kogo chcesz usunąć")))
    return kursydef


def kursyy(kursy):
    print("--------------KURSY---------------")
    print("1. Wyświetl wszystkich kursów")
    print("2. Dodawanie na kurs")
    print("3. Wyświetlanie informacji o kursie")
    print("4. Dodawanie kursów")
    print("5. Usowanie z kursów")
    select=input("Co chesz robić? ")
    if "1"==select:
        wyswitlanie_kursy(kursy)
    elif "2"==select:
        kursy=dodaj_na_kurs(kursy)
    elif "3"==select:
        wypisze_info_o_kursie(kursy)
    elif "4"==select:
        kursy=dodawanie_kursu(kursy)
    elif "5"==select:
        usuwanie_z_kursu(kursy)
    return kursy



def edytowanie_studenta(studencidef):
    select1=int(input("Kogo chcesz zmienić: "))
    select2=input("Jaką informacje chcesz zmienić (name,family,age,indeks): ")
    if select2=="indeks":
        select2=input("Na jaki chcesz zmienić: ")
        a=studencidef[select1]
        del studencidef[select1]
        studencidef[select2]=a
    elif select2 in ["name","family","age"]:
        a=input("Na co chesz zmienić: ")
        studencidef[select1][select2]=a
    else:
        print("Podano złą wartość")
    print(studencidef)
    return studencidef

def wyswietlanie_studentow():
    for i in studenci:
        print("----------KOLEJNY STUDENT----------")
        print(f"Jego imię i nazwisko to",studenci[i]["name"],studenci[i]["family"])
        print(f"Mam",studenci[i]["age"],"lat")
        print(f"Jego indeks to {i}")

def dodawanie_studenta(studencidef):
    name=input("Podaj imię: ")
    family=input("Podaj nazwisko: ")
    age=input("Podaj ile mam lat: ")
    inelx=int(input("Podaj jaki mam być ideks: "))
    studencidef[inelx]={"name":name,"family":family,"age":age}

    return studencidef


def studenta(studenci):
    print("-------------STUDENCI--------------")
    print("1. Edytowanie")
    print("2. Dodawanie")
    print("3. Wyświetlanie")
    select1=input("Podaj: ")

    if select1=="1":
        studenci=edytowanie_studenta(studenci)
    elif select1=="2":
        studenci=dodawanie_studenta(studenci)
    elif select1=="3":
        wyswietlanie_studentow()
    else:
        print("ERROR")
    return studenci


def main(kursy=kursy,studenci=studenci):
    print("WITAMY")
    while True:
        print("---------------MENU----------------")
        print(kursy)
        print(studenci)
        print("1. Kursy")
        print("2. Studeńci")
        print("10. EXIT")
        select=input("Co chesz robić? ")
        
        if "1"==select:
            kursy=kursyy(kursy)
        elif "2"==select:
            studenci=studenta(studenci)
        elif "10"==select:
            return "ŻEGRAM"
        else:
            print("ERROR")


print(main())
print("DOWIDZNIA")