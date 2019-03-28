# The Captain's Room


def captains_room(k, room_list):

    room_numbers = sorted([int(i) for i in room_list.split()])
    return (k * sum(set(room_numbers)) - sum(room_numbers))//(k-1)
     

if __name__ == "__main__":
#    k = int(input())
#    room_list = input()
    k = 5
    room_list = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'
    print(captains_room(k, room_list))
