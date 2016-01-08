import psycopg2


class PostgresqlConnection(object):

	conn = None

	def __init__(self):
		self.connection()

	def get_connection(self):
		if self.conn:
			return self.conn

	def connection(self):
		try:
		    self.conn = psycopg2.connect("dbname='yutengpan' user='yutengpan' host='localhost' ")
		except:
		    print "I am unable to connect to the database"



