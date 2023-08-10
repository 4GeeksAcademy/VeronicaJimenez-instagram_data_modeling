import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    followers = relationship ('Followers', backref = 'followers', lazy=True)  
    comments = relationship ('Comments', backref = 'comments', lazy=True)  
    posts = relationship ('Posts', backref = 'posts', lazy=True) 

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column (Integer, ForeignKey('user.id'), nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    posts_id = Column (Integer, ForeignKey('posts.id'), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post = Column(String(250), nullable=False)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    media_id = Column (Integer, ForeignKey('media.id'), nullable=False)
    comments = relationship ('Comments', backref = 'comments', lazy=True) 

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    posts = relationship ('Posts', backref = 'posts', lazy=True) 


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
