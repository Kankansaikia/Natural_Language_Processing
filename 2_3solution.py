#if you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

kilometer=10
minute=42
seconds=42
miles=kilometer/1.61
minute_h=42/60
second_h=42/3600
total_hour=minute_h+second_h
avg_speed=miles/total_hour
print("The average speed is ",avg_speed);