from random import randint
#from pw_manager import passwords

def createlistcar():
    list = []
    for i in range(48,58):
        list.append(i) 
    for j in range(65,91):
        list.append(j)
    for k in range(98,123):
        list.append(k)
    return list

def listchiffre():
    list = []
    for i in range(48,58):
        list.append(i)
    return list 

def listmajuscule():
    list = []
    for i in range(65,91):
        list.append(i)
    return list 

def listminiscule():
    list = []
    for i in range(98,123):
        list.append(i)
    return list 



def passwordallcharacter(n,name):
    pw=""
    while len(pw)<n:
        pw+=chr(randint(33,126))
    #passwords[name]=pw
    pw+="\n"
    fichier = open("pw.txt","a")
    fichier.write("The password to " + name + "is : " + pw)
    fichier.close()
    return pw

def passwordnotallcharacter(n,name):
    pw=""
    L = createlistcar()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    pw+="\n"
    fichier = open("pwnot.txt","a")
    fichier.write("The password to " + name +" is : " + pw)
    fichier.close()
    return pw

def passwordnumber(n,name):
    pw=""
    L = listchiffre()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    pw+="\n"
    fichier = open("pwnumber.txt","a")
    fichier.write("The password to " + name + " is : " + pw)
    fichier.close()
    return pw

def passwordmajuscule(n,name):
    pw=""
    L = listmajuscule()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    pw+="\n"
    fichier = open("pwmaj.txt","a")
    fichier.write("The password to " +name+" is : " + pw)
    fichier.close()
    return pw

def passwordminiscule(n,name):
    pw=""
    L = listminiscule()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    pw+="\n"
    fichier = open("pwmin.txt","a")
    fichier.write("The password to " +name+ " is : " + pw)
    fichier.close()
    return pw

def pwall():
    print("Quelle est le nom du site ou vous voulez créer un mot de passe ?")
    name = input()
    print("Quelle type de mots de passe voulez-vous utiliser ? (all, not_all, number, minuscule ou majuscule)")
    choice = input()
    match choice:
        case "all":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return False
            else:
                print(passwordallcharacter(number,name))
        case "not_all":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return False
            else:
                print(passwordnotallcharacter(number,name))
        case "number":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return False
            else:
                print(passwordnumber(number,name))
        case "minuscule":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            print(type(number))
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return False
            else:
                print(passwordminiscule(number,name))
        case "majuscule":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return False
            else:
                print(passwordmajuscule(number,name))
        case _:
            print("erreur")
            return False
    
pwall()
#print(passwordallcharacter(15))
#print(passwordnotallcharacter(15))
#print(passwordnumber(15))
#print(passwordmajuscule(15))
#print(passwordminiscule(15))
#print(createlistcar())