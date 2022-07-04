from infra.configs.connection import DBConnectionHandler
from infra.entities.livros import Livros
from sqlalchemy.orm.exc import NoResultFound

class LivrosRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Livros).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_livros_genero(self, genero):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Livros).filter(Livros.genero==genero).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, id_doador, titulo, genero):
        with DBConnectionHandler() as db:
            try:
                data_isert = Livros(id_doador=id_doador, status=True, titulo=titulo, genero=genero)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Livros).filter(Livros.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_genero(self, id, genero):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Livros).filter(Livros.id == id).update({ "genero": genero})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_titulo(self, id, titulo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Livros).filter(Livros.id == id).update({ "titulo": titulo})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_status(self, id):
        with DBConnectionHandler() as db:
            try:
                status = db.session.query(Livros).filter(Livros.id == id).status
                new_status = not status
                db.session.query(Livros).filter(Livros.id == id).update({ "status": new_status})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

if __name__ == '__main__':
    titulo = 'Dom Casmurro'
    genero = 'Romance'
    titulo2 = 'Forest Gump'
    genero2 = 'Drama'
    titulo3 = 'Chapeuzinho Vermelho'
    genero3 = 'Infantil'
    lr = LivrosRepository()
    print(lr.select())
    #lr.select_livros_genero("Drama")
    #lr.select_livros_genero("Romance")
    #lr.select_livros_genero("Guerra")
    #lr.insert(titulo3, genero3)  - FAZER DEBUG
    #lr.delete(titulo3)
    #lr.update_genero(titulo3, genero2)
