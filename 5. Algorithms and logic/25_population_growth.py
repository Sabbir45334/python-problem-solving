# The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. 
# For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000

population = 10000
year = 10
for i in range(10):
    population = population / 1.10
    year = year - i
    print(f"{year}th year - {round(population)}")