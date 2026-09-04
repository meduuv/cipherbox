import unittest
from cipherbox.core import derive_key,make_salt
class Tests(unittest.TestCase):
 def test_key_length(self): self.assertEqual(len(derive_key('test-password',make_salt())),32)
 def test_short_salt(self):
  with self.assertRaises(ValueError): derive_key('x',b'1')
if __name__=='__main__': unittest.main()
