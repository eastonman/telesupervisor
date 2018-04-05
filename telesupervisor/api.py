import xmlrpc.client
import logging


server = xmlrpc.client.ServerProxy('http://localhost:9001')

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"

logging.basicConfig(filename='tele.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

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
