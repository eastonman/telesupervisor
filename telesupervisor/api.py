import xmlrpc.client


server = xmlrpc.client.ServerProxy('http://localhost:9001')

def getAllProcessInfo():
    return server.supervisor.getAllProcessInfo()
