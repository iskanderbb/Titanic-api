from swagger_server.app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'titanicdb'
app.config['MYSQL_DATABASE_HOST'] = 'mysqldb'
mysql.init_app(app)
