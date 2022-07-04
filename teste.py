from infra.configs.connection import DBConnectionHandler
from infra.repository.clientes_repository import ClientesRepository
from infra.repository.doadores_repository import DoadoresRepository
from infra.repository.livros_repository import LivrosRepository

if __name__ == '__main__':

    # teste livro
    titulo1 = 'Dom Casmurro'
    genero1 = 'Romance'
    titulo2 = 'Forest Gump'
    genero2 = 'Drama'
    titulo3 = 'Chapeuzinho Vermelho'
    genero3 = 'Infantil'
    titulo4 = 'Memórias Postumas'
    genero4 = 'Romance'

    lr = LivrosRepository()
    print(lr.select())
    #lr.select_livros_genero("Drama")
    #lr.select_livros_genero("Romance")
    #lr.select_livros_genero("Guerra")
    #lr.insert(titulo3, genero3)  - FAZER DEBUG
    #lr.delete(titulo3)
    #lr.update_genero(titulo3, genero2)

    dr = DoadoresRepository()

    id1=1
    id2=2
    id3=3
    id4=4
    id5=5

    id_cliente1=1
    id_cliente2=2
    id_cliente3=3
    id_cliente4=4
    id_cliente5=5

    id_doador1=1
    id_doador2=2
    id_doador3=3
    id_doador4=4
    id_doador5=5

    nome = 'Rodrigo'
    email = 'didier.rda@gmail.com'
    nome2 = 'Didier'
    email2 = 'fisica.didier@gmail.com'
    nome3 = 'Fulano'
    email3 = 'fulano@gmail.com' 
    email4 = 'update@gmail.com'

    lr.insert(id_doador4, titulo4, genero4) #- FAZER DEBUG
    lr.insert(id_doador4, titulo4, genero4) #- FAZER DEBUG
    lr.insert(id_doador4, titulo4, genero4) #- FAZER DEBUG
    lr.update_status(id4)
    lr.delete(id1)

    lr.select_livros_genero("Drama")
    lr.select_livros_genero("Romance")
    lr.select_livros_genero("Guerra")
    lr.insert(titulo3, genero3) #- FAZER DEBUG
    lr.delete(titulo3)
    lr.update_genero(titulo3, genero2)
    # test select
    print(dr.select())

    # test insert
    dr.insert(id_cliente5)
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

    # Teste ConnectionHandler 
    dbch = DBConnectionHandler()

    # Testes Clientes
    cr = ClientesRepository()
    id1=1
    id2=2
    nome1 = 'Rodrigo'
    email1 = 'didier.rda@gmail.com'
    nome2 = 'Didier'
    email2 = 'fisica.didier@gmail.com'
    nome3 = 'Fulano'
    email3 = 'fulano@gmail.com' 
    email4 = 'update@gmail.com'

    # test insert
    cr.insert(nome1, email1) #ok
    cr.insert(nome2, email2) #ok
    cr.insert(nome3, email3) #ok

    # test select
    print(cr.select()) #ok

    # test select email
    cr.select_cliente_email(email1) #ok
    cr.select_cliente_email("a.gmail.com") #ok but - se not string notok

    # test delete
    cr.delete(id1) #ok
    cr.select_cliente_email(email1) #ok
    cr.insert(nome1, email1)

    # test update 
    update_email='meuemail.@gmail.com'
    cr.update_email(id2, update_email)
    print(cr.select())

    # Testes Doadores