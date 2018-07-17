from datetime import datetime


def get_time_of_day(datetime):
  hour = datetime.hour

  if hour >= 0 and hour < 6:
    return "night"
  elif hour >= 6 and hour < 12:
    return "morning"
  elif hour >= 12 and hour < 18:
    return "afternoon"

  return "evening"


# Test

import unittest


def today_at(hour, minute=0, second=0):
  now = datetime.now()

  return datetime(now.year, now.month, now.day, hour, minute, second)


class TestGetTimeOfDay(unittest.TestCase):
  def test_returns_morning_at_6(self):
    time_of_day = get_time_of_day(today_at(6))

    self.assertEqual(time_of_day, "morning")

  def test_returns_afternoon_at_12(self):
    time_of_day = get_time_of_day(today_at(12))

    self.assertEqual(time_of_day, "afternoon")

  def test_returns_evening_at_18(self):
    time_of_day = get_time_of_day(today_at(18))

    self.assertEqual(time_of_day, "evening")

  def test_returns_night_at_0(self):
    time_of_day = get_time_of_day(today_at(0))

    self.assertEqual(time_of_day, "night")


if __name__ == '__main__':
    unittest.main()
