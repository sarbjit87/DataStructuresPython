import unittest
from single_linked_lists_queues import *

class TestQueues(unittest.TestCase):
    def setUp(self):
        self.Q = Queue()
  
    def test_setup(self):
        "Test for Empty Queue"
        self.assertEqual(self.Q.size(),0)
        self.assertTrue(self.Q.isEmpty())
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.dequeue()
        expected_msg = "No Elements in Queue"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.front()
        expected_msg = "No Elements in Queue"
        self.assertEquals(cm.exception.message, expected_msg)

    def test_enqueue_dequeue(self):
        self.Q.enqueue('A')
        self.Q.enqueue('B')
        self.assertEqual(self.Q.size(),2)
        self.assertFalse(self.Q.isEmpty())
        self.Q.enqueue('C')
        self.Q.enqueue('D')
        self.Q.enqueue('E')
        self.assertFalse(self.Q.isEmpty())
        self.assertEqual(self.Q.front(),'A')
        self.assertEqual(self.Q.size(),5)
        self.Q.dequeue()
        self.assertEqual(self.Q.size(),4)
        self.assertFalse(self.Q.isEmpty())
        self.Q.enqueue('G')
        self.assertEqual(self.Q.front(),'B')
        self.assertEqual(self.Q.size(),5)
        self.assertEqual(self.Q.dequeue(),'B')
        self.assertEqual(self.Q.dequeue(),'C')
        self.Q.dequeue()
        self.Q.dequeue()
        self.assertEqual(self.Q.size(),1)
        self.assertEqual(self.Q.front(),'G')
        self.assertFalse(self.Q.isEmpty())
        self.assertEqual(self.Q.dequeue(),'G')
        self.assertEqual(self.Q.size(),0)
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.dequeue()
        expected_msg = "No Elements in Queue"
        self.assertEquals(cm.exception.message, expected_msg)
        self.assertTrue(self.Q.isEmpty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
