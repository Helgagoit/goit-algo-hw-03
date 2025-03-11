import random 

def get_numbers_ticket(min, max, quantity):
    if 1 <= min and max <= 1000 and min < max and min <= quantity <= max:
        return sorted(random.sample(range(min, max + 1), quantity))
    else:
        return []
          

lottery_numbers = get_numbers_ticket(5, 999, 18)
print("Ваші лотерейні числа:", lottery_numbers)