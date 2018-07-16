from datetime import datetime


def get_time_of_day():
  now = datetime.now()

  if now.hour >= 0 and now.hour < 6:
    return "night"
  elif now.hour >= 6 and now.hour < 12:
    return "morning"
  elif now.hour >= 12 and now.hour < 18:
    return "afternoon"

  return "evening"


# Test

import unittest


class TestGetTimeOfDay(unittest.TestCase):
  def test_returns_morning_at_6am(self):
    # How to specify 6am?
    self.assertEqual(get_time_of_day(), "morning")


if __name__ == '__main__':
    unittest.main()
