def find_lucky(num):
    lucky_digits = [4,7]
    no_lucky = 0
    while num != 0:
        luck = num % 10
        num = num // 10
        if luck in lucky_digits:
            no_lucky += 1
    
    return "YES" if no_lucky in lucky_digits  else "NO" 
        
print(find_lucky(int(input())))