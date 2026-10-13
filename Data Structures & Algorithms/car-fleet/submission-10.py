class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # associate position & speed for each car
        # sort by position, descending order
        # maintain a number of fleets, by keeping a monotonically increasing stack of times to target, where each represents a fleet

        last_time = 0
        num_fleets = 0
        
        sorted_cars = sorted(zip(position, speed), reverse = True)

        for position, speed in sorted_cars:
            time = (target - position) / speed

            if time > last_time:
                num_fleets += 1
                last_time = time
        
        return num_fleets