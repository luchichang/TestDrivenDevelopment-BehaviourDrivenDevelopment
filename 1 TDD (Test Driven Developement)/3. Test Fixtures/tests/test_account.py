"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all() # creates the SQL Alchemy table before the test case class
        global ACCOUNT_DATA 
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA=json.load(json_data)



    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close() #closes the db connection after the test case class

    def setUp(self):
        """Truncate the tables"""

    def tearDown(self):
        """Remove the session"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    

