import datetime

time = datetime.datetime.now()
print("Current time with microseconds: ", time.time())
print("Current time without microsecond: ", time.strftime("%X"))