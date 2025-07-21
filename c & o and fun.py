class car:
    def __init__(self):
        self.has_called = False
    def engine_start(self):
        if not self.has_called():
            self.has_called = True
            return "this function is called for 1 st time"
        else:
            return "this function is already called"
    def engine_off(self):
        if self.has_called == True:
            return "vehicle stopped"
            self.has_called = False
        else:
            return "start the engine"
            
    def acc(self):
        if self.has_called == True:
            return "lets go"
        else:
            return "start the engine"
    def break_vehicle(self):
        if self.has_called == True:
            return "break"
        else:
            return "start the vehicle"
            
vehicle = car()
result = vehicle.acc()
print(result)
