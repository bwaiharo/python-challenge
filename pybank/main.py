import os
from csv import DictReader, writer

budget_csv = os.path.join('python-challenge\pybank\budget_data.csv')
b_date = []
b_pl = []
with open (budget_csv, "r") as csv_f:
    budget_file = DictReader(csv_f)
    # next(csv_file)
    for b_row in budget_file:
       b_date.append(b_row["Date"])
       b_pl.append(int(b_row['Profit/Losses']))

def title():
    return '''Financial Analysis \n---------------------------'''

def total_months(mnths):
    return "Total Months: "+ str(len(mnths))

def total (ttl):
    return "Total: " +str(sum(ttl))

def average(avg):
    return "Average Change: "+str(sum(avg)/len(b_pl))

def greatest_inc(gi):
    return "Greatest Increase in Profits: "+str(gi[b_pl.index(max(b_pl))])+"  ($"+str(max(b_pl))+")"

def greatest_dec(gd):
    return "Greatest Decrease in Profits: "+str(gd[b_pl.index(min(b_pl))])+"  ($"+str(min(b_pl))+")"

print(title())
print(total_months(b_date))
print(total(b_pl))
print(average(b_pl))
print(greatest_inc(b_date))
print(greatest_dec(b_date))

with open("python-challenge\Resources\Budget_output.csv","w") as file:
    budget_write = writer(file)
    budget_write.writerow([title()])
    budget_write.writerow([total_months(b_date)])
    budget_write.writerow([total(b_pl)])
    budget_write.writerow([average(b_pl)])
    budget_write.writerow([greatest_inc(b_date)])
    budget_write.writerow([greatest_dec(b_date)])



