import unittest

def areaSQuare(length,width,height):

    return length*width*height

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(areaSQuare(8,9,9),648)

if __name__=='__main__':

    unittest.main()