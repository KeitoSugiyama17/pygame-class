n = 5
for i in range(0, 10):
    line = ''
    if (i == 0) or (i == 10 - 1):
        for j in range(0, n):
          line = line + '*'
    else:
        line = '*'
        for j in range(0, n - 2):
            line = line + ' '
        line = line + '*'
    print(line)