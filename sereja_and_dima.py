n = int(input())
serja = 0
dima = 0
cards = list(map(int, input().split()))
turn = 1
while len(cards) != 0:
    if cards[0] < cards[-1]:
        if turn % 2 == 0:
            dima += cards[-1]
        else:
            serja += cards[-1]
        cards.pop()
        turn += 1
    else:
        if turn % 2 != 0:
            serja += cards[0]
        else:
            dima += cards[0]
        turn += 1
        cards.pop(0)
print(f"{serja} {dima}")