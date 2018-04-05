import xmlrpc.client
import logging


server = xmlrpc.client.ServerProxy('http://localhost:9001')


def getAllProcessInfo():
    """
    @return list
    """
    try:
        return server.supervisor.getAllProcessInfo()
    except ConnectionRefusedError:
        logging.error('XMLRPC connection refused!')
        return 1

def getProcessInfo(name):
    return server.supervisor.getProcessInfo(name)
