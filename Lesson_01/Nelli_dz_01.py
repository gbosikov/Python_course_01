duration = int(input("duration"))


def Convert_Time ():
    oneday = 86400  # seconds in one day
    day = duration // oneday  # целочисленное деление для определения колличества дней
    chas = (duration - (day * oneday)) // 3600  # остаток секунд после расчёта количества дней целочисленно делёный на количество секунд в часе
    minut = (duration - (day * oneday) - (chas * 3600)) // 60  # статок секунд после расчёта количества часов целочисленно делёный на количество секунд в минуте
    seck = (duration - (day * oneday) - (chas * 3600)) % 60  # статок секунд после расчёта количества минут целочисленно делёный на количество секунд в часе
    print(day, "day", chas, "chas", minut, "minuti", seck, "sec")


Convert_Time()

