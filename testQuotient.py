import unittest
from Divide import Divide

class TestQuotient(unittest.TestCase):
  def test_Quotient(self):
  	self.assertEqual(Divide(9,3), 3.0)
  	self.assertEqual(Divide(21.69,3), 7.23)
  	
  def test_ZeroDivisionError(self):
    self.assertRaises(ZeroDivisionError)
      
	
		
if __name__ == '__main__':
    unittest.main()
