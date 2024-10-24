# importe library random

import random

# Fonction principale du jeu


def deviner_nombre():
    # Générer un nombre aléatoire entre 1 et 100 ,avec randint module de la library randam
    # init variable tentative max
    # init variable tentatives
    nombre_a_deviner = random.randint(1, 100)
    tentatives_max = 10
    tentatives = 0

    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. Vous avez 10 tentatives pour deviner le bon nombre.")

    while tentatives < tentatives_max:
        # Demander à l'utilisateur de deviner
        # rajoute +1 à la variable tentatives pour compter le nbr de tentatives
        try:
            devine = int(input(f"Tentative {tentatives + 1}: Entrez votre nombre: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        tentatives += 1

        # Comparer le nombre deviné avec le nombre à deviner
        # si devine est inférieur au nombre a deviner
        if devine < nombre_a_deviner:
            print("Trop petit.")
        # si devine supérieur au nombre a deviner
        elif devine > nombre_a_deviner:
            print("Trop grand.")
        else:
            print(f"Bravo, vous avez deviné le nombre en {tentatives} tentatives !")
            break

    # Si l'utilisateur n'a pas trouvé le nombre , si toutes les tentative sont utilisées
    # et devine est different du nombre_a_deviner
    # print la réponse
    if tentatives == tentatives_max and devine != nombre_a_deviner:
        print(f"Game Over. Le nombre était {nombre_a_deviner}.")

# Fonction pour demander si l'utilisateur veut rejouer


def rejouer():
    while True:
        choix = input("rejouer ? (o/n): ").lower()
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

# Lancer le jeu , si le jeu est exectuer dans main ou en tant que module


if __name__ == "__main__":
    jeu()
