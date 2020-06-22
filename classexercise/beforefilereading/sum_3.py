count = 0
result = 0
while count < 100:
    count += 1
    if count%3 != 0:
        continue
    result += count
    print(count)
print(result)
        
