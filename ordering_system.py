menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}
order_list = [1, 2] 

def calculate_subtotal(order_list):
    subtotal = 0
    for item in order_list:
        if item in menu:  # Check if the item number exists in the menu
            subtotal += menu[item]["price"]
    return subtotal

def calculate_tax(subtotal):
    """ Calculates the tax of an order """
    tax_percentage = 0.15
    tax = subtotal * tax_percentage
    return round(tax, 2)

def summarize_order(order_list):
    """ Summarizes the order """
    order_summary = [(menu[item]["name"], menu[item]["price"]) for item in order_list]
    subtotal = calculate_subtotal(order_list)
    tax = calculate_tax(subtotal)
    total_amount = subtotal + tax
    # Include subtotal in the summary
    order_summary.append(('Subtotal', subtotal))
    order_summary.append(('Tax (15%)', tax))
    order_summary.append(('Total Amount', total_amount))
    return order_summary

def print_order(order):
  
    item_count = len([item for item in order if not item[0].startswith('Subtotal') and not item[0].startswith('Tax') and not item[0].startswith('Total')])
    print(f'You have ordered {item_count} items')
    for item in order:
        print(f"{item[0]}: ${item[1]:.2f}")

def main():
    order_list = [4, 2, 1]  # Using the corresponding menu item numbers
    order_summary = summarize_order(order_list)
    print_order(order_summary)

if __name__ == "__main__":
    main()
