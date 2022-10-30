#!/usr/bin/env python3
from constraint import Problem, AllDifferentConstraint, ExactSumConstraint


# Task 1    
def Travellers(List):
    problem = Problem ()
    people = [ "claude" , "olga" , "pablo" , "scott"]
    times = [ "2:30" , "3:30" , "4:30" , "5:30"]
    destinations = [ "peru" , "romania" , "taiwan" , "yemen"]
    t_variables = list ( map ( lambda x : "t_" +x , people ))
    d_variables = list ( map ( lambda x : "d_" +x , people ))
    problem.addVariables ( t_variables , times )
    problem.addVariables ( d_variables , destinations )
    problem.addConstraint ( AllDifferentConstraint () , t_variables )
    problem.addConstraint ( AllDifferentConstraint () , d_variables )

    #Claude is either the person leaving at 2:30 pm or the traveller leaving at 3:30 pm.
    problem.addConstraint((lambda x: (x == "2:30") or (x == "3:30")), ["t_claude"])

    #The person leaving at 2:30 pm is flying from Peru.
    for person in people:
        problem.addConstraint((lambda x, y: (x != "2:30") or
            ((x == "2:30") and (y == "peru"))), 
            ["t_" + person, "d_" + person])

    #The person flying from Yemen is leaving earlier than the person flying from Taiwan.
    for personA in people:
        for personB in people:
            if (personA != personB):
                problem.addConstraint(
                    (lambda x,y,z,a: ( y!="yemen" or 
                        a!="taiwan" or
                        ((y=="yemen") and (a=="taiwan")) and (x<z))), 
                    ["t_" + personA, "d_"+personA, "t_"+personB, "d_" + personB])

    #The four travellers are Pablo, the traveller flying from Yemen, the person leaving at 2:30 pm 
    #and the person leaving at 3:30 pm.
    problem.addConstraint(lambda x,y: (x != "2:30") and (x!="3:30") and (y!="yemen"), 
        ["t_pablo", "d_pablo"])

    for person in people:
        problem.addConstraint(lambda x,y: (x!="yemen") or 
            ((x=="yemen") and (y!="2:30") and (y!="3:30")), 
            ["d_" + person, "t_" + person])

    #Person inputted must be at time inputted
    for i in range(0, len(List)):
        if (List[i][1] == "2:30"):
            problem.addConstraint(lambda x: (x=="2:30"), ["t_"+List[i][0]])
        elif (List[i][1] == "3:30"):
            problem.addConstraint(lambda x: (x=="3:30"), ["t_"+List[i][0]])
        elif (List[i][1] == "4:30"):
            problem.addConstraint(lambda x: (x=="4:30"), ["t_"+List[i][0]])
        elif (List[i][1] == "5:30"):
            problem.addConstraint(lambda x: (x=="5:30"), ["t_"+List[i][0]])

    solns = problem.getSolutions()
    return (solns)


# Task 2
def CommonSum(n):
    return int(sum(range(1,(n*n)+1))/n)

# Task 3
def msqList(m, pairList):
    problem = Problem()
    problem.addVariables(range(0, m*m), range(1, m*m+1))
    problem.addConstraint(AllDifferentConstraint() , range(0, m*m))

    for row in range (m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [(row * m) + i for i in range (m)])

    for col in range (m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [col+(m*i) for i in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [i + (m*i) for i in range(m)])
    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [(m-1)*(1+i) for i in range(m)])

    for item in pairList:
        problem.addConstraint(ExactSumConstraint(item[1]), [item[0]])

    solns = problem.getSolutions()
    return (solns)


# Task 4
def pmsList(m, pairList):
    problem = Problem()
    problem.addVariables(range(0, m*m), range(1, m*m+1))
    problem.addConstraint(AllDifferentConstraint() , range(0, m*m))

    for row in range (m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [(row * m) + i for i in range (m)])

    for col in range (m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [col+(m*i) for i in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [i + (m*i) for i in range(m)])
    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [(m-1)*(1+i) for i in range(m)])

    dd = [] #each member of dd is a list of variables lying along some broken diagonal

    #number of upward and downward diagonals = m
    for i in range(m): #for each diagonal
        currentDiagonal = [i]
        for j in range(m-1): #for each row in the square
            if (((j+1)*m)-1 == currentDiagonal[len(currentDiagonal)-1]): #if on the edge, wrap around to the other side
                currentDiagonal.append(currentDiagonal[len(currentDiagonal)-1]+1)
            #else, don't wrap to the other side
            else:
                currentDiagonal.append(currentDiagonal[len(currentDiagonal)-1]+m+1)
        dd.append(currentDiagonal)
    print(dd)

    for i in range(m): #for each diagonal
        currentDiagonal = [i]
        for j in range(m-1): #for each row in the square
            if (currentDiagonal[len(currentDiagonal)-1]%m == 0): #if on the edge, wrap around to the other side
                currentDiagonal.append(currentDiagonal[len(currentDiagonal)-1]+m+(m-1))
            #else, don't wrap to the other side
            else:
                currentDiagonal.append(currentDiagonal[len(currentDiagonal)-1]+m-1)
        dd.append(currentDiagonal)
    print (dd)

    for pair in dd:
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [pair[i] for i in range(0,m)])

    for pair in pairList:
        problem.addConstraint(ExactSumConstraint(pair[1]), [pair[0]])

    solns = problem.getSolutions()
    return (solns)

#print(Travellers([["olga", "2:30"], ["claude", "3:30"]]))
#print(msqList(4,[[0,13],[1,12],[2,7]]))
print(pmsList(4, [[0,13],[1,12],[2,7]]))

# Debug
if __name__ == '__main__':
    print("debug run...")

   