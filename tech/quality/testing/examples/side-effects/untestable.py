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
  def motion_detected(self, datetime):
    if AlarmController.is_night(datetime):
      AlarmSiren.get_instance().activate()

  @staticmethod
  def is_night(datetime):
    return get_time_of_day(datetime) == "night"


class AlarmSiren:
  @staticmethod
  def get_instance():
    return alarm_siren

  def activate(self):
    pass

  def deactivate(self):
    pass

alarm_siren = AlarmSiren()


# ---
# TEST

from datetime import datetime

import unittest


def today_at(hour, minute=0, second=0):
  now = datetime.now()

  return datetime(now.year, now.month, now.day, hour, minute, second)


class AlarmControllerTest(unittest.TestCase):
  def setUp(self):
    self.alarm_controller = AlarmController()

  def test_motion_detected_at_2am_activates_alarm(self):
    self.alarm_controller.motion_detected(today_at(2))

    # How to assert?
    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()