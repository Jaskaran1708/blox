
import time
from collections import deque

call_limit = 15  
refresh_token_interval = 60 / call_limit  

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def consume_token(self):
        current_time = time.time()
        a = current_time - self.last_refill
        tokens_to_add = int(a / self.refill_rate)

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill = current_time

        if self.tokens > 0:
            self.tokens -= 1
            return True
        else:
            return False

def rate_limited_api_call(inputs):
    bucket = TokenBucket(call_limit, refresh_token_interval)  

    for input_data in inputs:
        while not bucket.consume_token():
            print("Limit reached. Waiting for token refill...")
            time.sleep(refresh_token_interval)

        print(f"Calling API with input: {input_data}")
        call_me(input_data)  

def call_me(input_data):
    print(f"API called with input: {input_data}")

if __name__ == "__main__":
    test_inputs = [f"Test input {i+1}" for i in range(20)] 
    rate_limited_api_call(test_inputs)
