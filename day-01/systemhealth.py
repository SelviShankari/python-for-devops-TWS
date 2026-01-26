import psutil

cpu_threshold=float(input("Enter your cpu threshold: "))
cpu_utilized=psutil.cpu_percent(interval=1)

def cpu_check():
    if cpu_threshold<cpu_utilized:
        print("Alert !!!!!, The utilizaiton has crossed the limit. This is your current utilization: ",cpu_utilized)
    else:
        print("Everything ok for now!!,This is your current utilization: ",cpu_utilized)    

cpu_check() 