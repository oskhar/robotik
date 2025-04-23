def get_mean(list):
    total = 0
    for i in list:
        total += i

    return total / len(list)

values = [75, 85, 80, 50, 110]
print(get_mean(values))
