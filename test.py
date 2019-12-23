import flask
import unittest
import pytest
import requests
from spell_check.spell import *

server_address="http://127.0.0.1:5000"
app.config["WTF_CSRF_ENABLED"] = False

class TestSpellFunctions(unittest.TestCase):	
def test_index_page():
  r = requests.get(server_address + '/')
  self.assertEqual(response.status_code, 200)

def test_register_page():
  r = requests.get(server_address + '/register')
  self.assertEqual(response.status_code, 200)

def test_login_page():
  r = requests.get(server_address + '/login')
  self.assertEqual(response.status_code, 200)
  
def test_checker_page():
  r = requests.get(server_address + '/checker')
  self.assertEqual(response.status_code, 200)
  
def login(username, password, 2fa):
return client.post('/login', data=dict(username=uname, password=pword, 2fa=2fa), follow_redirects=True)
  
if __name__ == '__main__':
	unittest.main()	
