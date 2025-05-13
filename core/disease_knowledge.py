import sqlite3

class DiseaseKnowledge:
    def __init__(self, db_name="AgbakoAI_knowledge_base.db"):
        self.db_name = db_name

    def get_disease_details(self, disease_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM diseases WHERE name=?", (disease_name,))
        disease_details = cursor.fetchone()
        conn.close()
        return disease_details

    def add_disease(self, name, description, symptoms, cure_found=False):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO diseases (name, description, symptoms, cure_found)
                          VALUES (?, ?, ?, ?)''', (name, description, symptoms, cure_found))
        conn.commit()
        conn.close()
