
# bringing in necessities
import os
import csv

#opening and reading proper csv, establishing output file as well
data_csv = os.path.join("Resources","budget_data.csv")
analysis_txt = os.path.join("Analysis","budget_analysis.txt")

#establish variables to be used during reading
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 9999999999]
total_net = 0

with open(data_csv) as csvfile:
    csvreader = csv.reader(csvfile)

#ensuring to read header row first if it exists
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:

        #tracking the total
        total_months += 1
        total_net += int(row[1])

        #tracking net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #determining greatest increase/decrease
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#average net change
net_average = sum(net_change_list) / len(net_change_list)


# output summary

output = (
    f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months : {total_months}\n"
    f"Total : ${total_net}\n"
    f"Average Change : ${net_average:.2f}\n"
    f"Greatest Increase in Profits : {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits : {greatest_decrease[0]} (${greatest_decrease[1]})"
)

print(output)

# exporting to text file
with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)


    