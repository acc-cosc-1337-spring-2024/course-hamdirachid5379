#create functions 
def get_hour(epoch_seconds):# get the hour since 1970
    return (epoch_seconds // 3600 ) % 60 % 24

def get_minutes(epoch_seconds): # get the minutes since 1970
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):# get the seconds since 1970
    return (epoch_seconds % 3600) % 60

s=int(input("Enter epoch_seconds:"))
#1hr = 3600s
hour = s//3600 % 60 %24
second = s%60
minutes = s//60 % 60
print("%d:%d:%d" %(hour,minutes,second))







