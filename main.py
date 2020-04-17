for i in range(0, 5):
    spaces = ''
    for j in range(0, 5 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 1):
        stars = stars + '*'
    print(spaces + stars)
