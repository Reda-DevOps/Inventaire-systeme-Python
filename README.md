# Inventaire Système Python

Script Python pour collecter automatiquement les informations
d'une machine et les exporter en CSV.

## Informations collectées
- Hostname et adresse IP
- Système d'exploitation et version
- RAM (totale, utilisée, pourcentage)
- Disque (total, utilisé, pourcentage)
- CPU (coeurs physiques, logiques, utilisation)

## Installation
pip install psutil

## Utilisation
python inventaire.py

Un fichier `inventaire.csv` est généré automatiquement.

## Contexte
Projet réalisé dans le cadre de mon apprentissage.
Ce type de collecte est la base d'un outil de CMDB
(gestion d'inventaire IT).

## Technologies
- Python 3
- psutil
- csv (bibliothèque standard)
