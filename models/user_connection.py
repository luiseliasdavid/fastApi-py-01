import psycopg

class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=123456 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    

    def __del__(self):
        self.conn.close()

