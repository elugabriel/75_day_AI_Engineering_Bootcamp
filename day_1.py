valid_numbers = []
total_sum = 0


for num in range(1, 1001):
    first = num
    initial_sum = 0
    
    for digit in str(first):
        initial_sum = initial_sum + int(digit)

   
    sum_2 = 0
    for digit in str(initial_sum):
        sum_2 = sum_2 + int(digit)

  
    if sum_2 < 10:
        chain_length = 3
        final_digit = sum_2

       
        if chain_length == 3 and final_digit == 7:
            valid_numbers.append(num)
            total_sum = total_sum + num

print("Valid numbers:", valid_numbers)
print("Count:", len(valid_numbers))
print("Sum of all such numbers:", total_sum)