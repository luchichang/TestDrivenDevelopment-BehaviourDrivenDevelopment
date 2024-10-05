# importing from the module
import logging
from sqlalchemy.sql import func
from models import db

#  Initializing the logger Instance for the flask application
logger = logging.getLogger()

# class data validation Error with Exception as a base class
class DataValidationError(Exception):
    """used for data validation error when deserializing"""

class Account(db.Model):
    """class that represents the Account DB model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(32), nullable=True )
    disabled = db.Column(db.Boolean(), nullable=False, default=False)
    date_joined = db.Column(db.Date, nullable=False, server_default=func.now())

    def __repr__(self):
        return '<Account %r>' % self.name
    
    def to_dict(self) -> dict:
        """Serialize the class as a dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def from_dict(self, data: dict) -> None:
        """Sets attribute from the dictionary"""
        for key, value in data:
            setattr(self, key, value)

    def create(self):
        """creates an account in the database"""
        logger.info("creating %s", self.name)
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates an account in the database"""
        logger.info("saving %s", self.name)
        if not  self.id:
            raise DataValidationError("update called with Empty Id Field")
        db.session.commit()
    
    def delete(self):
        """Deletes an account"""
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    ##################################################
    # CLASS METHODS
    ##################################################

    @classmethod
    def all(cls) -> list:
        """Returns all of the account in database"""
        logger.info("processing all Accounts")
        return cls.query.all()
    
    @classmethod
    def find(cls, account_id: int):
        """Finds an account by ID
        :param account_id: the id of the account to find
        :type account_id: int
        :return: an instance with account_id or none if not found
        :rtype: Account
        """
        logger.info("processing lookup for %s...", account_id)
        return cls.query.get(account_id)





