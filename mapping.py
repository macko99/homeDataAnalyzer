def map(topic):
    switcher = {
        "lema/home/level0/restroom": "Toalet parter",
        "lema/home/level0/hall": "Przedsionek",
        "lema/home/level0/kitchen/sink": "Kuchnia",
        "lema/home/level0/kitchen/island": "Wyspa",
        "lema/home/level0/living/table": "Stół",
        "lema/home/level0/living/TV": "Salon",
        "lema/home/level0/living/library": "Biblioteczka",
        "lema/home/level1/stairs/tiles": "Płytki - schody",
        "lema/home/level1/stairs": "Schody",
        "lema/home/level1/hall": "Piętro - korytarz",
        "lema/home/level1/bathroom/mirror": "Łazienka - lustro",
        "lema/home/level1/bathroom/ceiling": "Łazienka",
        "lema/home/level1/bathroom/cupboard": "Łazienka - wanna",
        "lema/home/level1/bathroom/fan": "Łazienka - wiatrak",
        "lema/home/level1/west/bed": "Zachód - łózko",
        "lema/home/level1/west/ceiling": "Zachód - sufit",
        "lema/home/level1/west/corner": "Zachód - biurko",
        "lema/home/level1/east/bed": "Wschód - łóżko",
        "lema/home/level1/east/corner": "Wschód - skos",
        "lema/home/level1/east/ceiling": "Wschód - sufit",
        "lema/home/level1/south/ceiling": "Południe - sufit",
        "lema/home/level1/south/corner": "Południe - skos",
        "lema/home/level2/attic": "Strych",
        "lema/home/garage": "Garaż",
        "lema/blinds/level0/library": "Roleta - biblioteczka",
        "lema/blinds/level0/TV": "Roleta - salon",
        "lema/blinds/level0/terrace": "Roleta - taras",
        "lema/blinds/level0/table": "Roleta - stół",
        "lema/blinds/level0/kitchen": "Roleta - kuchnia",
        "lema/blinds/level1/east": "Roleta - wschód",
        "lema/blinds/level1/west": "Roleta - zachód",
        "lema/blinds/level1/south": "Roleta - południe",
        "lema/blinds/level1/bathroom": "Roleta - łazienka",
        "lema/garden/garage": "Przed garażem",
        "lema/garden/entrance": "Przed wejściem",
        "lema/garden/wicket": "Furtka",
        "lema/garden/south": "Ogród - południe",
        "lema/garden/east": "Ogród - wschód",
        "lema/garden/shed": "Pergola",
        "lema/balcony/east": "Balkon - wschód",
        "lema/balcony/west": "Balkon - zachód",
        "lema/balcony/south": "Balkon - południe",
        "lema/sensors/move": "Ruch w garażu",
        "lema/sensors/temp/core": "Temp. procesora",
        "lema/sensors/door": "Drzwi",
        "lema/utils/garagedoor/target": "Brama garażowa",
        "lema/garden/wicket/target": "Furtka",
        "lema/utils/alarm/get": "Alarm",
        "lema/home/iPad": "iPad",
        "lema/home/level0/all": "Przycisk wszyskie-parter",
        "lema/utils/gate/target": "Brama - podjazd"
    }
    return switcher.get(topic, "ERR -> no mapping for: " + str(topic))


def weekday(day):
    switcher = {
        0: "\nPoniedziałek\n",
        1: "\nWtorek\n",
        2: "\nŚroda\n",
        3: "\nCzwartek\n",
        4: "\nPiątek\n",
        5: "\nSobota\n",
        6: "\nNiedziela\n"
    }
    return switcher.get(day, "ERR -> no mapping for: " + str(day))


def time_format(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)