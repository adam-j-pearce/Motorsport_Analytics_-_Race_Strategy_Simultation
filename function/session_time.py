def session_time_log():
      
  time_remaining = ['SessionTimeRemain']
  laps_remaining = ['SessionLapsRemain']
  laps_remaining_expected = ['SessionLapsRemainEx']
  session_time = ['SessionTimeOfDay']
  
  session_time_log = {
    "time":{
      "session": session_time,
      "remaining": time_remaining
      },
    "laps":{
      "remaining": laps_remaining,
      "expected": laps_remaining_expected
      }
    }

  return session_time_log
