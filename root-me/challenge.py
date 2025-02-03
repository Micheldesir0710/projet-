import socket
import math

def solve_challenge():
    # Paramètres de connexion
    host = 'challenge01.root-me.org'
    port = 52002

    # Création d'une socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur
        s.connect((host, port))

        # Réception des données
        data = s.recv(1024).decode('utf-8')
        print(data)

        # Extraction des nombres
        # Supposons que les nombres sont envoyés sous la forme "n1 n2"
        numbers = data.strip().split()
        n1 = float(numbers[-6])
        n2 = float(numbers[-2])

        # Calcul de la racine carrée de n1 et multiplication par n2
        
        result = math.sqrt(n1) * n2
        #Arrondir à deux chiffres après la virgule
        result_rounded = round(result, 2)

        # Envoi du résultat au serveur
        s.sendall(f"{result_rounded}\n".encode('utf-8'))
        
        # Réception de la réponse finale
        final_response = s.recv(1024).decode('utf-8')
        print("Réponse finale:", final_response)
        s.close()

if __name__ == "__main__":
    solve_challenge()