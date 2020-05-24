from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP'),
    ('Delhi NCR', 'IN'),
    ('Mexico City', 'MX'),
    ('New York', 'US'),
    ('Sao Paulo', 'BR')
]

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

print(itemgetter(1, 0).__call__(metro_data[0]))