try:
    from HRMS_app import app
    import unittest
    from unittest.mock import patch
    import json
    from HRMS_app.models import db, User
    import pymysql
    pymysql.install_as_MySQLdb()
    import flask
except Exception as e:
    print("Some module is missing {}".format(e))

db.init_app(app)

class HRMS(unittest.TestCase):

    def test_login(self):
        tester = app.test_client(self)
        test_data = {'username':'admin', 'password':'Admin@12345'}
        response = tester.post('/login',data = test_data)
        status_code = response.status_code
        self.assertEqual(status_code, 308)

    def test_insert(self):
        tester = app.test_client(self)
        test_data = {
            'name': 'Emma',
            'email':'emma@gmail.com',
            'phone':'6102347566',
            'address':'California',
            'education':'Masters',
            'experience':'6'
        }
        response = tester.post('/insert',data = test_data)
        status_code = response.status_code
        self.assertEqual(status_code,302)

    def test_update(self):
        tester = app.test_client(self)
        test_data = {
            'id':'2',
            'name': 'Peter',
            'email': 'peter@gmail.com',
            'phone': '4842989004',
            'address': 'Chicago',
            'education': 'Masters',
            'experience': '10'
        }
        response = tester.post('/update', data=test_data)
        status_code = response.status_code
        self.assertEqual(status_code, 302)

    def test_show(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()