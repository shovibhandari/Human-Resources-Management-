from HRMS_app import app
from HRMS_app.models import db
import pymysql
pymysql.install_as_MySQLdb()

db.init_app(app)

if __name__ == "__main__":
    app.run()