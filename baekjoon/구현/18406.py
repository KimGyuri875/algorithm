N = (str(input()))
front, back = 0, 0

for i in range(len(N)//2):
    front += int(N[i])
    back += int(N[-1 * (i) -1])

if front == back:
    print('LUCKY')
else:
    print('READY')
