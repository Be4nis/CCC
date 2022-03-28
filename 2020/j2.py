P = int(input()) #Number of people we want to spread to
N = int(input()) #number of people who have disease on day 0
R = int(input()) #Number of people who spread the disease each day

infected_people = N
infected_last_day = N
day = 0

while infected_people <= P:
    day += 1
    infected_people += infected_last_day * R
    infected_last_day *= R

print (day)