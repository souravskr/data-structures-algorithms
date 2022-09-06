def time_conversion(s):
    if 'AM' in s and s[:2] == '12':
        return '00' + s[2:-2]
    elif 'PM' in s:
        hour = 12 + int(s[:2])
        return str(hour) + s[2:-2]
    else:
        return s[:-2]


print(time_conversion('07:05:45AM'))
