# importe library random

import random

# Fonction principale du jeu


def deviner_nombre():
    # Générer un nombre aléatoire entre 1 et 100 ,avec randint module de la library randam
    nombre_a_deviner = random.randint(1, 100)
    tentatives_max = 10
    tentatives = 0

    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. Vous avez 10 tentatives pour deviner le bon nombre.")

    while tentatives < tentatives_max:
        # Demander à l'utilisateur de deviner
        try:
            devine = int(input(f"Tentative {tentatives + 1}: Entrez votre nombre: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        tentatives += 1

        # Comparer le nombre deviné avec le nombre à deviner
        if devine < nombre_a_deviner:
            print("Trop petit.")
        elif devine > nombre_a_deviner:
            print("Trop grand.")
        else:
            print(f"Bravo, vous avez deviné le nombre en {tentatives} tentatives !")
            break

    # Si l'utilisateur n'a pas trouvé le nombre
    if tentatives == tentatives_max and devine != nombre_a_deviner:
        print(f"Game Over. Le nombre était {nombre_a_deviner}.")

# Fonction pour demander si l'utilisateur veut rejouer


def rejouer():
    while True:
        choix = input("Voulez-vous rejouer ? (o/n): ").lower()
        if choix == 'o':
            return True
        elif choix == 'n':
            print("Merci d'avoir joué ! À bientôt.")
            return False
        else:
            print("Réponse invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")

# Boucle principale pour rejouer


def jeu():
    while True:
        deviner_nombre()
        if not rejouer():
            break

# Lancer le jeu


if __name__ == "__main__":
    jeu()
