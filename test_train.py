import unittest
# We have to do some weird stuff to import the file due to the name
import imp
train = imp.load_source('train.5m', 'train.5m.py')


class TestTrain(unittest.TestCase):

    def test_can_get_ontime(self):
        status = 'On time'
        self.assertEqual(train.shorten(status), '0')

    def test_can_get_delay(self):
        status = '1m late'
        self.assertEqual(train.shorten(status), '+1')

    def test_can_get_early(self):
        status = '1m early'
        self.assertEqual(train.shorten(status), '-1')

    def test_can_shorten_tens_of_minutes(self):
        status = '11m late'
        self.assertEqual(train.shorten(status), '+11')

    def test_will_use_last_item_in_array(self):
        statuses = ['On time', '2m late', 'On time', 'On time', 'On time']
        self.assertEqual(train.get_status(statuses), '0')


if __name__ == '__main__':
    unittest.main()
