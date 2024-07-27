# Quicksign stage data scientist

## Introduction

Chez QuickSign, nous traitons des dizaines de milliers de documents tous les mois. L'équipe DocReco a pour rôle de créer les modèles permettant de classifier et de lire ces documents.

L'ensemble de nos librairies et services sont développés avec l'outil [poetry](https://python-poetry.org/). Cela nous permet de les versionner (grâce au champ `version` du fichier `pyproject.toml` à la racine de la librairie / du service), de développer plusieurs services / librairies sur la même machine en utilisant des environnements virtuels et de gérer les dépendences de nos services / librairies en fixant les versions des packages dont ils dépendent.

## Bonnes pratiques

L'utilisation de poetry est primordiale, et nous permet de tester le code reçu en quelques lignes.
L'utilisation de librairies externes est autorisée, mais dans ce cas la mise à jour de l'environnement est nécessaire.

Un environnement à jour est indispensable afin de nous permettre de tester le code.

Certaines conventions sur le code sont établies au sein de notre équipe. Nous attendons la même chose pour votre rendu.

Nous appliquons `black` et `isort` sur notre code. Ils vont formatter le code afin de respecter certaines normes. Nous en attendons de même pour votre rendu. Nous utilisons également `mypy` pour la gestion du typing. `pylint` est un autre outil utilisé qui permet de respecter les normes définis dans les [PEP](https://www.python.org/dev/peps/pep-0008/) (une note de 8/10 minimum à pylint est requise).

Pour lancer les tests unitaires vous pouvez utiliser la commande `poetry run pytest`. Afin d'obtenir un rapport plus détaillé sur la couverture de tests et de savoir quelles parties du code n'ont pas été testées vous pouvez utiliser la commande `poetry run pytest . -ra -q -vv --cov-config=./pyproject.toml --cov=./app --cov-report=term`. Un coverage de 100% à la fin du développement sera apprécié.

Le fichier `pyproject.toml` contient les configurations de ces différents outils.

Le script `lint_module.sh` permet d'appliquer ces différents outils sur le projet.

## Objectifs

Ici nous allons remplir une librairie permettant de faire quelques calculs mathématiques sur des tableaux de données. Ce test a plusieurs objectifs :
* Ajouter des fonctions à la librairie pour permettre la réalisation de certaines tâches
* Compléter la documentation des fonctions manquantes (voir TODO)
* S'assurer que les fonctions passent les tests, et ajouter des tests si besoin pour vérifier que le coverage est bon.

## Exécution

### Ubuntu

Ce setup a été pensé pour une machine GNU/Linux (Ubuntu par exemple). Si vous n'avez pas accès directement à cet OS, nous vous conseillons d'utiliser une VM.
Dans un soucis de facilité d'exécution, seulement une librairie usuelle de data science est nécessaire (numpy en version < 2.0).
Comme précisé précédemment, l'utilisation d'autres librairies est possible et encouragée, cependant il est nécessaire de tenir l'environnement virtuel à jour !

## Bonne chance !
Le test est difficile ! Nous n'attendons pas un résultat parfait, nous voulons voir si vous êtes capable de résoudre des problèmes et comment vous vous adaptez à une codebase.
Si vous n'arrivez pas à compléter tous les objectifs, pas de panique ! Expliquez votre raisonnement, dans un fichier dédié ou dans les commentaires du code, nous prendrons tout en compte.
Bonne chance :) 
