import psycopg

class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=123456 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
            SELECT * FROM "user"
            """)
            return data.fetchall()

    def write(self,data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s )
            """,data)
        self.conn.commit()    
    

    def __del__(self):
        self.conn.close()

