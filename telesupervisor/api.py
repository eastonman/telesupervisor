import xmlrpc.client


server = xmlrpc.client.ServerProxy('http://localhost:9001')

def getAllProcessInfo():
    """
    @return list
    """
    return server.supervisor.getAllProcessInfo()


def getProcessInfo(name):
    return server.supervisor.getProcessInfo(name)
