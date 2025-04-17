-- SQLite
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    label TEXT);
    
CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                description TEXT, 
                categorie_id INTEGER, 
                FOREIGN KEY (categorie_id) REFERENCES categories(id) ON DELETE CASCADE);