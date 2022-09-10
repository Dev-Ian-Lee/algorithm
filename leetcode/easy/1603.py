# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:
    lot = [0, 0, 0]

    def __init__(self, big: int, medium: int, small: int):
        self.lot[0] = big
        self.lot[1] = medium
        self.lot[2] = small

    def addCar(self, carType: int) -> bool:
        if(self.lot[carType - 1] != 0):
            self.lot[carType - 1] -= 1
            return True
        
        else:
            return False