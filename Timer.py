import time

timer = int(input("Enter the time in second: "))

# Set the timer duration in seconds
duration = timer

# Set the timer start time
start_time = time.time()

# Run the timer
while time.time() - start_time < duration:
    # Calculate the time remaining
    time_remaining = duration - (time.time() - start_time)

    # Format the time remaining as a string
    time_remaining_str = time.strftime("%M:%S", time.gmtime(time_remaining))

    # Print the time remaining
    print(f"Time remaining: {time_remaining_str}", end="\r")

    # Pause for one second
    time.sleep(1)

# Timer is finished
print("Timer is finished!")
