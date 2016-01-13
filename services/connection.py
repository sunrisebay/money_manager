import psycopg2
from common import env_config

class PostgresqlConnection(object):

	conn = None

	def __init__(self):
		self.connection()

	def get_connection(self):
		if self.conn:
			return self.conn

	def connection(self):
		try:
		    self.conn = psycopg2.connect("dbname='" + 
		    	env_config.get('db','dbname') + 
		    	"' user='" + env_config.get('db','username') 
		    	+ "' host='localhost' ")
		except:
		    print "I am unable to connect to the database"
		    



