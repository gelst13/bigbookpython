import unittest
import birthday_paradox


class TestBirthdayParadox(unittest.TestCase):
    def test_generate_birthdays(self):
        self.assertEqual(len(birthday_paradox.generate_birthdays(2)), 2)
        self.assertEqual(len(birthday_paradox.generate_birthdays(1)), 1)
        self.assertEqual(len(birthday_paradox.generate_birthdays(0)), 0)
        self.assertEqual(len(birthday_paradox.generate_birthdays(100)), 100)
    
    def test_readable_dates(self):
        self.assertEqual(len(birthday_paradox.readable_dates([])), 0)
        self.assertEqual(len(birthday_paradox.readable_dates([1])), 1)
        self.assertEqual(len(birthday_paradox.readable_dates([1, 2])), 2)
        self.assertEqual(len(birthday_paradox.readable_dates([1, 1, 1])), 3)
        self.assertEqual(len(birthday_paradox.readable_dates([1, 2, 1])), 3)
        self.assertEqual(len(birthday_paradox.readable_dates([1, 2, 3])), 3)
        self.assertEqual(birthday_paradox.readable_dates([]), [])
        self.assertEqual(birthday_paradox.readable_dates([1]), ['Jan 01'])
        self.assertEqual(birthday_paradox.readable_dates([1, 2]), ['Jan 01', 'Jan 02'])
        self.assertEqual(birthday_paradox.readable_dates([1, 1, 1]), ['Jan 01', 'Jan 01', 'Jan 01'])
        self.assertEqual(birthday_paradox.readable_dates([1, 2, 1]), ['Jan 01', 'Jan 02', 'Jan 01'])
        self.assertEqual(birthday_paradox.readable_dates([1, 2, 3]), ['Jan 01', 'Jan 02', 'Jan 03'])

    def test_calculate_duplicate_dates(self):
        self.assertEqual(birthday_paradox.calculate_duplicate_dates(list()), [])
        self.assertEqual(birthday_paradox.calculate_duplicate_dates([1]), [])
        self.assertEqual(birthday_paradox.calculate_duplicate_dates([1, 2, 1]), [1])
        self.assertEqual(birthday_paradox.calculate_duplicate_dates([1, 1, 1]), [1])
        self.assertEqual(birthday_paradox.calculate_duplicate_dates([1, 2, 3]), [])
    
    def test_calculate_probability(self):
        self.assertGreater(birthday_paradox.calculate_probability(23)[1], 49)
        self.assertGreater(birthday_paradox.calculate_probability(70)[1], 99)
