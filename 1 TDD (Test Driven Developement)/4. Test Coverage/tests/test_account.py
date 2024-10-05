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
    def test_account_creation(self):
        """test for account creation"""
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()
        self.assertEqual(account.all(), 1)


    def test_all_account_create(self):
        """test for all account creation"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
    

