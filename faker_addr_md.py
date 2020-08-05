import random
import re
from random import randint

file_addresses_name = 'address_list_chisinau.txt'
# source: https://wiki.openstreetmap.org/w/index.php?title=Ro:Moldova/municipiul_Chi%C8%99in%C4%83u/Chi%C8%99in%C4%83u/Str%C4%83zi&action=edit
file_districts_name = 'district_list_md.txt'

f_addr = open(file_addresses_name, 'r')
f_districts = open(file_districts_name, 'r')

address_list = [line.replace("\n", '').strip() for line in f_addr.readlines() ]
districts_list = [line.replace("\n", '').strip() for line in f_districts.readlines() ]

# print(address_list)
# print(districts_list)

f_addr.close()
f_districts.close()

def random_street():
	return random.choice(address_list)


def random_district():
	return random.choice(districts_list)


def random_street_short():
	street = random.choice(address_list)
	return street.replace('Bulevardul', 'bd.').replace('Șoseaua', 'şos. ').replace('Strada', 'str.').replace("Stradela", "str-la")


# Strada <NumeStrada> 3/6, ap. 353
def random_address_format1():
	return random_street() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))


# str. <NumeStrada> 3/6, ap. 353
def random_address_format1_short():
	return random_street_short() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))

# str. <NumeStrada> 3/6, ap. 353
def random_address_format2():
	return random_street_short() +  " " + str(randint(1, 20)) + " et. " +  str(randint(1, 5)) + ", of." + str(randint(1, 100))

# str. <NumeStrada> 3/6, ap. 353
def random_address_format1_short():
	return random_street_short() +  " " + str(randint(1, 20)) + "/" +  str(randint(1,10)) + " ap. " +  str(randint(100, 500))


# str. <NumeStrada> 3/6, ap. 353, Chisinau, Moldova
# TODO: adaugat random un oras
def random_address_complete():
	return random_address_format1() + ", " + random_district() +", Moldova"


# str. <NumeStrada> 3/6, ap. 353, <NumeRaion>
def random_address_district():
	return random_address_format1() + ", " + random_district()
