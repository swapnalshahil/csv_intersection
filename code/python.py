import csv


def csv_intersection(path_one, path_two, delimiter='\t', encoding="UTF-8"):
    one = []
    two = []
    result = []

    with open(path_one, "r", encoding=encoding) as first_csv:
        csv_reader_1 = csv.DictReader(first_csv,  delimiter=delimiter)
        for row in csv_reader_1:
            one.append(row)

    with open(path_two, "r", encoding=encoding) as second_csv:
        csv_reader_2 = csv.DictReader(second_csv,  delimiter=delimiter)
        for row in csv_reader_2:
            two.append(row)

    for OrderedDict in one:
        if OrderedDict in two:
            result.append(OrderedDict)

    return result
