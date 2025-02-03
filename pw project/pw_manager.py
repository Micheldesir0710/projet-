#password manager basic

import sys, pyperclip
"""from random import randint
#from pw_manager import passwords
 
passwords = {}

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
    passwords = {}
    while len(pw)<n:
        pw+=chr(randint(33,126))
    passwords[name]=pw
    return passwords

def passwordnotallcharacter(n,name):
    pw=""
    passwords = {}
    L = createlistcar()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    passwords[name]=pw
    return passwords

def passwordnumber(n,name):
    pw=""
    passwords = {}
    L = listchiffre()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    passwords[name]=pw
    return passwords

def passwordmajuscule(n,name):
    pw=""
    passwords = {}
    L = listmajuscule()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    passwords[name]=pw
    return passwords

def passwordminiscule(n,name):
    pw=""
    passwords = {}
    L = listminiscule()
    while len(pw)<n:
        pw+=chr(L[randint(0,len(L)-1)])
    passwords[name]=pw
    return passwords

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
                return {}
            else:
                print(passwordallcharacter(number,name))
        case "not_all":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return {}
            else:
                print(passwordnotallcharacter(number,name))
        case "number":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return {}
            else:
                print(passwordnumber(number,name))
        case "minuscule":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            print(type(number))
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return {}
            else:
                print(passwordminiscule(number,name))
        case "majuscule":
            print("combien de charactère doit contenir le mot de passe ?")
            number = input()
            number = int(number)
            if type(number)!= int:
                print("Erreur le nombre doit être un entier !!!")
                return {}
            else:
                print(passwordmajuscule(number,name))
        case _:
            print("erreur")
            return False
"""

passwords = {
    "google" : "googlepass",
    "paypal" : "paypalpass"
}



if len(sys.argv) < 2:
    print('Help : python pw_manager [account]')
    sys.exit()

account = sys.argv[1]
verif = False

"""if account == "all":
    pwall()
    passwords = passwords.update(pwall())
    verif = True
"""
if account in passwords and not verif:
    pyperclip.copy(passwords[account])
    print('Password pour ' + account + ' à été copié avec succès')
elif not verif:
    print("Il n'y a pas de compte de ce nom")