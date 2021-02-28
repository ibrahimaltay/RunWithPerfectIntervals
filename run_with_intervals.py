import time

def run_method_with_perfect_intervals(interval_seconds):
    
    #start = time.perf_counter()
    while True:
        timer_start = time.perf_counter_ns()
        print("Hello world")
        timer_stop = time.perf_counter_ns()
        
        print((timer_stop - timer_start)/1000000)
        time.sleep(interval_seconds - (timer_stop - timer_start) / 1000000000)
    #end = time.perf_counter()
    
    #print(f"Completed in: {end - start} seconds!")
