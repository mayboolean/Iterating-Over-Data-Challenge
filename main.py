def calculate_total_sales(sales_totals):
    if not sales_totals:
        return 0.0
    
    total = 0
    for value in sales_totals.values():
        total += (value["quantity"] * value["price"])
    
    return total


def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    
    total = 0
    quantity_total = 0
    for value in sales_totals.values():
        total += (value["quantity"] * value["price"])
        quantity_total += 1
    avg = total/quantity_total
    
    return avg

def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return {}

    avg_sales = calculate_average_sales(sales_totals)
    filtered_dictionary = {}
    
    for key, qty_price_dict in sales_totals.items():
        total = 0
        total += (qty_price_dict["quantity"] * qty_price_dict["price"])
        if total > avg_sales:
            filtered_dictionary[key] = qty_price_dict
        
    return filtered_dictionary
    
def ninety_nine_bottles(count, beverage):
    expected_lines = []
    for i in range(count,0,-1):
        if i == 1:
            expected_lines.append(f'{i} bottle of {beverage} on the wall, {i} bottle of {beverage}')
        else:
            expected_lines.append(f'{i} bottles of {beverage} on the wall, {i} bottles of {beverage}')
        if i == 2:
            expected_lines.append(f'If one of those bottles should happen to fall, {i-1} bottle of {beverage} on the wall')
        else: 
            expected_lines.append(f'If one of those bottles should happen to fall, {i-1} bottles of {beverage} on the wall')
        
    return expected_lines

# print(ninety_nine_bottles(2, "pop"))


