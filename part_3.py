try:
    speed = int(input("Enter Motor Speed : "))
    print(f"Speed set to {speed}")
except ValueError: 
    print("Error: Corrupted Signal. Maintaining current speed.") 

def get_coordinate():
    while True:
        try:
            x = int(input("Enter X-coordinate: "))

            if x > 100 or x < -100:
                print("Coordinate out of range")
            else:
                return x 
        except ValueError: 
            print("Invalid Coordinate") 

coordinate = get_coordinate() 
print(f"Coordinate Recieved: {coordinate}")
