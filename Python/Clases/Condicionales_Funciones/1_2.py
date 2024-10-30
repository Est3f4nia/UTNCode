def min_max():
    maxi = 0
    mini = 0
    n = int(input())
    for contador in range(n):
        nota = float(input())
        if maxi < nota or contador == 0:
            maxi = nota
        if mini > nota or contador == 0 and nota:
            mini = nota
    print(mini)
    print(maxi)
min_max()