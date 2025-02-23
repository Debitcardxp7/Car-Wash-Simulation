import random

class queue:
    def __init__(self):
        #creates an empty queue
        self.items = []
    def isEmpty(self):
        #checks if the queue is empty
        return self.items == []
    def enqueue(self, item):
        #adds an item to the queue
        self.items.insert(0, item)
    def dequeue(self):
        #removes an item from the queue
        return self.items.pop()
    def size(self):
        #returns the size of the queue
        return len(self.items)

#initialize global variables
average_wait_time = 0
average_cars_per_hour = 0
average_cars_washed_per_hour = 0 
cars_entered = 0
cars_washed = 0

def simulate_car_wash(duration):
    #initialize global variables
    global average_wait_time, average_cars_per_hour, average_cars_washed_per_hour, cars_entered, cars_washed
    #initialize local variables
    car_line = queue()
    current_time = 0
    car_id = 1
    busy = False
    total_wait_time = 0

    while current_time < duration:
        #randomly check if a car has entered the queue
        if random.randint(1,10) <= 2:
            car_line.enqueue((car_id, current_time))
            print(f"Car {car_id} entered the queue at time {current_time}")
            car_id += 1
            cars_entered += 1
        #check if wash is busy
        if busy:
            time_until_free -= 1
            if time_until_free == 0:
                busy = False
        #check if car is in queue and wash if it is
        if not car_line.isEmpty() and not busy:
            car, arrival_time = car_line.dequeue()
            wait_time = current_time - arrival_time
            total_wait_time += wait_time
            wash_time = random.randint(2, 5)
            print(f"Car {car} is being washed at time {current_time} after waiting {wait_time} minutes")
            busy = True
            time_until_free = wash_time
            cars_washed += 1
        else:
            current_time += 1
        
    #get averages
    average_wait_time = total_wait_time / cars_washed
    average_cars_per_hour = cars_entered / (duration / 60)
    average_cars_washed_per_hour = cars_washed / (duration / 60)

    #print results
    print("\nSimulation Results:")
    print(f"Total cars entered: {cars_entered}")
    print(f"Total cars washed: {cars_washed}")
    print(f"Average wait time: {average_wait_time:.2f} minutes")
    print(f"Average cars entered per hour: {average_cars_per_hour:.2f}")
    print(f"Average cars washed per hour: {average_cars_washed_per_hour:.2f}")

simulate_car_wash(120)