
from infra.configs.connection import DBConnectionHandler
from infra.repository.clientes_repository import ClientesRepository
from infra.repository.doadores_repository import DoadoresRepository
from infra.repository.livros_repository import LivrosRepository

if __name__ == '__main__':

    # Teste ConnectionHandler 
    dbch = DBConnectionHandler()

    # Testes Clientes
    cr = ClientesRepository()
    id1=1
    nome1 = 'Rodrigo'
    email1 = 'didier.rda@gmail.com'
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

    # Testes Doadores