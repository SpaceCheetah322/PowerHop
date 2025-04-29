# Inspired by a Processing class written by Daniel Shiffman. Rewritten by Katelyn.
# Should work as a countdown; use start() when you want to start counting down, and done() to check if it's finished.
# NOTE: Not entirely sure this works yet.
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


"""
This is a temporary instance of the timer class, currently compatible with all of the files. This should work and cause no errors.

# -*- coding: utf-8 -*-
class Timer:
    def __init__(self, total_time):
        self.saved_time = 0
        self.total_time = total_time

    def start(self):
        self.saved_time = millis()

    def done(self):
        return (millis() - self.saved_time) > self.total_time

"""
