import csv


def parse(filename):
    """
    Given a CSV file, this function outputs the column titles
    in headers and a two dimensional list which is a list of the
    rows of the CSV file.

    Input: CSV filename
    Output:
        headers: the column titles
        values: a two dimensional list of the values from the table
    """
    table = []
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            table.append(row[1:])

    for i in range(0, len(table)):
        for j in range(len(table[i])):
            table[i][j] = int(table[i][j])

    headers = table[0]
    values = table[1:]

    return headers, values


def sum_rows(values_table):
    """
    Given a two dimensional table of values, sum up all the rows
    and return the list of sums.

    Input: a two dimensional list of the values
    Output: an array conaiting the sum of each row of the two dimensional list
    """
    total_inventory = []
    for i in range(len(values_table)):
        total_inventory.append(sum(values_table[i]))

    return total_inventory


def new_function(total_inventory_list, ranges):
    """
    Here is the new feature implemented by the developer. Using a list of
    ranges of the form [(start1,end1), (start2,end2),....] they supposedly
    found all the total inventories between each start and end. Your task
    is to find what is wrong with this implementation.

    Inputs:
        ranges: A list of tuples where each tuple is a range
        total_inventory_list: An array of total inventories

    Output: A list of total inventories that fall within the specified ranges
    """
    output_list = []
    output_str = ""

    for total in total_inventory_list:
        for r in ranges:
            if total > r[0] and total < r[1] and total not in output_list:
                output_list.append(total)
            if total > r[0] and total < r[1] and str(total) not in output_str:
                output_str.join(str(total) + " ")

    return output_list, output_str


def main():
    headers, values = parse("large_data.csv")

    # Sum the values of each row
    total_inventory = sum_rows(values)

    # User Input to the new feature
    ranges = [(2200, 2500), (3000, 3300)]
    new_function(total_inventory, ranges)


if __name__ == "__main__":
    main()
