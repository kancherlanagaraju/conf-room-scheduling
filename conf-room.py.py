roomsTxt = """7.11,8,9:00,9:15,14:30,15:00
8.23,6,10:00,11:00,14:00,15:00
8.43,7,11:30,12:30,17:00,17:30
9.511,9,9:30,10:30,12:00,12:15,15:15,16:15
9.527,4,9:00,11:00,14:00,16:00
9.547,8,10:30,11:30,13:30,15:30,16:30,17:30
"""

input = "5,8,10:30,11:30" # 5 team members, located on the 8th floor, meeting time 10:30 - 11:30 Output: 9.547

#print("rooms: " + roomsTxt)
#print("input; " + input)

def time_slot_matches(room, input):
    input_start_time = input[2]
    input_end_time = input[3]
    found = False
    i = 2
    while True:
        try:
            if room[i] == input_start_time and room[i+1] == input_end_time:
                found = True
                break
            i += 2
        except:
            break # End of time slots in room
    return found

def capacity_matches(room, input):
    return True if int(room[1]) >= int(input[0]) else False
    

rooms_list = []
input_list = []
filtered_rooms = []
for room in roomsTxt.split("\n"):
    cols = room.split(",")
    rooms_list.append(cols)

input_list = input.split(',')


# Filter rooms matching input time slot
for room in rooms_list:
    if time_slot_matches(room, input_list):
        filtered_rooms.append(room)

fr1 = []
for room in filtered_rooms:
    if capacity_matches(room, input_list):
        fr1.append(room)

result = {}
for room in fr1:
    input_floor = int(input_list[1])
    room_floor = int(room[0].split('.')[0])
    result[room[0]] = abs(input_floor - room_floor)
top = sorted(result.items(), key=lambda x: x[1])
print("Available Conf Room: " + top[0][0])





