-- SQLite
CREATE TABLE IF NOT EXISTS categories(
    label TEXT PRIMARY KEY);
    
CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                description TEXT, 
                categorie_label TEXT, 
                FOREIGN KEY (categorie_label) REFERENCES categories(label) ON DELETE CASCADE);