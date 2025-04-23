# Not entirely sure this works
class Timer:
    def __init__(self, temp_total_time):
        self.saved_time = 0
        self.total_time = temp_total_time
        
    def start():
        self.saved_Time = millis()
    
    def done():
        passed_time = millis() - saved_Time
        if (passed_time > self.total_time):
            return True
        else:
            return False
