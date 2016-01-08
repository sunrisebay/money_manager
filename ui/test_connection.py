import psycopg2


class PostgresqlConnection(object):

	conn = None;

	def __init__(self):
		conn = self.connection()

	def get(self):
		if conn:
			return conn

	def connection(self):
		try:
		    conn = psycopg2.connect("dbname='yutengpan' user='yutengpan' host='localhost' ")
		except:
		    print "I am unable to connect to the database"



