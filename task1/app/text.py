from django.shortcuts import render
import csv
import os
from app.settings import BASE_DIR


def inflation_view(request):
    template_name = 'inflation.html'
    # print(BASE_DIR)

    csv_path = os.path.join(BASE_DIR, 'inflation_russia.csv')
    # print(csv_path)

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        values = []
        for row in reader:
            print(row)
            key = ''.join(row)
            print(key)
            values.append(row[key].split(';'))
            print(values)

    table_heads = key.split(';')
    print(table_heads)

    context = {
        'table_heads': table_heads,
        'values': values
    }

    return render(request, template_name,
                  context)

inflation_view(1)