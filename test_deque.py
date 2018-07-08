import unittest
from deque import Deque, EmptyDequeException

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.D = Deque(N=5)
  
    def test_empty_deque(self):
        self.assertEqual(self.D.size(),0)
        self.assertTrue(self.D.isEmpty())
        with self.assertRaises(EmptyDequeException) as cm:
            self.D.delete_first()
        expected_msg ="Empty Deque"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyDequeException) as cm:
            self.D.delete_last()
        expected_msg ="Empty Deque"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyDequeException) as cm:
            self.D.first()
        expected_msg ="Empty Deque"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyDequeException) as cm:
            self.D.last()
        expected_msg ="Empty Deque"
        self.assertEquals(cm.exception.message, expected_msg)

    def test_add_delete_element(self):
        self.D.add_first('A')
        self.assertListEqual(['A',None,None,None,None,],self.D._A)
        self.assertEqual(self.D.size(),1)
        self.assertEqual(self.D.first(),'A')
        self.assertEqual(self.D.last(),'A')
        self.assertFalse(self.D.isEmpty())
        self.D.add_last('B')
        self.assertListEqual(['A','B',None,None,None,],self.D._A)
        self.assertEqual(self.D.size(),2)
        self.assertEqual(self.D.first(),'A')
        self.assertEqual(self.D.last(),'B')
        self.D.add_last('C')
        self.D.add_first('AA')
        self.assertListEqual(['A','B','C',None,'AA'],self.D._A)
        self.assertEqual(self.D.size(),4)
        self.assertEqual(self.D.first(),'AA')
        self.D.add_first('AAA')
        self.assertEqual(self.D.size(),5)
        self.assertEqual(self.D.first(),'AAA')
        self.assertEqual(self.D.last(),'C')
        self.assertListEqual(['A','B','C','AAA','AA'],self.D._A)
        self.D.delete_first()
        self.assertEqual(self.D.first(),'AA')
        self.assertEqual(self.D.last(),'C')
        self.D.delete_last()
        self.assertEqual(self.D.first(),'AA')
        self.assertEqual(self.D.last(),'B')
        self.assertListEqual(['A','B',None,None,'AA'],self.D._A)
        self.D.add_last('C')
        self.D.add_last('D')
        self.D.add_last('E')
        self.assertListEqual(['AA','A','B','C','D','E',None,None,None,None],self.D._A)
        self.D.add_last('F')
        self.assertEqual(self.D.first(),'AA')
        self.assertEqual(self.D.last(),'F')
        self.assertEqual(self.D.size(),7)
        self.assertEqual(self.D.delete_first(),'AA')
        self.assertEqual(self.D.delete_last(),'F')
        self.assertListEqual([None,'A','B','C','D','E',None,None,None,None],self.D._A)

if __name__ == '__main__':
    unittest.main(verbosity=2)
