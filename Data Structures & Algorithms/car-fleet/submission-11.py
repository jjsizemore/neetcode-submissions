class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # associate position & speed for each car
        # sort by position, descending order
        # maintain a number of fleets, by keeping a monotonically increasing stack of times to target, where each represents a fleet

        fleets = []
        
        sorted_cars = sorted(zip(position, speed), reverse = True)

        for position, speed in sorted_cars:
            time = (target - position) / speed

            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)