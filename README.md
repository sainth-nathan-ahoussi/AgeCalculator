# Calculateur d'Âge

## Introduction

**Calculateur d'Âge** est une application Python interactive basée sur Tkinter. Elle permet aux utilisateurs de calculer leur âge à partir de leur année de naissance. L'application vérifie la validité des entrées et affiche si l'utilisateur est majeur ou mineur.

C'est un excellent projet pour comprendre les bases de la création d'interfaces utilisateur avec Tkinter et la gestion des données utilisateur.

## Table des Matières

- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Améliorations Futures](#améliorations-futures)
- [Exemples](#exemples)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

## Fonctionnalités

- **Validation des Entrées** : Vérifie que l'année saisie est valide, entre 1900 et l'année actuelle.
- **Calcul de l'Âge** : Calcule l'âge de l'utilisateur à partir de l'année saisie.
- **Statut de Majorité** :
  - Si l'utilisateur est majeur, affiche un message humoristique.
  - Si l'utilisateur est mineur, indique le nombre d'années restantes avant la majorité.
- **Interface Graphique** : Une interface simple et intuitive créée avec Tkinter.

## Installation

1. **Cloner le Dépôt** :
   ```bash
   git clone https://github.com/sainth-nathan-ahoussi/AgeCalculator.git
   cd calculateur-age
   ```

2. **Installer Python** :
   Assurez-vous d'avoir Python 3.x installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org).

3. **Installer Tkinter** :
   Tkinter est généralement inclus avec Python. Si ce n'est pas le cas, installez-le via votre gestionnaire de paquets :
   - **Windows/Linux** :
     ```bash
     sudo apt-get install python3-tk
     ```
   - **Mac** :
     Assurez-vous que Tkinter est inclus dans votre installation Python.

4. **Exécuter le Script** :
   ```bash
   python CalculateurAge.py
   ```

## Utilisation

1. Lancez l'application.
2. Entrez votre année de naissance dans le champ prévu.
3. Cliquez sur le bouton "Calculer".
4. L'application affichera votre âge et votre statut de majorité.

## Améliorations Futures

- Ajouter des messages personnalisés pour différents groupes d'âge.
- Ajouter la possibilité de calculer l'âge à une date spécifique autre que l'année actuelle.
- Intégrer des options de style pour personnaliser l'apparence de l'interface.
- Traduire l'application dans plusieurs langues.

## Exemples

### Exemple de Fonctionnement
1. Entrée de l'année : `2005`
2. Résultat :
   - Âge : `18`
   - Statut : *"Majeur !! Alors, comme ça on est Majeur, petit coquin :)"*

3. Entrée de l'année : `2010`
4. Résultat :
   - Âge : `13`
   - Statut : *"Mineur !! Vous êtes majeur dans 5 ans !! Soyez patient"*

## Contributeurs

- **AHOUSSI Sainth-Nathan** – *Développeur et Mainteneur*

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
