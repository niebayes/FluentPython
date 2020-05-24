charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
lewis is charles
id(charles), id(lewis)
lewis['balance'] = 950
print(charles)