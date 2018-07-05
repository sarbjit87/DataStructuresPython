import unittest
from stacks import StacksList, EmptyStackException

class TestStacks(unittest.TestCase):
    def setUp(self):
        self.S = StacksList()
  
    def test_emptyStack(self):
        self.assertEqual(len(self.S),0)
        self.assertTrue(self.S.isEmpty())
        with self.assertRaises(EmptyStackException) as cm:
            self.S.pop()
        expected_msg = "No Elements in Stack"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyStackException) as cm:
            self.S.top()
        expected_msg = "No Elements in Stack"
        self.assertEquals(cm.exception.message, expected_msg)

    def test_push_pop_top_len(self):
        self.S.push('A')
        self.S.push('B')
        self.assertEqual(len(self.S),2)
        self.assertFalse(self.S.isEmpty())
        self.assertEqual(self.S.top(),'B')
        self.assertEqual(len(self.S),2)
        self.assertEqual(self.S.pop(),'B')
        self.assertEqual(len(self.S),1)
        self.S.push('C')
        self.assertEqual(self.S.pop(),'C')
        self.assertEqual(self.S.pop(),'A')
        self.assertEqual(len(self.S),0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
