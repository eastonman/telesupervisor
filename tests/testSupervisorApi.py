import sys
sys.path.append("..")
import telesupervisor.api

data = telesupervisor.api.getAllProcessInfo()[0]

print(data['name'])

