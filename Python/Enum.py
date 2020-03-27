objective = int(input("Choose an integeer: "))
answer = 0

while answer**2 < objective:
    answer += 1
    
if answer**2 == objective:
    print(f'Sqrt of {objective} is {answer}')
else:
    print(f'{objective} doesn\'t have an exact sqrt')