class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_list = []

        for i in range(len(position)):
            car_list.append([position[i],speed[i]])
        
        starting_car_positions = list(sorted(car_list,key=lambda x: x[0]))
        print(starting_car_positions)

        finish_time = float("-inf")
        fleet_count = 0
        for j in range(len(position)-1,-1,-1):
            cur_finish_time = (target - starting_car_positions[j][0]) / starting_car_positions[j][1]
            print(j,cur_finish_time)
            if cur_finish_time > finish_time:
                fleet_count += 1
                finish_time = cur_finish_time


        return fleet_count


