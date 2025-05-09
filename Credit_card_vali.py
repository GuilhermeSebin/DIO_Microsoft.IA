"""build a program in python that will recognize a credic card number and identify the flags (visa, mastercard, amex, discover) and the card type (debit or credit)"""
import re
import random
import string

def generate_card_number():
    """Generate a random credit card number"""
    card_number = ''.join(random.choices(string.digits, k=16))
    return card_number
def validate_card_number(card_number):
    """Validate the credit card number using Luhn's algorithm"""
    def luhn_check(card_number):
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    return luhn_check(card_number)
def identify_card_type(card_number):
    """Identify the card type based on the number"""
    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number):
        return "Visa"
    elif re.match(r'^5[1-5][0-9]{14}$', card_number):
        return "MasterCard"
    elif re.match(r'^3[47][0-9]{13}$', card_number):
        return "American Express"
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', card_number):
        return "Discover"
    else:
        return "Unknown"
def identify_card_flags(card_number):
    """Identify the card flags (debit or credit)"""
    if re.match(r'^[0-9]{16}$', card_number):
        return "Credit"
    elif re.match(r'^[0-9]{15}$', card_number):
        return "Debit"
    else:
        return "Unknown"
def main():
    card_number = generate_card_number()
    print(f"Generated Card Number: {card_number}")
    
    if validate_card_number(card_number):
        print("Card Number is valid.")
    else:
        print("Card Number is invalid.")
    
    card_type = identify_card_type(card_number)
    print(f"Card Type: {card_type}")
    
    card_flags = identify_card_flags(card_number)
    print(f"Card Flags: {card_flags}")