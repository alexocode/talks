def get_time_of_day(datetime):
  hour = datetime.hour

  if hour >= 0 and hour < 6:
    return "night"
  elif hour >= 6 and hour < 12:
    return "morning"
  elif hour >= 12 and hour < 18:
    return "afternoon"

  return "evening"


class AlarmController:
  def __init__(self, alarm):
    self.alarm = alarm

  def motion_detected(self, datetime):
    if AlarmController.is_night(datetime):
      self.alarm.activate()

  @staticmethod
  def is_night(datetime):
    return get_time_of_day(datetime) == "night"


# ---
# TEST

from datetime import datetime

import unittest


def today_at(hour, minute=0, second=0):
  now = datetime.now()

  return datetime(now.year, now.month, now.day, hour, minute, second)


class FakeAlarm:
  activated = False

  def activate(self):
    self.activated = True

class AlarmControllerTest(unittest.TestCase):
  def setUp(self):
    self.alarm = FakeAlarm()
    self.alarm_controller = AlarmController(self.alarm)

  def test_motion_detected_at_2_activates_alarm(self):
    self.alarm_controller.motion_detected(today_at(2))

    self.assertTrue(self.alarm.activated)

  def test_motion_detected_at_8_does_not_activate_alarm(self):
    self.alarm_controller.motion_detected(today_at(8))

    self.assertFalse(self.alarm.activated)


if __name__ == '__main__':
    unittest.main()