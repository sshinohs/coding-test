data = input()
duration = input()
time_str = data.split()
time_hour = int(time_str[0])
time_minute = int(time_str[1])
duration_minute = int(duration)

time_minute_after = time_hour*60+time_minute+duration_minute

if time_minute_after>=1440:
    time_minute_after = time_minute_after - 1440


time_hour_processed = time_minute_after//60

time_minute_processed = time_minute_after%60

print(str(time_hour_processed) + " " + str(time_minute_processed))