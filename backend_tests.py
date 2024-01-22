import unittest
from app import app  
from flask_testing import TestCase
import psycopg2

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['DATABASE'] = {
            'dbname': 'divum',
            'user': 'postgres',
            'password': 'postgres',
            'host': 'localhost',
            'port': '5432'
        }
        return app

    def setUp(self):
        self.connection = psycopg2.connect(
            dbname=app.config['DATABASE']['dbname'],
            user=app.config['DATABASE']['user'],
            password=app.config['DATABASE']['password'],
            host=app.config['DATABASE']['host'],
            port=app.config['DATABASE']['port']
        )
        self.cursor = self.connection.cursor()
        

    def tearDown(self):
        
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def test_add_user(self):
        self.client = self.app.test_client()
        response = self.client.post('/submit', data=dict(
            email='test@example.com',
            fname='John',
            lname='Doe',
            mobile='1234567890',
            dob='2000-01-01',
            address='123 Main St'
        ))
        self.assertEqual(response.status_code, 302)


    def test_edit_user(self):
        self.client = self.app.test_client()
        response = self.client.post('/update/test@example.com', data=dict(
            email='new_email@example.com',
            fname='Jane',
            lname='Smith',
            mobile='9876543210',
            dob='1995-12-31',
            address='456 Elm St'
        ))
        self.assertEqual(response.status_code, 302)
        
    def test_delete_user(self):
        self.client = self.app.test_client()
        response =self.client.get('/delete/test@example.com')
        self.assertEqual(response.status_code, 302)
        
        

if __name__ == '__main__':
    unittest.main()
