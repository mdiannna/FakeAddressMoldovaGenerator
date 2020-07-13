import random
import re
from random import randint

file_addresses_name = 'address_list_chisinau.txt'
# source: https://wiki.openstreetmap.org/w/index.php?title=Ro:Moldova/municipiul_Chi%C8%99in%C4%83u/Chi%C8%99in%C4%83u/Str%C4%83zi&action=edit

f_addr = open(file_addresses_name, 'r')

address_list = [line.replace("\n", '').strip() for line in f_addr.readlines() ]
# print(address_list)

f_addr.close()

def random_street():
	return random.choice(address_list)


def random_street_short():
	street = random.choice(address_list)
	return street.replace('Bulevardul', 'bd.').replace('Șoseaua', 'şos. ').replace('Strada', 'str.').replace("Stradela", "str-la")

# Strada <NumeStrada> 3/6, ap. 353
def random_address_format1():
	return random_street() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))

# str. <NumeStrada> 3/6, ap. 353
def random_address_format1_short():
	return random_street_short() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))

# str. <NumeStrada> 3/6, ap. 353, Chisinau, Moldova
# TODO: adaugat random un oras
def random_address_format1_complet():
	return random_address_format1() + ", Chisinau, Moldova"

def random_address_format2():
	return random_street() +  " " + str(randint(1, 20)) + " et. " +  str(randint(1, 5)) + ", of." + str(randint(1, 100))

# str. <NumeStrada> 3/6, ap. 353
def random_address_format1_short():
	return random_street_short() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))


print(random_street())
print(random_street_short())
print(random_address_format1())
print(random_address_format2())
print(random_address_format1_short())
print(random_address_format1_complet())