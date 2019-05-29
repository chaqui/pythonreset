import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA= ['name','company','email','position']
clientes = []

def _initialize_clients_form_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clientes.append(row)

def _save_clients_to_storage():
    tmp_tabñle_name ='{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_tabñle_name,mode="w") as f:
        writer= csv.DictWriter(f,fieldnames= CLIENT_SCHEMA)
        writer.writerows(clientes)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_tabñle_name,CLIENT_TABLE)

def create_client(client):
    global clientes
    if client not in clientes:
        clientes.append(client)
    else:
        print('client already is in the client\'s list')

def list_clients():
    print("uid |name | company | email |position ")
    print("**************************************")
    for idx, client in enumerate(clientes):
        print("{uid} |{name} | {company} | {email} |{position} ".format(
            uid=idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))

def update_client(index, update_client):
    global clientes
    clientes[index] = update_client

def delete_client(client_name):
    global clientes
    found = search_client(client_name)
    if found > -1:
        del clientes[found]
    else:
        print("The cliente: {} is not in our client's List".format(client_name))

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
    for idx, client in enumerate(clientes):
        if(client_name == client.get("name")):
            return idx
    return -1

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
def __get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field

def __getClient():
    client = {
            'name': __get_client_field('name'),
            'company': __get_client_field('company'),
            'email': __get_client_field('email'),
            'position': __get_client_field('position'),
        }
    return client
if __name__ == '__main__':
    _initialize_clients_form_storage()
    _printWelcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = __getClient()
        create_client(client)

    elif command == 'L':
        list_clients()
    elif command== 'D':
        client_name = __get_client_name()
        delete_client(client_name)
    elif command== 'U':
        client_name = __get_client_name()
        found = search_client(client_name)
        if found > -1:
            print("values of client modified")
            client_update = __getClient()
            update_client(found, client_update)
        else:
            print("The cliente: {} is not in our client's List".format(client_name))
    elif command == 'S':
        client_name = __get_client_name()
        found = search_client(client_name)
        if found > -1:
            print("The client is in the client's List")
        else:
            print("The cliente: {} is not in our client's List".format(client_name))
    else:
        print(' invalid command')
    _save_clients_to_storage()



