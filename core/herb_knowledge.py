import sqlite3

class HerbKnowledge:
    def __init__(self, db_name="AgbakoAI_knowledge_base.db"):
        self.db_name = db_name
    
    def get_herb_details(self, herb_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM herbs WHERE name=?", (herb_name,))
        herb_details = cursor.fetchone()
        conn.close()
        return herb_details

    def add_herb(self, name, description, usage, chemical_properties):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO herbs (name, description, usage, chemical_properties)
                          VALUES (?, ?, ?, ?)''', (name, description, usage, chemical_properties))
        conn.commit()
        conn.close()
