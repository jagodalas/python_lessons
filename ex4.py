# cars rownsie/equel 100
cars = 100
# romm in the car for 4 people
space_in_the_car = 4.0
# drivers equel 30
drivers = 30
# pasangers equel 90
pasangers = 90
# car emptywithout drivers means no drivers
cars_not_driven = cars - drivers
# car is driven
cars_driven = drivers
# how much can one put in the car or bag
carpool_capacity = cars_driven * space_in_the_car
# average ( durchnittlich) passangers pro auto
average_90_per_car = 90 / cars_driven


print "The are", cars , "cars available."
print "The are only", 30 , "drivers availble."
print " There will be" , cars_not_driven , "empty cars today."
print "We can transport" , carpool_capacity , "people today."
print "We have" , 90 , "to carpool today."
print "We need to put about" , average_90_per_car , "in each car."  
print # means this under the line that you have to put 90 for passengers!!!

print 40 / 4.0
print 40 / 4