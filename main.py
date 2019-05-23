import sys
clientes = 'pablo,ricardo,'


def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_coma()
    else:
        print('client already is in the client\'s list')

def _add_coma():
    global clientes
    clientes +=','

def list_clients():
    global clientes
    print(clientes)

def update_client(client_name, update_client_name):
    global clientes
    if client_name in clientes :
        clientes = clientes.replace(client_name+',', update_client_name+',')
    else:
        print ('CLient is not in clients list')

def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes = clientes.replace(client_name+',','')
    else:
        print ("client is not in clients list")

def _printWelcome():
    print ('Welcome To Platzi Ventas')
    print ('*'*50)
    print ('Whay would you like to do day?')
    print ('[c]reate client')
    print ('[L]ist Clients')
    print ('[D]elete client')
    print ('[U]pdate')
    print ('[S]earch Client')

def search_client(client_name):
    clients_list = clientes.split(',')

    for client in clients_list:
        if(client_name == client):
            return True
    return False

def __get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name= None
            break
    if not client_name:
        sys.exit()
    return client_name

if __name__ == '__main__':
    _printWelcome()
    command=input()
    command = command.upper()
    if command == 'C':
        clientName= __get_client_name()
        create_client(clientName)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command== 'D':
        client_name = __get_client_name()
        delete_client(client_name)
        list_clients()
    elif command== 'U':
        client_name = __get_client_name()
        update_client_name = input("What is the updated cliente name?")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = __get_client_name()
        found = search_client(client_name)
        if found:
            print("The client is in the client's List")
        else:
            print("The cliente: {} is not in our client's List",format(client_name))
    else:
        print(' invalid command')



