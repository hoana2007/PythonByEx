import unittest
def modthree(x):                             #defining the function
      return x%3

class Tests(unittest.TestCase):
      def test(self):                                  #test method
               self.assertEqual(modthree(4),1)

if __name__ == '__main__':
    unittest.main()

