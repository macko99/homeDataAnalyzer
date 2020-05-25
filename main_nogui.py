import os
import sys

from datahandler import *

price = 0.60
power = 10


def main():
    global price, power
    if len(sys.argv) == 3:
        price = float(sys.argv[1])
        power = float(sys.argv[2])
    init()
    populate_data()
    print(price + power)
    save_data(power, price)
    visualize_data()
    os.remove("tmp.txt")
    sys.exit()


if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    main()
