class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        buildings.sort(key=lambda x: (x[0],x[1]))
        covered_buildings = set()

        for i in range(1, len(buildings)-1):
            if buildings[i-1][0] == buildings[i][0] and buildings[i+1][0] == buildings[i][0]:
                covered_buildings.add(str(buildings[i][0]) + ":" + str(buildings[i][1]))
        
        buildings.sort(key=lambda x: (x[1],x[0]))
        # print(covered_buildings)

        for i in range(1, len(buildings)-1):
            if buildings[i-1][1] == buildings[i][1] and buildings[i+1][1] == buildings[i][1]:
                continue
            building = str(buildings[i][0]) + ":" + str(buildings[i][1])
            if building in covered_buildings:
                covered_buildings.remove(building)
        
        first_building = str(buildings[0][0]) + ":" + str(buildings[0][1])
        if first_building in covered_buildings:
            covered_buildings.remove(first_building)
        last_building = str(buildings[-1][0]) + ":" + str(buildings[-1][1])
        if last_building in covered_buildings:
            covered_buildings.remove(last_building)
        
        return len(covered_buildings)


        # 1,2  2,1  2,2  2,3  3,2

        