def session_info():

  session = ir['WeekendInfo']['EventType']
  session_id = ir['WeekendInfo']['SessionID']
  session = ir['WeekendInfo']['EventType']
  session_id = ir['WeekendInfo']['SessionID']
  subsession_id = ir['WeekendInfo']['SubSessionID']
  season_id = ir['WeekendInfo']['SeasonID']
  series_id = ir['WeekendInfo']['SeriesID']
  official = ir['WeekendInfo']['Official']
  
  if str(ir['WeekendInfo']['EventType']) == "Test":
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    session_id == "Testing-",timestamp
    
  if official == "0":
    official = False
  else:
    official = True

session_info_log= {
  "type":session,
  "id":session_id,
  "sub_id":subsession_id,
  "season":season_id,
  "official":official
  }

  return session_info_log
