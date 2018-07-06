import unittest
from queues import Queue, FullQueueException, EmptyQueueException

class TestQueues(unittest.TestCase):
    def setUp(self):
        self.Q = Queue(N=5)
  
    def test_setup(self):
        "Test for Empty Queue"
        self.assertEqual(self.Q.size(),0)
        self.assertTrue(self.Q.isEmpty())
        self.assertFalse(self.Q.isFull())
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.dequeue()
        expected_msg = "Queue is empty"
        self.assertEquals(cm.exception.message, expected_msg)
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.front()
        expected_msg = "Queue is empty"
        self.assertEquals(cm.exception.message, expected_msg)

    def test_enqueue_dequeue(self):
        self.Q.enqueue('A')
        self.Q.enqueue('B')
        self.assertEqual(self.Q.size(),2)
        self.assertFalse(self.Q.isEmpty())
        self.assertFalse(self.Q.isFull())
        self.Q.enqueue('C')
        self.Q.enqueue('D')
        self.Q.enqueue('E')
        self.assertFalse(self.Q.isEmpty())
        self.assertTrue(self.Q.isFull())
        self.assertEqual(self.Q.front(),'A')
        with self.assertRaises(FullQueueException) as cm:
            self.Q.enqueue('F')
        expected_msg = "Queue is full"
        self.assertEquals(cm.exception.message, expected_msg)
        self.assertEqual(self.Q.size(),5)
        self.Q.dequeue()
        self.assertEqual(self.Q.size(),4)
        self.assertFalse(self.Q.isEmpty())
        self.assertFalse(self.Q.isFull())
        self.Q.enqueue('G')
        self.assertEqual(self.Q.front(),'B')
        self.assertEqual(self.Q.size(),5)
        self.Q.dequeue()
        self.Q.dequeue()
        self.Q.dequeue()
        self.Q.dequeue()
        self.assertEqual(self.Q.size(),1)
        self.assertEqual(self.Q.front(),'G')
        self.assertFalse(self.Q.isEmpty())
        self.assertFalse(self.Q.isFull())
        self.Q.dequeue()
        self.assertEqual(self.Q.size(),0)
        with self.assertRaises(EmptyQueueException) as cm:
            self.Q.dequeue()
        expected_msg = "Queue is empty"
        self.assertEquals(cm.exception.message, expected_msg)
        self.assertTrue(self.Q.isEmpty())
        self.assertFalse(self.Q.isFull())

if __name__ == '__main__':
    unittest.main(verbosity=2)
