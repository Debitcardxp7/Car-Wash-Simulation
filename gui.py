import tkinter as tk
from Queue_Simulation import simulate_car_wash

def update_label():
    from Queue_Simulation import average_wait_time, average_cars_per_hour, average_cars_washed_per_hour, cars_entered, cars_washed  # Re-import values
    result_label.config(text= f"Simulation Results:\n"
                            f"Total cars entered: {cars_entered}\n"
                            f"Total cars washed: {cars_washed}\n"
                            f"Average wait time: {average_wait_time:.2f} minutes\n"
                            f"Average cars entered per hour: {average_cars_per_hour:.2f}\n"
                            f"Average cars washed per hour: {average_cars_washed_per_hour:.2f}")
    animate_cars(cars_washed)
    create_carwash()

def animate_cars(num_cars):
    #animates cars moving through wash
    def move_car(x, car, wheel1, wheel2):
        if x < 300 and x < 110:
            canvas.move(car, 5, 0)
            canvas.move(wheel1, 5, 0)
            canvas.move(wheel2, 5, 0)
            canvas.after(50, move_car, x+5, car, wheel1, wheel2)
        elif x < 300 and x >= 110:
            canvas.move(car, 5, 0)
            canvas.move(wheel1, 5, 0)
            canvas.move(wheel2, 5, 0)
            canvas.after(50, move_car, x+5, car, wheel1, wheel2)
            canvas.itemconfig(car, fill="blue")
        else:
            canvas.delete(car)
            canvas.delete(wheel1)
            canvas.delete(wheel2)
    #creates cars
    for i in range(num_cars):
          # Car body
        car = canvas.create_rectangle((10, 30, 60, 60), fill="brown")

        # Wheels (two black circles)
        wheel1 = canvas.create_oval((20, 60, 30, 70), fill="black")
        wheel2 = canvas.create_oval((40, 60, 50, 70), fill="black")

        # Start the animation for each car with a delay
        root.after(i * 800, lambda c=car, w1=wheel1, w2=wheel2: move_car(0, c, w1, w2))
def create_carwash():
    global car_wash
    car_wash = canvas.create_rectangle((110, 10, 180, 70), fill="red")
    canvas.create_text(145, 40, text="Car Wash", fill="white")
def on_button_click():
    try:
        minutes = int(entry.get())
        simulate_car_wash(minutes)
        update_label()
    except ValueError:
        print("Please enter a valid number")
        result_label.config(text="Please enter a valid number")

#sets window
root = tk.Tk()
root.title("Car Wash Simulation")

#allows label to give description
label = tk.Label(root, text="Enter the number of minutes to simulate:")
label.pack(pady=5)

#allows user to enter number of minutes
entry = tk.Entry(root)
entry.pack(pady=5)

#creates a label to display the results
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

#creates a button to start the simulation
button = tk.Button(root, text="Start Simulation", command=on_button_click)
button.pack(pady=20)

#creates a canvas to animate cars
canvas = tk.Canvas(root, width=350, height=100, bg="lightgray")
canvas.pack()

root.mainloop()