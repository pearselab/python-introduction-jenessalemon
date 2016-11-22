bubble = [5, 34, 9, 10, 3]      #Random list I made for an example
def bubble_sort(to_sort):
    length = len(to_sort) - 1
    sorted = False
    while not sorted:           #This is kind of like the counter used in intro.py. It's used to tell python when to stop looping.
        sorted = True
        for i in range(length):
            if to_sort[i] > to_sort[i+1]: #If the element on the left is less than the element on the right
                sorted = False            #We're not done yet
                to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i] #So make the switch
                print(to_sort) #I put the print statement here so that each pass through the list can be seen. Obviously if this were to be used on a huge data set, I would remove this print statement.

print(bubble_sort(bubble))
