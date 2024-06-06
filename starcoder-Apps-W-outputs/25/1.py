
#The ships can be attacked in any order.
#The answer is the maximum amount of gold the ships can steal.
#This includes the number of ships, bases and the order in which they are given.
#No need to include the maximum number of gold.

#the input is the attacking power of each spaceship.
#the next lines contain the defensive power and gold of each base.
#the output is the maximum gold that each spaceship can steal.

#store the input
attacking_power = [1, 3, 5, 2, 4]
base_defensive_power = [0, 4, 2, 9]
base_gold = [1, 2, 8, 4]

#use a dictionary to store the number of gold stolen by each ship.
gold = {}

#create a list to store the defensive powers and gold of the bases.
defensive_power_and_gold = list(zip(base_defensive_power, base_gold))

#sort the list by the defensive powers.
defensive_power_and_gold.sort()

#start with the base with the smallest defensive power.
gold_stolen = 0
base_index = 0

#iterate through the attacking power of each ship and check if it can destroy the bases.
for i in range(len(attacking_power)):
    #check if the attacking power of the ship is greater than the defensive power of the base.
    while defensive_power_and_gold[base_index][0] <= attacking_power[i]:
        #add the gold stolen by the ship.
        gold_stolen += defensive_power_and_gold[base_index][1]
        #move to the next base.
        base_index += 1
        #check if all bases have been destroyed.
        if base_index == len(defensive_power_and_gold):
            break
    #store the total gold stolen by the ship.
    gold[i] = gold_stolen

#print the gold stolen by each ship.
print(gold)

