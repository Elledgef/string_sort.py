#Author: Faith Elledge
#Githubuser: elledgef
#Date: 10/19
#Description: code sorts a list of farm animals "in place" using insertion sort


def string_sort (farm_animals):
    for animals in range(1,len(farm_animals)):
        value = farm_animals[animals]
        pos = animals -1
        while pos >= 0 and farm_animals[pos] > value:
            farm_animals[pos + 1] = farm_animals[pos]
            pos = pos -1
        farm_animals[pos + 1] = value

