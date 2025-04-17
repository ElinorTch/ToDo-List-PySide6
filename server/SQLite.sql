-- SQLite
CREATE TABLE IF NOT EXIST categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    label TEXT);
    
CREATE TABLE IF NOT EXIST tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                description TEXT, 
                categorie_id INTEGER, 
                FOREIGN KEY (categorie_id) REFERENCES categories(id) ON DELETE CASCADE);