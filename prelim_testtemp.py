import unittest

def tempConver(c,f):

    return c/f

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(tempConver(40,20),2)

if __name__=='__main__':

    unittest.main()