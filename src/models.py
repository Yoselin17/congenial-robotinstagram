import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class User (Base):
        __tablename__ = "user"
        id = Column(Integer,primary_key=True)
        User_correo = Column(String(50))
        User_contraseña = Column(String(50))

class Capitulo  (Base):
                __tablename__ = "capitulo"
                id = Column (Integer,primary_key=True)
                capitulo_capitulo = Column(String(70))
                capitulo_nombre = Column (String(70))
                capitulo_informacion = Column (String(70))
                capitulo_detalle = Column (String(70))

class Personaje (Base):
    __tablename__ = "personaje"
    id = Column (Integer,primary_key=True)         
    nombre = Column (String(70))              
    imagen = Column (String(70))
    specie = Column (String(70))

class FavoritoCapitulo(Base):
            __tablename__ = "FavoritoCapitulo"
            id = Column (Integer,primary_key=True)
            capitulo_id = Column(Integer, ForeignKey("capitulo.id"))
            user_id = Column(Integer, ForeignKey("user.id"))  
            relacioncapitulo = relationship(Capitulo)
            relacionuser = relationship(User)


                
class FavoritoPersonaje (Base):
            __tablename__ = "FavoritoPersonaje"
            id= Column (Integer,primary_key=True)
            FavoritoPersonaje_id = Column(Integer, ForeignKey("personaje.id"))
            user_id = Column(Integer, ForeignKey("user.id"))  
            relacionpersonaje = relationship(Personaje)
            relacionuser = relationship(User)





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e