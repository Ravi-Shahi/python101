'''
time module allows you to manipulate time, measure time intervals and format time values.

time()
sleep(seconds)
ctime(seconds)
localtime(seconds)
gmtime(seconds)
strftime(format, struct_time)
'''
import time

#time()
current_time = time.time()
print(current_time) #time in seconds, counting since 1 Jan, 1970, 00:00:00

#sleep(seconds)
'''
suspends the execution, for given number of seconds.

useCases:
- delays or pause the execution of a script
'''
for num in range(10):
    if num == 4:
        print('2 seconds break!')
        time.sleep(2) #pauses the execution for two second
        print('Thanks for patience!')
    else:
        print('continue')

#ctime(seconds)
'''
converts a time expressed in seconds to a string representing local time.
'''
formatted_time = time.ctime(current_time)
print('formated time',formatted_time)


#localtime()
local_time = time.localtime(current_time)
print("Local time:", local_time)

#gmtime()  [UTC Universal time cordinate]
utc_time = time.gmtime(current_time)
print('UTC :', utc_time)
print(type(utc_time))

#strftime(format,time)
string_formate_time = time.strftime("%d-%m-%Y %H:%M", time.localtime())
print('String formated time:', string_formate_time)


