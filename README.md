# Projet de Gestion Collaborative de Cards et Boards


## Description du projet

Ce projet consiste en une **extension web** permettant à un utilisateur (User) d’enregistrer et organiser facilement des contenus variés (liens, images, textes) sous forme de **cards**. Ces cards sont ensuite classées dans des **boards**.

- Un **User** peut créer une infinité de **boards**.
- Un **board** peut contenir une infinité de **cards**.
- Chaque **card** appartient obligatoirement à un **board**.

---

### Contenu d’une Card

Chaque card peut contenir les informations suivantes :

- **URL** : lien vers la source.
- **Texte extrait** de la source.
- **Image** associée.
- **Note** ajoutée par l’utilisateur.
- **Tags** pour faciliter la recherche.
- **Résumé** des informations importantes.

---

### Objectif fonctionnel

Ce système permet à des utilisateurs de collaborer et partager de la veille sur différents sujets ou domaines, **en équipe**.

---

## Infrastructure & Technologies utilisées

- **AWS LightSail** pour l’hébergement de l’application.
- **AWS Secrets Manager** pour la gestion sécurisée des secrets et des clés.
- **Politiques IAM** pour la gestion des permissions et accès.
- **DynamoDB** comme base de données NoSQL.
- **Route 53** pour la gestion du nom de domaine et DNS.

---

## État actuel & défis

L’application n’est pas encore pleinement fonctionnelle sur l’infrastructure AWS LightSail, en raison de plusieurs difficultés techniques rencontrées lors du déploiement.

Mise en place du projet fonctionnel de secours:
- Fonction du projet, sans le déploiement AWS
- Utilisation de Flask
- Utilisation de MongoDB
- Mise en place d'un Docker, docker-compose
   
---

## Perspectives & évolutions prévues

- Mise en place d’un **pipeline CI/CD** pour automatiser et faciliter le déploiement et le développement continu.
- Intégration d’un **CDN CloudFront** pour améliorer la distribution des contenus.
- Utilisation de **S3** comme solution de stockage pour les images et autres fichiers.
- Une migration vers **AWS EC2** permettrait d'avoir un contrôle plus fin sur l'infrastructure serveur, facilitant la gestion des ressources et la personnalisation de l'environnement pour optimiser les performances de l'application.

---
## Equipe Back-end / DevOps: 
- [Fouad](https://github.com/fouuuadi)
- [Arnaud](https://github.com/Jeck0v)

## Conclusion

Ce projet vise à offrir une solution collaborative efficace et évolutive pour la collecte et l’organisation d’informations diverses, en tirant parti des services AWS pour une infrastructure robuste et scalable.



*Dernière mise à jour : Mai 2025*

