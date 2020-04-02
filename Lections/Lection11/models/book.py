TABLE_NAME = 'books'
TABLE = (
    "CREATE TABLE `books` ("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`name` varchar(14) NOT NULL,"
    "`description` varchar(255) NOT NULL,"
    "`writerId` int(11) NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")