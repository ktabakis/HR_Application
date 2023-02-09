# Import MySql Connector
import mysql.connector
# making MySQL connection object
mycon = mysql.connector.connect(
host='localhost', user='root',
password='', database='HR')
# making MySQL cursor object
mycur = mycon.cursor()

def space():
	for i in range(1):
		print()

def check():
    # query to select all customer IDs from the table
    qry = 'select Kodikos_Ypallilou from members;'
    mycur.execute(qry)

    d = mycur.fetchall()

    # to create a list of all customer IDs in the table
    list_of_workers = []
    for ids in d:
        # a list of all customer IDs in table
        list_of_workers.append(ids[0])
    return list_of_workers

def prosthiki():#prosthiki ypalllilou
        ask ="Y"
        list_of_workers = check()
        while ask in "Yy":
            Kodikos_Ypallilou=int(input("Dwse kodiko upalillou"))#elegxos ama uparxei hdh o upallilos
            if Kodikos_Ypallilou in list_of_workers:
                print("O ypallilos yparxei hdh. Prosthese kainourio ")
            else:
                stoixeia=()   #Ena tuple gia ta stoixeia tou neou upallilou
                Onoma=input("Onoma ypallilou:")
                Email=input("Email ypallilou:")
                Thlefono=input("Thlefono ypallilou:")
                Dieuthinsh=input("Dieuthinsh ypallilou:")
                Misthos=input("Mistho ypallilou:")
                stoixeia=(Kodikos_Ypallilou,Onoma,Email,Thlefono,Dieuthinsh,Misthos)

                qry="Insert into members values(%s,%s,%s,%s,%s,%s);"

                values=stoixeia
                #Bainoun ta stoixeia mes sthn vash mas
                mycur.execute(qry, values)
                mycon.commit()
                print("O ypallilos prosthethike")
                ask = input('Theleis na prostheseis kiallon ypallilo? (Y/N) ')
                if ask not in ('Yy'):
                    space()
                    break

def provolh():    #provolh ypallilou
    y=int(input("Dwse Kodiko Ypallilou"))
    kodikos=(y, )
    list_of_workers = check()#elegxos ama uparxei o ypallilos
    if y in list_of_workers:
        ask = input("Eisai sigouros oti theleis na sunexiseis? (Y/N)")
        if ask in ('Yy'): #elegxos ama einai sigouros gia thn diadikasia pou paei na kanei
            qry="Select * from members where Kodikos_Ypallilou=%s;"
            mycur.execute(qry,kodikos)
            d = mycur.fetchall()#fernei ta stoixeia tou ypallilou apo thn vash
            print("Ta stoixeia tou ypallilou pou dialekse einai:",d) #emfanizei ta stouxeia
        else:
            print("H diadikasia akuronete.")

    else:
            print("O kodikos ypallilou pou edwses den uparxei.Ksana prospathise")

def epeksergasia(): #epeksergasia ypallilou
    y = int(input("Dwse Kodiko Ypallilou"))
    list_of_workers = check()
    kodikos = (y,)
    if y in list_of_workers:
        qry = "Select * from members where Kodikos_Ypallilou=%s;"
        mycur.execute(qry,kodikos)
        d = mycur.fetchall()
        print("Ta stoixeia tou ypallilou pou dialekse einai:", d)
        ask = input("Eisai sigouros oti theleis na sunexiseis? (Y/N)")
        if ask in ('Yy'):
           qry="Update members set Onoma=%s,Email=%s,Thlefono=%s,Dieuthinsh=%s,Misthos=%s where Kodikos_Ypallilou=%s;"
           stoixeia = ()  # Ena tuple gia ta stoixeia tou neou upallilou
           Onoma = input("Onoma ypallilou:")
           Email = input("Email ypallilou:")
           Thlefono = input("Thlefono ypallilou:")
           Dieuthinsh = input("Dieuthinsh ypallilou:")
           Misthos = input("Mistho ypallilou:")
           stoixeia = (Onoma, Email, Thlefono, Dieuthinsh, Misthos, y)
           mycur.execute(qry, stoixeia)#Kanei execute to query me to update ton stoixeion tou ypallilou
           mycon.commit()
        else:
            print("H diadikasia akuronete.")
    else:
        print("O kodikos ypallilou pou edwses den uparxei.Ksana prospathise")

def proagogh(): #epeksergasia ypallilou
    y = int(input("Dwse Kodiko Ypallilou"))
    list_of_workers = check()
    kodikos=(y, )
    if y in list_of_workers:
        qry = "Select * from members where Kodikos_Ypallilou=%s;"
        mycur.execute(qry, kodikos)
        d = mycur.fetchall()
        print("Ta stoixeia tou ypallilou pou dialekse einai:", d)
        ask = input("Eisai sigouros oti theleis na sunexiseis? (Y/N)")
        if ask in ('Yy'):
            print("O ypallilos pou dialekse einai o:",y)
            qry="Update members set Misthos=%s where Kodikos_Ypallilou=%s;"
            stoixeia = ()  # Ena tuple gia ta stoixeia tou neou upallilou
            Misthos = input("Neos misthos ypallilou:")
            stoixeia = (Misthos, y)
            mycur.execute(qry, stoixeia)#Kanei execute to query me to update ton mistho tou ypallilou
            mycon.commit()
        else:
            print("H diadikasia akuronete.")
    else:
            print("O kodikos ypallilou pou edwses den uparxei.Ksana prospathise")

def diagrafh(): #diagrafh ypallilou
    y = int(input("Dwse Kodiko Ypallilou"))
    list_of_workers = check()
    kodikos = (y,)
    if y in list_of_workers:
        qry = "Select * from members where Kodikos_Ypallilou=%s;"
        mycur.execute(qry, kodikos)
        d = mycur.fetchall()
        print("Ta stoixeia tou ypallilou pou dialekse einai:", d)
        ask = input("Eisai sigouros oti theleis na sunexiseis? (Y/N)")
        if ask in ('Yy'):
            print("O ypallilos pou dialekse einai o:",y)
            qry="delete from members  where Kodikos_Ypallilou=%s;"
            mycur.execute(qry)
            mycon.commit()
        else:
            print("H diadikasia akuronete.")
    else:
            print("O kodikos ypallilou pou edwses den uparxei.Ksana prospathise")

def anazhthsh():
    y = int(input("Dwse Kodiko Ypallilou"))
    list_of_workers = check()
    kodikos = (y,)
    if y in list_of_workers:
        qry = "Select * from members where Kodikos_Ypallilou=%s;"
        mycur.execute(qry, kodikos)
        d = mycur.fetchall()
        print("Ta stoixeia tou ypallilou pou dialekse einai:", d)
        ask = input("Eisai sigouros oti theleis na sunexiseis? (Y/N)")
        if ask in ('Yy'):
            print("O ypallilos pou dialekse einai o: ",y)
            z =int(input("Tha itheles na:\n 1.Na deis ta stoixeia tou ypallilou\n 2.Na kaneis kapoia epeksergasia sta soixeia tou ypallilou \n 3.Na allakseis ton mistho tou ypallilou\n 4.Diagrapseis ton ypallilo"))
            if z==1:
                 provolh()
            elif z==2:
                    epeksergasia()
            elif z==3:
                   proagogh()
            else:
                   diagrafh()
        else:
            print("H diadikasia akuronete.")
    else:
            print("O kodikos ypallilou pou edwses den uparxei.Ksana prospathise")

            #Provolh epilogon
x=int(input("Ti tha thelate na kanete: \n1.Prosthikh ypallilou\n2.Provolh stoixeion ypallilou\n3.Epeksergasia ypallilou\n4.Proagogi ypalliloou(Afora auksish misthou)\n5.Diagrafh ypallilou\n6.Anazhthsh ypallilou\n7.Eksodos"))
while x<1 or x>7:
    x=int(input("Dwse yparkth epilogh"))
if x==1:
   prosthiki()
elif x==2:
    provolh()
elif x==3:
    epeksergasia()
elif x==4:
    proagogh()
elif x==5:
    diagrafh()
elif x==6:
    anazhthsh()
else:
    print("Telos diergasias. Kalh sunexeia")