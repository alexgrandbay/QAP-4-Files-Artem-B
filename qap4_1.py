# Artem Babiienko; 29 Nov 2023

# Set up the following default values for the next policy number, the basic premium, 
# the discount for additional cars, the cost of extra liability coverage, the cost of 
# glass coverage, the cost for loaner car coverage, the HST rate, and the processing 
# fee for monthly payments. The values are 1944, , 869.00, .25, 130.00, 86.00, 
# 58.00, .15, and 39.99 respectfully.

# The user will input the customer’s first and last name, address, city, 
# province (validate using a list to make sure the province is valid), postal code, 
# and phone number. They will also enter the number of cars being insured, and options 
# for extra liability up to $1,000,000 (enter Y for Yes or N for No), optional glass
# coverage (Y or N), and optional loaner car (Y or N). Finally enter a value to indicate 
# if they want to pay in full or monthly (Full or Monthly or Down Pay – use a list 
# to validate). If the enter Down Pay allow them to enter the amount of the down payment. 
# Finally enter the date and cost of all previous claims for the customer – press 
# Enter to finish. Add at least 2-3 claims and store the values in lists. Convert the first and
#last name, the city, and the payment Method to title case and the Y/N values 
# upper case. No validations required – other than those specified - but go 
# for it if you want. Be careful when testing - enter values
# that are valid for each input.

# Insurance premiums are calculated using a basic rate of $869.00 for the 
# first automobile, with each additional automobile offered at a discount of 25%. 
# If the user enters a Y for any of the options, the costs are $130.00 per car for 
# extra liability, $86.00 per car for glass coverage, and $58.00 per car for the loaner
# car option. All these values are added together for the total extra costs. 
# The total insurance premium is the premium plus the total extra costs. 
# HST is calculated at 15% on the total insurance premium, and the total cost is 
# the total insurance premium plus the HST. Customers can pay for their insurance in full or in
# 8 monthly payments, with or without a downpayment. Calculate the monthly payment by adding a
# processing fee of $39.99 to the total cost and dividing the total cost by 8. If the user 
#entered a down payment, determine the monthly payment based on the total price less 
# the downpayment with the same processing fee over the same 8 months. 
# The invoice date is the current date, and the first payment date is the first day of the next month.


import datetime

# Values

next_policy_number = 1944
basic_premium = 869.00
discount_rate = 0.25
liability_cost = 130.00
glass_cost = 86.00
loaner_cost = 58.00
hst_rate = 0.15
processing_fee = 39.99

customer_data = []
claims_data = []


def format_values(value):
    return value.title()

def get_province():
    provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'NU', 'YT']
    while True:
        province = input("Enter province (e.g: ON): ").upper()
        if province in provinces:
            return province
        else:
            print("Invalid province. Please try again and enter a valid province abbreviation.")

def get_yes_or_no(prompt):
    while True:
        response = input(prompt).upper()
        if response in ['Y', 'N']:
            return response
        else:
            print("Invalid input. Please try again and enter Y or N.")

def get_payment_method():
    payment_methods = ['Full', 'Monthly', 'Down Pay']
    while True:
        method = input("Enter payment method (Full, Monthly, or Down Pay): ").title()
        if method in payment_methods:
            return method
        else:
            print("Invalid payment method. Please try again and enter Full, Monthly, or Down Pay.")

def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    total_extra_costs = 0
    total_extra_costs += num_cars * liability_cost if extra_liability == 'Y' else 0
    total_extra_costs += num_cars * glass_cost if glass_coverage == 'Y' else 0
    total_extra_costs += num_cars * loaner_cost if loaner_car == 'Y' else 0

    total_premium = basic_premium + (num_cars - 1) * basic_premium * discount_rate + total_extra_costs
    hst = total_premium * hst_rate
    total_cost = total_premium + hst

    return total_premium, hst, total_cost

def get_claims():
    claims = []
    while True:
        date = input("Enter date of claim (press Enter to finish): ")
        if not date:
            break
        cost = float(input("Enter cost of claim: "))
        claims.append((date, cost))
    return claims

def main():
    global next_policy_number

    while True:
        customer = {}
        customer['policy_number'] = next_policy_number
        customer['first_name'] = format_values(input("Enter first name: "))
        customer['last_name'] = format_values(input("Enter last name: "))
        customer['address'] = input("Enter address: ")
        customer['city'] = format_values(input("Enter city: "))
        customer['province'] = get_province()
        customer['postal_code'] = input("Enter postal code: ")
        customer['phone_number'] = input("Enter phone number: ")

        customer['num_cars'] = int(input("Enter number of cars: "))
        customer['extra_liability'] = get_yes_or_no("Extra Liability (Y/N): ")
        customer['glass_coverage'] = get_yes_or_no("Glass Coverage (Y/N): ")
        customer['loaner_car'] = get_yes_or_no("Loaner Car (Y/N): ")
        customer['payment_method'] = get_payment_method()

        if customer['payment_method'] == 'Down Pay':
            customer['down_payment'] = float(input("Enter down payment amount: "))
        else:
            customer['down_payment'] = 0

        customer['claims'] = get_claims()
        claims_data.extend([(customer['policy_number'], date, cost) for date, cost in customer['claims']])

        current_date = datetime.date.today()
        customer['invoice_date'] = current_date.strftime("%Y-%m-%d")
        customer['first_payment_date'] = (current_date.replace(day=1) + datetime.timedelta(days=32)).strftime("%Y-%m-%d")

        premium, hst, total_cost = calculate_premium(
            customer['num_cars'], customer['extra_liability'], customer['glass_coverage'], customer['loaner_car']
        )

        display_receipt(customer, premium, hst, total_cost)

def display_receipt(customer, premium, hst, total_cost):
    print("\n----- One Stop Insurance Company Receipt -----")
    print("")
    print(f"Policy Number: {customer['policy_number']}")
    print("")
    print(f"Name: {customer['first_name']} {customer['last_name']}")
    print(f"Address: {customer['address']}, {customer['city']}, {customer['province']} {customer['postal_code']}")
    print(f"Phone Number: {customer['phone_number']}")
    print("")
    print(f"Number of Cars: {customer['num_cars']}")
    print(f"Extra Liability: {customer['extra_liability']}")
    print(f"Glass Coverage: {customer['glass_coverage']}")
    print(f"Loaner Car: {customer['loaner_car']}")
    print(f"Payment Method: {customer['payment_method']}")
    if customer['payment_method'] == 'Down Pay':
        print(f"Down Payment: ${customer['down_payment']:.2f}")
    print("")
    print(f"\nTotal Premium: ${premium:.2f}")
    print(f"HST (15%): ${hst:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("")
    print(f"\nInvoice Date: {customer['invoice_date']}")
    print(f"First Payment Date: {customer['first_payment_date']}")
    print("---------------------------------------------\n")

if __name__ == "__main__":
    main()

# Could not understand how to make that part --> "At the end include the
# previous claims from the lists with the following format:"