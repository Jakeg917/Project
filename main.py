import csv
import matplotlib.pyplot as plt

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the first row of the CSV file
    next(csv_reader)

    # Define a dictionary to store the total number of vehicles sold in each year
    yearly_totals = {}

    # Define a variable to store the total number of vehicles sold in the first six months of 2021 and 2022
    total_2021 = 0
    total_2022 = 0

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Get the year and number of vehicles sold from the current row
        year = int(row[0])
        vehicles_sold = int(row[1])

        # Add the number of vehicles sold to the yearly_totals dictionary
        if year in yearly_totals:
            yearly_totals[year] += vehicles_sold
        else:
            yearly_totals[year] = vehicles_sold

        # Calculate the total sales for the first six months of 2021 and 2022
        if year == 2021 and int(row[2]) <= 6:
            total_2021 += vehicles_sold
        elif year == 2022 and int(row[2]) <= 6:
            total_2022 += vehicles_sold

    # Calculate the sales growth rate for the first six months of 2022, if there are sales data for the first six months of 2021
    if total_2021 != 0:
        SGR = (total_2022 - total_2021) / total_2021

        # Write the sales growth rate to the stats.txt file
        with open('stats.txt', 'a') as file:
            file.write(f'Sales Growth Rate: {SGR}\n')

            # Calculate the estimated sales for the last six months of 2022 and write to stats.txt
            for month in range(7, 13):
                estimated_sales = yearly_totals[2021] + yearly_totals[2021] * SGR
                file.write(f'Estimated Sales for {month}/2022: {estimated_sales}\n')

        # Plot the estimated sales for the last six months of 2022 using a horizontal bar plot
        months = [f'{month}/2022' for month in range(7, 13)]
        estimated_sales = [yearly_totals[2021] + yearly_totals[2021] * SGR] * 6
        plt.barh(months, estimated_sales)
        plt.title('Estimated Vehicles Sold for Last Six Months of 2022')
        plt.xlabel('Total Vehicles Sold')
        plt.ylabel('Month')
        plt.show()
    else:
        print("No data available for the first six months of 2021")

# Plot the yearly totals using a bar plot
years = list(yearly_totals.keys())
totals = list(yearly_totals.values())
plt.bar(years, totals)
plt.title('Total Vehicles Sold by Year')
plt.xlabel('Year')
plt.ylabel('Total Vehicles Sold')
plt.show()





