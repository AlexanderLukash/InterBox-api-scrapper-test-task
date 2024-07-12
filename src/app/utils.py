from prettytable import PrettyTable


def print_country_data(countries):
    table = PrettyTable()
    table.field_names = ["Country", "Capital", "Flag URL"]

    for country in countries:
        table.add_row(country)

    print(table)
