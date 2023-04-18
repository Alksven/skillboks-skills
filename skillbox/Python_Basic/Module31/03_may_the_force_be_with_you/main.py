import requests
import json


def starship_info(info):
    info_starship['name'] = info['results'][i]['name']
    info_starship['max_atmosphering_speed'] = info['results'][i]['max_atmosphering_speed']
    info_starship['starship_class'] = info['results'][i]['starship_class']
    pilots(info['results'][i]['pilots'])


def pilots(info):
    info_starship['pilots'] = list()

    for count_pilot in info:
        pilot_info = dict()
        pilot = requests.get(count_pilot)
        data = json.loads(pilot.text)
        pilot_info['name'] = data['name']
        pilot_info['height'] = data['height']
        pilot_info['mass'] = data['mass']
        homeworld = requests.get(data['homeworld'])
        data_homeworld = json.loads(homeworld.text)
        pilot_info['homeworld'] = data_homeworld['name']
        pilot_info['homeworld_url'] = data['homeworld']
        info_starship['pilots'].append(pilot_info)

        del pilot_info


if __name__ == '__main__':

    info_starship = dict()

    page = 1
    flag = True
    while flag:
        find_starship = requests.get(f'https://swapi.dev/api/starships/?page={page}')
        for i in range(1, 10 + 1):
            data = json.loads(find_starship.text)
            if data["results"][i]['name'] == 'Millennium Falcon':
                starship_info(data)
                flag = False
                with open('info_starship.json', 'w') as starship:
                    json.dump(info_starship, starship, indent=4)
                break

    with open('info_starship.json', 'r') as starship:
        deta = json.load(starship)
    print(json.dumps(deta, indent=4))
