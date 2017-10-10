import unittest
from Divide import Divide

class TestDivide(unittest.TestCase):
  def test_input_is_not_a_string(self):
    self.assertRaises(TypeError,Divide, ["string"])
    
  def test_input_is_integer(self):
    self.assertEqual(Divide(9,3), 3.0)
	
  def test_input_is_float(self):
    self.assertEqual(Divide(21.69,3), 7.23)
		
if __name__ == '__main__':
    unittest.main()
