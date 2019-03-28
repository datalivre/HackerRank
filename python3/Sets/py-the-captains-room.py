# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room

def captains_room(k, room_list):

    room_numbers = sorted([int(i) for i in room_list.split()])
    return (k * sum(set(room_numbers)) - sum(room_numbers))//(k-1)


if __name__ == "__main__":
    k = int(input())
    room_list = input()
    print(captains_room(k, room_list))

