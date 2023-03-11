import math

T = int(input())

l1=[]

for i in range(1, T+1):
    N = int(input())
    total_hours = 0
    accent_qty = 0
    regular_qty = 0
    for j in range(1, N+1):
        R, B, S, H = map(int, input().split(','))
        num_walls = 6*H + 4*S + 3*B 
        accent_paint = 1.5*num_walls/3
        regular_paint = 4.5*num_walls/3
        accent_hours = 2.5*num_walls/3
        regular_hours = 6.5*num_walls/3
        total_qty = accent_paint + regular_paint
        total_hours_house = accent_hours + regular_hours
        accent_qty += accent_paint
        regular_qty += regular_paint
        total_hours += total_hours_house
    l1.append([total_hours,accent_qty,regular_qty])
for i in range(1,T+1):
    print("Case #{}: {:.2f}, {:.2f}, {:.2f}".format(i, l1[i-1][0],l1[i-1][1],l1[i-1][2]))
