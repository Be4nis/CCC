# x = int(input())
# coords = []
# for i in range(x):
#     h = (input())
#     h = h.split(' ')
#     h = list(map(int, h))
#     coords.append(h)

# averages = []    

# for i in range(len(coords)):
#     d1 = coords[i]
#     try:
#         d2 = (coords[i+1])
#         distance = abs(d2[1] - d1[1])
#         time = abs(d2[0] - d1[0])
#         speed = distance/time
#         averages.append(speed)
#     except IndexError:
#         break

# print (max(averages))

n = int(input())
observations = []

for i in range(n):
    observation = {}
    line = input().split()
    observation['time'] = int(line[0])
    observation['pos'] = int(line[1])
    observations.append(observation)

def get_time(dict):
    return dict['time']

observations.sort(key = get_time)

max_speed = None
previous_time = None
previous_pos = None

for observation in observations:
    time = observation['time']
    pos = observation['pos']

    if previous_time == None:
        previous_time = time
        previous_pos = pos
        continue

    time_diff = time - previous_time
    distance = abs(pos - previous_pos)
    speed = distance/time_diff

    if max_speed == None or speed > max_speed:
        max_speed = speed
    previous_time = time
    previous_pos = pos

print (max_speed)



