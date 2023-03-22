import random
import time

class elevator:

    def __init__(self ,maxFloors, elevatorMoveTime):

        self.currentFloor = 0
        self.nextFloor = None
        self.maxFloors = maxFloors
        self.floorQueue = []
        self.elevatorMoveTime = elevatorMoveTime
        self.direction = "Up"

    def setFloorQueue(self):
        for i in range(self.maxFloors):
            self.floorQueue.append(0)

    def toggleOn(self,floorNumber):
        self.floorQueue[floorNumber] = 1

    def toggleOff(self, floorNumber):
        self.floorQueue[floorNumber] = 0

    def floorOcuppied(self, floorNumber):
        self.floorQueue[floorNumber] = "Ocuppied"

    def slicedQueueUp(self):
        return self.floorQueue[self.currentFloor + 1:]

    def slicedQueueDown(self):
        slicedQueueDown = self.floorQueue[0: self.currentFloor ]
        slicedQueueDown.reverse()

        return slicedQueueDown

    def setDirection(self):
        if 1 in self.slicedQueueUp() and 1 not in self.slicedQueueDown():
            self.direction = "Up"
        elif 1 in self.slicedQueueDown() and 1 not in self.slicedQueueUp():
            self.direction = "Down"

    def getNextFloor(self):
        if self.direction == "Up":
            self.nextFloor = self.slicedQueueUp().index(1) + self.currentFloor + 1

        elif self.direction == "Down":
            self.nextFloor = (len(self.slicedQueueDown()) - self.slicedQueueDown().index(1) - 1)

    def reachedFloor(self):
        self.toggleOff(self.currentFloor)
        # self.floorOcuppied(self.nextFloor)
        self.currentFloor = self.nextFloor
        self.nextFloor = None

    def getMaxFloors(self):
        return self.maxFloors

    def getDirection(self):
        return self.direction

    def getCurrentFloor(self):
        return self.currentFloor

    def getFloorQueue(self):
        return self.floorQueue





def main():
    Elevate = elevator(5, 3)
    Elevate.setFloorQueue()
    print(Elevate.floorQueue)
    print(f"The staring Direction: {Elevate.direction}\n")

    Elevate.toggleOn(1)
    Elevate.toggleOn(3)

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    Elevate.toggleOn(0)
    Elevate.toggleOn(2)
    Elevate.toggleOn(4)

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    Elevate.toggleOn(4)

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    Elevate.toggleOn(1)

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

    Elevate.toggleOn(0)

    print(Elevate.floorQueue)
    Elevate.setDirection()
    Elevate.getNextFloor()
    print(f"The next Floor the Elevator is going to is: {Elevate.nextFloor}")
    Elevate.reachedFloor()
    print(Elevate.floorQueue)
    print(f"The Elevator has reached the Floor: {Elevate.currentFloor}\n")

if __name__ == "__main__":
   main()


# class randomPeople:
#     def __init__(self, elevatorObj, peopleRange):
#         self.elevatorObj = elevatorObj
#         self.maxFloors = self.elevatorObj.maxFloors
#         self.peopleRange = peopleRange
#         self.floorHash = {}
#
#     def initialization(self):
#         for i in range(self.maxFloors):
#             self.floorHash[i] = [0] * self.maxFloors
#
#     def __populatePeople(self):
#         currentFloor = random.randrange(self.maxFloors)
#         nextFloor = random.randrange(self.maxFloors)
#
#         if currentFloor == nextFloor:
#             pass
#         else:
#             nextFloorList = self.floorHash.get(currentFloor)
#             nextFloorList[nextFloor]+=1
#             self.floorHash[currentFloor] = nextFloorList
#             self.elevatorObj.toggleOn(currentFloor)
#
#     def fillFloors(self):
#         people = random.randrange(3,self.peopleRange)
#         for i in range(people):
#             self.__populatePeople()
#
#
#
# class MovePeople:
#     def __init__(self, elevatorObj, randomPeopleObj):
#         self.elevatorObj = elevatorObj
#         self.randomPeopleObj = randomPeopleObj
#         self.floorGetOffList = [0] * self.elevatorObj.maxFloors
#
#     def atCurrentFloor(self):
#         if self.floorGetOffList[self.elevatorObj.currentFloor] != 0:
#             print(f"{self.floorGetOffList[self.elevatorObj.currentFloor]} People have gotten off at Floor {self.elevatorObj.currentFloor}")
#             self.floorGetOffList[self.elevatorObj.currentFloor] = 0
#
#     def __floorGetOffSet(self, start, stop, currentFloorList):
#         for i in range(start, stop):
#             if currentFloorList[i] != 0:
#                 self.floorGetOffList[i] += currentFloorList[i]
#                 print(f"{currentFloorList[i]} people are on the elevator" )
#                 self.elevatorObj.toggleOn(i)
#                 print(f"Floor {i} has been toggled")
#                 currentFloorList[i] = 0
#         self.randomPeopleObj.floorHash[self.elevatorObj.currentFloor] = currentFloorList
#
#     def goingToNextFloor(self):
#         if self.elevatorObj.getDirection() == "Up":
#             currentFloorList = self.randomPeopleObj.floorHash[self.elevatorObj.currentFloor]
#             self.__floorGetOffSet(self.elevatorObj.currentFloor +1,self.elevatorObj.maxFloors, currentFloorList)
#
#         elif self.elevatorObj.getDirection() == "Down":
#             currentFloorList = self.randomPeopleObj.floorHash[self.elevatorObj.currentFloor]
#             self.__floorGetOffSet(0,self.elevatorObj.currentFloor + 1, currentFloorList)
#
#
#
# #Inilization Conditions
# elevate = elevator(5,5)
# elevate.setFloorQueue()
#
#
# people = randomPeople(elevate,10)
# people.initialization()
# people.fillFloors()
#
#
# peopleMove = MovePeople(elevate,people)
#
# # Elevator Movement Conditions - Prints have been added to show inner Workings, since no gui is present currently
# while(True):
#     print(f"{peopleMove.floorGetOffList} this is the list of people who have to get off at each floor")
#     print(f"{people.floorHash} This is the Floor Hash")
#     print(f"{elevate.getFloorQueue()} This is the Floor Queue")
#     print(f"{elevate.getCurrentFloor()} This is the current Floor")
#     elevate.setDirection()
#     peopleMove.atCurrentFloor()
#     peopleMove.goingToNextFloor()
#     elevate.getNextFloor()
#     print(f"The next Floor the Elevator is going to is: {elevate.nextFloor}")
#     elevate.reachedFloor()
#     print(f"The Elevator has reached the Floor: {elevate.currentFloor}")
#     print(elevate.floorQueue)
#     time.sleep(elevate.elevatorMoveTime)
#     people.fillFloors()
#     print("\n")











