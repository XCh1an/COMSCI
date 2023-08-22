import time

countdown_number = int(input("Enter the starting countdown number: "))

while countdown_number > 0:
    print(countdown_number)
    time.sleep(0.5)
    countdown_number -= 1

print("Blastoff!")
