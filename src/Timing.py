import time


class Timing:
    time_spent = 0.0
    stop_time = 0.0
    start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()
        
    def get_measured_time(self):
        return float(self.stop_time - self.start_time)
