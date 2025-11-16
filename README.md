# ue19-1ab-05 : Application de blagues conteneurisée

Ce projet est un simple application Python 3 qui utilise la librairie `requests` pour interroger l'API publique **JokesAPI** afin d'afficher une blague aléatoire.

## Comment lancer le programme

### Prérequis

* **Docker** (recommandé pour la conteneurisation).

### Lancement avec Docker (Recommandé)

1.  **Construire l'image Docker :**
    ```bash
    docker build -t blague-app .
    ```
2.  **Lancer le conteneur :**
    ```bash
    docker run blague-app
    ```
