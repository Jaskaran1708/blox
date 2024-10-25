import time

call_limit = 15  
time_window = 60  
penalty_time = 60 
call_count = 0  
start_time = time.time()  
penalty_active = False  

def rate_limited_api_call(input):
    global call_count, start_time, penalty_active

    current_time = time.time()

    if current_time - start_time > time_window:
        call_count = 0 
        start_time = current_time 
        penalty_active = False 

    if penalty_active:
        wait_time = penalty_time
        print(f"Penalty active! Waiting for {wait_time:.2f} seconds.")
        time.sleep(wait_time)
        penalty_active = False  
        return rate_limited_api_call(input)  

    if call_count < call_limit:
        call_count += 1
        return call_me(input)  
    else:
        penalty_active = True
        wait_time = time_window  
        print(f"Limit reached! Waiting for penalty of {wait_time:.2f} seconds.")
        time.sleep(wait_time)
        return rate_limited_api_call(input)  

def call_me(input):
    print(f"API called with input: {input}")
    return f"Response from API for {input}"

if __name__ == "__main__":
    for i in range(31):  
        print(f"Making API call {i+1}")
        response = rate_limited_api_call(f"Test input {i+1}")
        print(response)
