import csv

months_counter = 0
total_amount = 0
rows_diff = 0
total_change = 0
avg_change = 0
greatest_inc_amt = 0
greatest_dec_amt = 0
greatest_inc_mon = None
greatest_dec_mon = None

with open('budget_data.csv', 'r') as csvfile:
    filereader = csv.reader(csvfile)
    next(filereader)
    prev_month_amt = 0
    for row in filereader:
        months_counter += 1
        row_amt = int(row[1])
        total_amount += row_amt
        if row_amt > prev_month_amt:
            new_greatest_inc = row_amt - prev_month_amt
            if new_greatest_inc > greatest_inc_amt:
                greatest_inc_amt = new_greatest_inc
                greatest_inc_mon = row[0]
        else:
            new_greatest_dec = row_amt - prev_month_amt
            if new_greatest_dec < greatest_dec_amt:
                greatest_dec_amt = new_greatest_dec
                greatest_dec_mon = row[0]
        if months_counter >= 2:
            rows_diff = row_amt - prev_month_amt
            total_change += rows_diff
        prev_month_amt = row_amt
avg_change = round(total_change/(months_counter - 1),2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months_counter))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: ", greatest_inc_mon,"($" + str(greatest_inc_amt) + ")")
print("Greatest Decrease in Profits: ", greatest_dec_mon,"($" + str(greatest_dec_amt) + ")")

with open('pybank_jmf.txt','w') as out:
    out.write("Financial Analysis\n")
    out.write("----------------------------\n")
    out.write("Total Months: " + str(months_counter) + "\n")
    out.write("Total: $" + str(total_amount) + "\n")
    out.write("Average Change: $" + str(avg_change) + "\n")
    out.write("Greatest Increase in Profits: "+ greatest_inc_mon +" ($" + str(greatest_inc_amt) + ")" + "\n")
    out.write("Greatest Decrease in Profits: "+ greatest_dec_mon +" ($" + str(greatest_dec_amt) + ")")