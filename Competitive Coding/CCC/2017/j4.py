d = int(input("Give the duration of minutes waited:"))
hr = 12
mn = 0
counter = 0 

#Steps:
#We first gotta make a worker clock that can check each passing second.
#We have enough time because the call time of the program is n to the power of 9
#To make the working clock loop for each minute given in the d input
#For every number add a minute to the mn counter
#If the min counter is bigger then 0 and a one to the hour counter
#The hour clock can only display up to 12 so if the counter is more then 12 go back to 1
#






#For I in each minute
for i in range (d):
    mn = int(mn)
    hr = int(hr)
    #Add 1 minute to the minute counter
    mn += 1 
    #If minute is more then 60, reset the minute counter and add 1 to the hours counter
    if mn >= 60:
        mn -= 60
        #If the hour counter + 1 is less the 13 make the hour add one, if the hour counter is more then or = to 13 
        #Hour equals 1
        if hr + 1 < 13:
            hr += 1
        else:
            hr = (hr + 1) % 12
    #If minute is below 10 add a 0 to the the minute
    #For example if the minute is one, you can't display 12:1, you gotta display 12:01
    if mn < 10:
        mn = "0" + str(mn)
    #Otherwise minute = minute, time is good
    else:
        mn = mn 
    #Get the time by making mn and hr into strings and combining those two together into a string
    mn = str(mn)
    hr = str(hr)
    time = hr + mn
    #If time has letters 1:00 to 9:59 3
    #And if the 3rd digit minus the 2nd digit of time equals the 2nd digit minus the 1st digit of time 
    #Add 1 to the counter.
    if len(time) == 3:
        if (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0])):
            counter += 1 
    #If time doesn't equal 3
    # If the fourth digit minus the 3rd digit and the 3rd digit minus the first digit is the same
    # AND if the 3rd digit minus the 2nd digit equals the 2nd digit minus the first digit equals teacher
    # Then + one to the counter        
    else: #Same thing as 3 but with one letter more.
        if ((int(time[3]) - int(time[2])) == (int(time[2]) - int(time[1]))) and ((int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0]))):
            counter += 1 
print(counter)