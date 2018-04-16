import math
class Node:
    
    def __init__(self,name,xx=0,yy=0):
        self.name=name
        self.x=xx
        self.y=yy
        self.successors = []
    
    def Add(self,v,distance):
        if v in self.successors:
            return
        else:
            self.successors.append([v,distance])
            v.successors.append([self,distance])

def AddSucc(fringe,successor,h_g):
    if len(fringe)!=0:
        for i in range(len(fringe)):
            if fringe[i][1]>h_g:
                fringe.insert(i,[successor,h_g])
                return
    else:
        fringe.append([successor,h_g])
    return 
def heheuristic(start,goal,mode="E"):
    if(mode=="E"):
        return math.sqrt(math.pow(start.x-goal.x,2)+math.pow(start.y-goal.y,2))
    if(mode=="M"):
        return math.fabs(start.x-goal.x)+math.fabs(start.y-goal.y)

def notin(fringe,succ):
    for node in fringe:
        if node[0]==succ:
            return False
    return True

def affiche(path):
    for val in path:
        print val.name,

def AStar(start,goal,mode="E"):
    fringe=[[start,heheuristic(start,goal,mode)]]
    path=[]
    print fringe[0][0].name
    while len(fringe)!=0 or fringe[0][0]==goal:
        path.append(fringe[0])
        for succ in path[-1][0].successors:
            if notin(fringe,succ[0]):
                AddSucc(fringe,succ[0],heheuristic(succ[0],goal,mode)+succ[1]) 
        fringe.remove(fringe[0])
    affiche(path)
    
point1=Node("1")
point2=Node("2",1,0)
point3=Node("3",2,0)

point4=Node("4",0,1)
point5=Node("5",1,1)
point6=Node("6",2,1)

point7=Node("7",0,2)
point8=Node("8",1,2)
point9=Node("9",2,2)

point1.Add(point2,1)
point1.Add(point4,1)

point2.Add(point3,1)
point2.Add(point5,1)

point3.Add(point6,1)

point4.Add(point5,1)
point4.Add(point7,1)

point5.Add(point6,1)
point5.Add(point8,1)

point6.Add(point9,1)

point7.Add(point8,1)

point8.Add(point9,1)

pa=AStar(point1,point7,"M")
#affiche(pa)
#print heheuristic(Arade,Node,"M")
