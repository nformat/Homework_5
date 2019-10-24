def is_year_leap(y):
    """
    Возвращающет True, если год високосный, и False иначе.

    """
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


def tre(a,b,c):
    """
    Определяет существует ли треуголник с такими сторонами. Возвращает True или False
    """

    l = [a, b, c]
    l.sort()
    if l[2]<l[0]+l[1]:
        return True
    else:
        return False


def tretype(a, b, c):
    """
    Определяет существует ли треуголник с такими сторонами. Возвращает True или False
    """

    l = [a, b, c]
    l.sort()
    if l[2] < l[0] + l[1]:
        if  l[2] == l[0] == l[1]:
            t = "равносторний"
        elif l[0] == l[1] or l[1] == l[2]:
            t = "равнобедренный"
        else:
            t = "разностороний"
    else:
        t = "несуществует"
    return t

if __name__ == "__main__":
    print(is_year_leap(2000))
    a = int(input("Введите первое число:\n"))
    b = int(input("Введите второе число:\n"))
    c = int(input("Введите третье число:\n"))
    print(tre(a, b, c))


    a = int(input("Введите первое число:\n"))
    b = int(input("Введите второе число:\n"))
    c = int(input("Введите третье число:\n"))
    print("Труголник", tretype(a, b, c))