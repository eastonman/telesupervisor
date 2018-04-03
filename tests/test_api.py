import sys
sys.path.append("..")
import telesupervisor.api
import unittest

# data = telesupervisor.api.getAllProcessInfo()[0]

# print(data['name'])


class TestSupervisorApi(unittest.TestCase):
    def test_getAllProcessInfo(self):
        assert type(telesupervisor.api.getAllProcessInfo()) == list


if __name__ == '__main__':
    unittest.main()
