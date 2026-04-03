# Site Web pour présenter mes projets

Ce site Web me permet de présenter mes projets faits à la maison.

Il a été réalisé avec Django Python. Un bon tutoriel est sur https://www.w3schools.com/django/index.php.

Le site est hénérgé par Hostinger.

Tutoriel Django sur Hostinger https://www.hostinger.com/tutorials/django-tutorial.

## Création du venv

```
python -m venv venv_website
```

Et activer le venv.

```
source venv_website/bin/activate
```

## Installation de Django

```
python -m pip install Django
```

## Création du projet

```
django-admin startproject my_website
```

## Lancement du projet

```
cd my_website
python manage.py runserver
```

## Création de l'app projects

```
python lanage.py startapp projects
```

## Créer le fichier requirements.txt

Nécessaire pour le déploiement Hostinger.

```
pip freeze > requirements.txt
```




