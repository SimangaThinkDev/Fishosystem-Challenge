from clear import clear
import random, time

try:
    while True:
        grounds = [[random.choices([" ", ">", "#"], [25, 2, 1])[0] for i in range(20)] for j in range(20)]
        clear()
        for row in grounds:
            print(row)
        time.sleep(1)
except KeyboardInterrupt:
    print("Thank you!")
