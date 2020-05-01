topics = ["lema/home/level0/restroom", "lema/home/level0/hall", "lema/home/level0/kitchen/sink",
          "lema/home/level0/kitchen/island", "lema/home/level0/living/table",
          "lema/home/level0/living/TV", "lema/home/level0/living/library", "lema/home/level1/stairs/tiles",
          "lema/home/level1/stairs", "lema/home/level1/hall", "lema/home/level1/bathroom/mirror",
          "lema/home/level1/bathroom/ceiling", "lema/home/level1/bathroom/cupboard",
          "lema/home/level1/bathroom/fan", "lema/home/level1/west/bed", "lema/home/level1/west/ceiling",
          "lema/home/level1/west/corner", "lema/home/level1/east/bed", "lema/home/level1/east/corner",
          "lema/home/level1/east/ceiling", "lema/home/level1/south/ceiling", "lema/home/level1/south/corner",
          "lema/home/level2/attic", "lema/home/garage", "lema/blinds/level0/library", "lema/blinds/level0/TV",
          "lema/blinds/level0/terrace", "lema/blinds/level0/table", "lema/blinds/level0/kitchen",
          "lema/blinds/level1/east", "lema/blinds/level1/west", "lema/blinds/level1/south",
          "lema/blinds/level1/bathroom",
          "lema/garden/garage", "lema/garden/entrance", "lema/garden/wicket", "lema/garden/south",
          "lema/garden/east", "lema/garden/shed", "lema/balcony/east", "lema/balcony/west", "lema/balcony/south",
          "lema/sensors/move", "lema/sensors/temp/core", "lema/sensors/door", "lema/utils/garagedoor/target",
          "lema/garden/wicket/target", "lema/utils/alarm/get", "lema/home/iPad",
          "lema/utils/gate/target"]
lights = ["lema/home/level0/restroom", "lema/home/level0/hall", "lema/home/level0/kitchen/sink",
          "lema/home/level0/kitchen/island", "lema/home/level0/living/table",
          "lema/home/level0/living/TV", "lema/home/level0/living/library", "lema/home/level1/stairs/tiles",
          "lema/home/level1/stairs", "lema/home/level1/hall", "lema/home/level1/bathroom/mirror",
          "lema/home/level1/bathroom/ceiling", "lema/home/level1/bathroom/cupboard",
          "lema/home/level1/bathroom/fan", "lema/home/level1/west/bed", "lema/home/level1/west/ceiling",
          "lema/home/level1/west/corner", "lema/home/level1/east/bed", "lema/home/level1/east/corner",
          "lema/home/level1/east/ceiling", "lema/home/level1/south/ceiling", "lema/home/level1/south/corner",
          "lema/home/level2/attic", "lema/home/garage", "lema/garden/garage", "lema/garden/entrance",
          "lema/garden/south",
          "lema/garden/east", "lema/garden/shed", "lema/balcony/east", "lema/balcony/west", "lema/balcony/south",
          "lema/home/iPad"]
blinds = ["lema/blinds/level0/library", "lema/blinds/level0/TV",
          "lema/blinds/level0/terrace", "lema/blinds/level0/table", "lema/blinds/level0/kitchen",
          "lema/blinds/level1/east", "lema/blinds/level1/west", "lema/blinds/level1/south",
          "lema/blinds/level1/bathroom"]
utils = ["lema/sensors/move", "lema/sensors/door", "lema/utils/garagedoor/target", "lema/utils/alarm/get",
         "lema/utils/gate/target", "lema/garden/wicket/target", "lema/garden/wicket"]
wicket = ["lema/garden/wicket/target", "lema/garden/wicket"]
sensors = ["lema/sensors/temp/core"]
garage = "lema/home/garage"

not_mapped = set()
PNGs = set()

topics_size = len(topics)
lights_size = len(lights)
utils_size = len(utils)
blinds_size = len(blinds)
sensors_size = len(sensors)

counter_mon = [0] * topics_size
counter_tue = [0] * topics_size
counter_wen = [0] * topics_size
counter_thu = [0] * topics_size
counter_fri = [0] * topics_size
counter_sat = [0] * topics_size
counter_sun = [0] * topics_size

lastOn = [-1] * lights_size

timeOn_mon = [0] * lights_size
timeOn_tue = [0] * lights_size
timeOn_wen = [0] * lights_size
timeOn_thu = [0] * lights_size
timeOn_fri = [0] * lights_size
timeOn_sat = [0] * lights_size
timeOn_sun = [0] * lights_size

core_temp = []

counters = []
counters.append(counter_mon)
counters.append(counter_tue)
counters.append(counter_wen)
counters.append(counter_thu)
counters.append(counter_fri)
counters.append(counter_sat)
counters.append(counter_sun)

timeON = []
timeON.append(timeOn_mon)
timeON.append(timeOn_tue)
timeON.append(timeOn_wen)
timeON.append(timeOn_thu)
timeON.append(timeOn_fri)
timeON.append(timeOn_sat)
timeON.append(timeOn_sun)