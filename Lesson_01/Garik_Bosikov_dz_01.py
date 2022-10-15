def convert_time(duration: int) -> str:
    day = duration // 86400
    hour = (duration - day * 86400) // 3600
    minutes = (duration - day * 86400 - hour * 3600) // 60
    sec = (duration - day * 86400 - hour * 3600 - minutes * 60) % 60
    return f'day: {day} hour: {hour} min: {minutes} sec: {sec}'


duration = 400153
result = convert_time(duration)
print(result)
