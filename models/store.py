# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:17:49 2020

@author: PKALYAN
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:43:10 2020

@author: PKALYAN
"""

import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel',lazy = 'dynamic')# this takes in class name
    def __init__(self,name):
        #self.id = id
        self.name = name
        
    def json(self):
        return {'name' : self.name,'items':[i.json() for i in self.items.all()]}
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
        