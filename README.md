# multilang_site

Bienvenue dans le projet multilang_site, une application Django multilingue créée pour le test technique en vue d'une alternance chez Diot-Siaci.

## Objectif du projet
Ce projet a pour but de démontrer mes compétences en développement avec Django, notamment la création d'une application multilingue. Une intégration optionnelle de modèles de langage (LLM) pour des tâches de création de chatbot et de recherche augmentée par intelligence artificielle (RAG) est également incluse.

## Structure du projet
Le projet est organisé comme suit :

- **multilang_site/** : Répertoire principal du projet Django.
- **main/** : Application Django contenant les fonctionnalités principales.
- **templates/** : Répertoire contenant les templates HTML.
- **static/** : Répertoire contenant les fichiers statiques (CSS, JS, images).
- **locale/** : Répertoire contenant les fichiers de traduction.

## Prérequis
- Python 3.x
- Django 4.x
- Git

## Installation et configuration

1. Clonez le dépôt Git :

    ```bash
    git clone https://github.com/YoussefELKALLOUBI/tt3.git
    cd multilang_site
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

3. Appliquez les migrations de la base de données :

    ```bash
    python manage.py migrate
    ```

4. Créez des instances d'articles :

    ```bash
    python main/management/commands/create_random_articles.py
    ```


5. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

## Utilisation
Accédez à l'application en ouvrant votre navigateur et en visitant `http://127.0.0.1:8000`.

## Démonstation
![chrome-capture-2024-6-18](https://github.com/YoussefELKALLOUBI/MultiLang-App/assets/81879215/6b947026-9dcc-4eea-821a-7974a62981dc)

## Contribuer
Les contributions sont les bienvenues ! Pour signaler un problème ou proposer une amélioration, veuillez ouvrir une "issue" sur le dépôt GitHub.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
