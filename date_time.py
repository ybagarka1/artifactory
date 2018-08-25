from datetime import datetime, timedelta
#created_date = '2018-08-18T23:05:16.091Z' 
created_date = '2018-08-18T23:05:16.091-07:00'
zulu_time,string,seconds = created_date.rpartition('-')
#tuple_time = time.strptime(created_date, "%Y-%m-%dT%H:%M:%S")
#iso_time = time.strftime("%Y-%m-%dT%H:%M:%S", tuple_time)
#print(iso_time)
zulu_time = zulu_time+'Z'
utc_dt = datetime.strptime(zulu_time, '%Y-%m-%dT%H:%M:%S.%fZ')
past_time = utc_dt - timedelta(90)
timestamp =  (past_time - datetime(1970, 1, 1)).total_seconds()
print(past_time)
print(timestamp)


