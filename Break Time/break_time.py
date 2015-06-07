import time
import webbrowser

total_breaks = 3
break_count = 0

print("The program started at " + time.ctime())
while break_count < total_breaks:
    time.sleep(50*60)   # Break after 50mins
    print("Played video at " + time.ctime())
    webbrowser.open("https://youtu.be/7fkyMKZXUS0")
    break_count = break_count + 1
