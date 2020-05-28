import unittest

from app import app


class BasicTestCase(unittest.TestCase):
    def test_home(self):
	    tester = app.test_client(self)
	    response = tester.get('/', content_type='html/text')
	    self.assertEqual(response.status_code, 200)

class TestCase(unittest.TestCase):
	def test_delete(self):
		tester = app.test_client(self)
		response = tester.get('/delete', content_type='html/text')
		self.assertEqual(response.status_code,405)



if __name__ == '__main__':
    unittest.main()
