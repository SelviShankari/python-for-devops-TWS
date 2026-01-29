import psutil

def check_memory_utilization():
    try:
        mem_threshold=int(input("Enter the memory threshold in percentage: "))
    except ValueError :
        print("Invalid input! Please enter a numeric value.")
        return # instead of throwing error returns the above statement as the output
    else :
        pass

    actual_mem_utilized=psutil.virtual_memory() # psutil.virtual_memory() returns mutliple vlaues in form of tuple. Eg:- total , available , percent , used , free
    mem_utilized_percent=actual_mem_utilized[2] # Since i want only the percentage value im using the index 2

    if mem_threshold > mem_utilized_percent :
        print("Memory is underutilized")
    else :
        print("Memory is overutilized")

check_memory_utilization()