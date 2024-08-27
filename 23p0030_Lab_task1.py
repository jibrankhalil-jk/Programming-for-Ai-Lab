n = int(input('Enter a positive integer'))
sum = 0
for i in range (1,n+1):
    sum += i
    
    if i ==1:
        print(f"{i}",end='')
    else:
        print(f"+{i}",end='')

print(f"\nsum is : {sum}")