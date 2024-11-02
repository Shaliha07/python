import csv

# Writing to a CSV file
with open('house_data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Size','Location','Price'])
    csv_writer.writerow([1500,'Urban',300000])
    csv_writer.writerow([1600,'Suburban',250000])
    csv_writer.writerow([1700,'Rural',200000])
    csv_writer.writerow([1800,'Urban',350000])
    csv_writer.writerow([1900,'Suburban',280000])

    



