from infra.configs.connection import DBConnectionHandler
from infra.entities.doadores import Doadores
from infra.entities.clientes import Clientes

class DoadoresRepository:
    def select_clientes_doadores(self):
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Doadores)\
                .join(Clientes, Doadores.id_cliente == Clientes.id)\
                .with_entities(
                    Doadores.id_cliente,
                    Doadores.id,
                    Clientes.email,
                    Clientes.nome 
                )\
                .all()
            return data

    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Doadores).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_id_client(self, id_cliente):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Doadores).filter(Doadores.id_cliente==id_cliente).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, id_cliente):
        with DBConnectionHandler() as db:
            try:
                data_isert = Doadores(id_cliente=id_cliente)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Doadores).filter(Doadores.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    #def update_id_cliente(self, id, id_cliente):
    #    with DBConnectionHandler() as db:
    #        try:
    #            db.session.query(Doadores).filter(Doadores.id == id).update({ "id_cliente": id_cliente })
    #            db.session.commit()
    #        except Exception as exception:
    #            db.session.rollback()
    #            raise exception

if __name__ == '__main__':
    dr = DoadoresRepository()

    id1=1
    id2=2
    id3=3
    id_cliente=1
    id_cliente=2
    id_cliente=3
    nome = 'Rodrigo'
    email = 'didier.rda@gmail.com'
    nome2 = 'Didier'
    email2 = 'fisica.didier@gmail.com'
    nome3 = 'Fulano'
    email3 = 'fulano@gmail.com' 
    email4 = 'update@gmail.com'

    # test select
    print(dr.select())

    # test insert
    dr.insert(id_cliente1)
    print(dr.select()) 
    dr.insert(id_cliente2)
    dr.insert(id_cliente3)

    # test join
    print(dr.select_clientes_doadores())

    # test select email
    dr.select_id_client(id_cliente1)
    dr.select_id_cliente("a.gmail.com")

    # test delete
    dr.delete(id1)
    dr.insert(id_cliente1)