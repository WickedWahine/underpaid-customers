def find_payment_discrepancy():
    file = open("customer-orders.txt")
    melon_cost = 1.00

    for line in file:
        cust_entry = line.rstrip()
        cust_data = cust_entry.split("|")
        cust_name = cust_data[1]
        qty = int(cust_data[2])
        payment_amt = float(cust_data[3])
        payment_due = float(qty * melon_cost)

        if payment_amt != payment_due:
            print(f"{cust_name:20} paid ${payment_amt:7.2f}, expected ${payment_due:7.2f}. Discrepancy ${payment_due - payment_amt:7.2f}")

find_payment_discrepancy()