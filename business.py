import random
import json

def get_random_city():

    json_file = open('data.json')

    data = json.load(json_file)

    data_list = list(data)

    random_city = ''

    while(len(random_city) == 0):

        random_country_index = random.randint(1, len(data_list) - 1)
        random_country = data_list[random_country_index]
        random_city_index = random.randint(0, len(data[random_country]) - 1)
        random_city = data[random_country][random_city_index]

        json_file.close()

    return random_city

# if __name__ == '__main__':
#     n = 50
#     while(n):
#         print(get_random_city())
#         n -= 1