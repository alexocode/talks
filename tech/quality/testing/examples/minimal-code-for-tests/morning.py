def get_time_of_day(datetime):
  return "morning"

# ----
# TEST

from datetime import datetime

import unittest


def today_at(hour, minute=0, second=0):
  now = datetime.now()

  return datetime(now.year, now.month, now.day, hour, minute, second)


class TestGetTimeOfDay(unittest.TestCase):
  def test_returns_morning_at_6(self):
    time_of_day = get_time_of_day(today_at(6))

    self.assertEqual(time_of_day, "morning")


if __name__ == '__main__':
    unittest.main()