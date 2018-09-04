from hello import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self): #setup flask
        self.app = app.test_client()
        self.app.testing = True
        pass

    def test_response(self):
        pop = self.app.get('/')
        assert pop.status_code == 200 # if http code is 200 it will pass

    def test_content(self):
        pop = self.app.get('/')
        assert not len(pop.data) == 0 # check the lengh of the data on the page. if 0 thats mean the page is empty and it will fail  

if __name__ == '__main__':
    unittest.main()
