import stdio

total = 0.0
count = 0

while not stdio.isEmpty(4):
    value = stdio.readfloat()
    total += value
    count += 1
print('Average is %.2f' % (total/count))
