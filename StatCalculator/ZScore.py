from StatCalculator.Mean import mean
from StatCalculator.StandardDev import stand_dev
from pprint import pprint


def z_score(num):
    try:
        z_mean = mean(num)
        sd = stand_dev(num)
        z_list = []
        z_list1 = []

        for x in num:
            z = round(((float(x) - float(z_mean)) / float(sd)), 6)
            z_list.append(z)
        nFinal = z_list[0]
        return nFinal

    except ZeroDivisionError:
        print("Error!  Cannot divide by 0")
    except ValueError:
        print("Error!  Invalid data inputs")