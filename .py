def find_minimum_platforms(arr, dep):

    # Convert time strings (HH:MM) to minutes since midnight

    def time_to_minutes(time_str):

        hours, minutes= map(int, time_str.split(':'))

        return hours * 60 + minutes

    # Convert times to minutes

    arr = [time_to_minutes(time) for time in arr]

    dep = [time_to_minutes(time) for time in dep]

    # Sort both arrival and depature times

    arr.sort()

    dep.sort()

    # Initialize pointers and counters

    platform_needed=0

    max_platforms= 0

    i=j=0

    # Traverse through both the sorted arrays.

    while i<len(arr) and j<len(dep):

        # If a_train_is arriving before the earliest train departs.

        if arr[i]< dep[j]:

            platform_needed += 1

            i += 1

            max_platforms= max(max_platforms, platform_needed)

        else:

            # A train departs

            platform_needed -= 1

            j+= 1

    return max_platforms



# Test cases.

arr1 = ["9:00", "9:40","9:50", "11:00", "15:00", "18:00"]

dep1 = ["9:10","12:00", "11:20", "11:30", "19:00", "20:00"]

arr2 = ["9:00","9:40"]

dep2 = ["9:10","12:00"]

print("Minimum platforms needed (Case 1) :", find_minimum_platforms(arr1, dep1))  # Output: 3

print("Minimum platforms needed (Case 2) :", find_minimum_platforms(arr2, dep2))  # Output: 1