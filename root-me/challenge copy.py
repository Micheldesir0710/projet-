import socket
import base64

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
        print(answer)
        word = answer[-6].replace("'",'')
        word_bytes = base64.b64decode(word)
        word_string = word_bytes.decode('utf-8')
        print(word_string)

        

        # Envoi du résultat au serveur
        s.sendall(f"{word_string}\n".encode('utf-8'))
        
        # Réception de la réponse finale
        final_response = s.recv(1024).decode('utf-8')
        print("Réponse finale:", final_response)
        #s.close()

if __name__ == "__main__":
    solve_challenge()