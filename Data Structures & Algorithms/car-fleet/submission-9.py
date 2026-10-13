class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # associate position & speed for each car
        # sort by position, descending order
        # maintain a number of fleets, by keeping a monotonically increasing stack of times to target, where each represents a fleet

        cars = []
        fleets = []

        for idx, p in enumerate(position):
            cars.append([p, speed[idx]])
        
        sorted_cars = sorted(cars, key = lambda car: car[0] * -1)

        for position, speed in sorted_cars:
            time = (target - position) / speed

            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)