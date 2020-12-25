




class Point:

    def __init__(self,x,isStart=True):
        self.x = x
        self.isStart = isStart


    def __lt__(self,point):

        if isinstance(point,Point):

            if self.x == point.x:
                return not self.isStart and point.isStart
            else:
                return self.x < point.x







def best_time_to_party(intervals):


    points = []
    for start,end in intervals:
        p1 = Point(start)
        p2 = Point(end,isStart=False)
        points.append(p1)
        points.append(p2)


    points.sort()


    count = maximum =  0
    best_hour = None
    for point in points:
        if point.isStart:
            count +=1 
        else:
            count -= 1

        
        if count > maximum:
            maximum =count
            best_hour = point.x

    print(f"The best time to party is at {best_hour}")

# Exercises

def best_time_to_party_2(intervals,your_start,your_end):
    # best time to party bewtween two intervals


    points = []

    for start,end in intervals:
        p1 = Point(start)
        if your_start <= start < your_end:
            points.append(p1)
        p2 = Point(end,isStart=False)

        if your_start <= end < your_end:
            points.append(p2)

    points.sort()


    count = maximum =  0
    best_hour = None
    for point in points:
        if point.isStart:
            count +=1 
        else:
            count -= 1

        
        if count > maximum:
            maximum =count
            best_hour = point.x

    print(f"The best time to party is at {best_hour} where you will see {maximum} celebrities")


def best_time_to_party_alternative(intervals):
    # choose each celebrity interval and determine how many other celebrity intervals contain the chosen celebrity's start time. Pick the time to attend the party to be the start time of the celebrity whose start time contained in the maximum number of other celebrity intervals

    maximum = 0
    maximum_interval = None
    for interval in intervals:
        start,end = interval
        count = 0
        for other_interval in intervals:
            if other_interval is interval:
                continue
            other_start,other_end = other_interval

            if other_start <= start < other_end:
                count += 1
        

        if count > maximum:
            maximum = count
            maximum_interval = interval


    

    print(f"The best time to party is at {maximum_interval[0]}")



class Point2:

    def __init__(self,x,weight,isStart=True):
        self.x = x
        self.weight = weight
        self.isStart = isStart

    def __lt__(self,point):
        if isinstance(point,Point):

            if self.x == point.x:
                return not self.isStart and point.isStart
            else:
                return self.x < point.x



def best_time_to_party_weighted(intervals):
    points = []
    for start,end,weight in intervals:
        p1 = Point2(start,weight)
        p2 = Point2(end,weight,isStart=False)
        points.append(p1)
        points.append(p2)


    points.sort()


    count = maximum =  0
    best_hour = None
    for point in points:
        if point.isStart:
            count +=point.weight 
        else:
            count -= point.weight

        
        if count > maximum:
            maximum =count
            best_hour = point.x

    print(f"The best time to party is at {best_hour}")



if __name__ == "__main__":
    

    intervals = [(6,7),(7,9),(10,11),(10,12),(8,10),(9,11),(6,8)]
    
    intervals_weighted = [(6,8,2),(6.5,12.0,1),(6.5,7.0,2),
                          (7.0,8.0,2),(7.5,10.0,3),(8.0,9.0,2),
                          (8.0,10.0,1),(9.0,12.0,2),
                          (9.5,10,4),(10,11,2),
                          (10,12,3),(11,12,7)]
    your_availability = (6,10)
    best_time_to_party_weighted(intervals_weighted)


        



