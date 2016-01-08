import psycopg2
from services.connection import PostgresqlConnection as pgconn

class PostgresqlHandlers(object):

    cur = None

    def insert_values(self):
        return None

    def remove_values(self):
        return None

    def modify_values(self):
        return None

    def check_accounts(self):
        return None

    def add_account(self):
        return None

    def remove_account(self):
        return None

    def check_account(self):
        return None

    def print_results(self, results):
        print "\nShow me the results:\n"
        for result in results:
            print "   ", result[1], result[2], result[3]

    def set_cursor(self):
        if not self.cur:
            _pgconn = pgconn()
            self.cur = _pgconn.get_connection().cursor()

    def get_cursor(self):
        if self.cur:
            return cur

    def execute_statements(self,statements):
        if self.cur:
            self.cur.execute(statements)
            rows = self.cur.fetchall()
            self.print_results(rows) 



# cur.execute("""SELECT * from persons""")
# rows = cur.fetchall()
# print "\nShow me the databases:\n"
# for row in rows:
#     print "   ", row[0], row[1], row[2]
