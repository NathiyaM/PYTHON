from Palindromechecker import Deque

def palchecker(a_string):
    char=Deque.Deque()
    for i in a_string:
        char.add_rear(i)
        still_equal=True
    while char.size()> 1 and still_equal:
        front = char.remove_front()
        rear=char.remove_rear()
        if front!=rear:
            still_equal=False
    return still_equal

print(palchecker('radar'))
