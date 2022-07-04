from infra.configs.connection import DBConnectionHandler
from infra.entities.clientes import Clientes
from sqlalchemy.orm.exc import NoResultFound

class ClientesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Clientes).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_cliente_email(self, email):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Clientes).filter(Clientes.email==email).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, nome, email):
        with DBConnectionHandler() as db:
            try:
                data_isert = Clientes(nome=nome, email=email)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Clientes).filter(Clientes.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_email(self, id, email):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Clientes).filter(Clientes.id == id).update({ "email": email })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
if __name__ == '__main__':
    cr = ClientesRepository()
    id1=1
    nome = 'Rodrigo'
    email = 'didier.rda@gmail.com'
    nome2 = 'Didier'
    email2 = 'fisica.didier@gmail.com'
    nome3 = 'Fulano'
    email3 = 'fulano@gmail.com' 
    email4 = 'update@gmail.com'

    # test insert
    cr.insert(nome1, email1)
    cr.insert(nome2, email2)
    cr.insert(nome3, email3)

    # test select
    print(cr.select())

    # test select email
    cr.select_cliente_email(email1)
    cr.select_cliente_email("a.gmail.com")

    # test delete
    cr.delete(id1)
    cr.select_cliente_email(email1)
    cr.insert(nome1, email1)

    # test update 
    cr.update_email(id1, update_email)
    print(cr.select())
    #titulo = 'Dom Casmurro'
    #genero = 'Romance'
    #titulo2 = 'Forest Gump'
    #genero2 = 'Drama'
    #titulo3 = 'Chapeuzinho Vermelho'
    #genero3 = 'Infantil'
    #cr = ClientesRepository()
    #print(cr.select())
    #lr.select_livros_genero("Drama")
    #lr.select_livros_genero("Romance")
    #lr.select_livros_genero("Guerra")
    #lr.insert(titulo3, genero3)  - FAZER DEBUG
    #lr.delete(titulo3)
    #lr.update_genero(titulo3, genero2)
