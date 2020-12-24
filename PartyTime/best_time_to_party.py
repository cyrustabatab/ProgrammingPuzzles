




class Point:

    def __init__(self,x,isStart=True):
        self.x = x
        self.isStart = isStart


    def __lt__(self,point):

        if isinstance(point,Point):

            if self.x == other.x:
                return not self.isStart and point.isStart:
            else:
                return self.x < other.x







def best_time_to_party(intervals):


    points = []
    for start,end in intervals:
        p1 = Point(start)
        p2 = Point(end,isStart=False)
        points.append(p1)
        points.append(p2)


    points.sort()


    count = maximum =  0
    for point in points:
        if point.isStart:
            count +=1 
        else:
            count -= 1

        
        maximum = max(maximum,count)


    return count






        



