import socket
import math

def solve_challenge():
    # Paramètres de connexion
    host = 'challenge01.root-me.org'
    port = 52023

    # Création d'une socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur
        s.connect((host, port))

        # Réception des données
        data = s.recv(1024).decode('utf-8')
        print(data)
        
        answer = data.strip().split()
        word = answer[-6]
        word = word.decode()
        print(word)

        

        # Envoi du résultat au serveur
        #s.sendall(f"{result_rounded}\n".encode('utf-8'))
        
        # Réception de la réponse finale
        #final_response = s.recv(1024).decode('utf-8')
        #print("Réponse finale:", final_response)
        #s.close()

if __name__ == "__main__":
    solve_challenge()