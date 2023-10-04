import unittest

def grade(grade):

    return grade>=50

class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(grade(50))

if __name__=='__main__':

    unittest.main()