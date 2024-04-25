def chew_number(n):
    temp = n
    string_array = []
    while n!= 0:
        digit = n % 10
        replace_digit = 9 - digit
        if(digit > replace_digit):
            string_array.append(str(replace_digit))
        else:
            string_array.append(str(digit))
        
        n = n // 10
    
    string_array = string_array[::-1]
    s = "".join(string_array)
    return int(s)

n = int(input())
print(chew_number(n))