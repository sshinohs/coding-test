data = input()
time_str = data.split()
time_hour = int(time_str[0])
time_minute = int(time_str[1])

time_minute_all = time_hour*60+time_minute

if time_minute_all<45:
    time_minute_all = time_minute_all + 1440

time_processed = time_minute_all-45

time_hour_processed = time_processed//60

time_minute_processed = time_processed%60

print(str(time_hour_processed) + " " + str(time_minute_processed))