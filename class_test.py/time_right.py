

def is_Time(number):
    hour = number // 60
    minute = number % 60
    time = hour, minute
    return time




print(is_Time(130))
