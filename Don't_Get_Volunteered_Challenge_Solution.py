def solution(src, dest):

    if src == dest: return 0

    #src coordinates:
    src_x= int(src/8)
    src_y= src%8

    #dest coordinates:
    dest_x= int(dest/8)
    dest_y= dest%8


    #Generate all possible steps
    def all_possible_steps():
        x=[-1,1,-2,2]
        y=[-1,1,-2,2]
        possible_steps_list=[]
        for each_x in x:
            for each_y in y:
                if abs(each_x)!= abs(each_y):
                    possible_steps_list.append((each_x,each_y))
        return possible_steps_list

    #Calling All Possible Steps' List
    possible_steps= all_possible_steps()
    
    
    #Setting up initial variables
    solution_found= False
    possible_solutions=[(src_x,src_y)]
    np_solutions= [] #next set of possible solutions
    not_solutions=[] #excluded solutions
    step_count=0

    #Here starts the fun
    while solution_found== False:

        #looping through possible solutions list to see if we have got to our destination
        for each_possible_solution in possible_solutions:
            if each_possible_solution[0]==dest_x and each_possible_solution[1]==dest_y:
                solution_found=True
                return step_count

        #Finding the next set of solutions and getting rid of the old ones
        for each_possible_solution in possible_solutions:
            for each_step in possible_steps:

                not_solutions.append(each_possible_solution)
                new_step=(each_possible_solution[0]+each_step[0],each_possible_solution[1]+each_step[1])
                
                #Validating our new found soltution
                if(     new_step[0]>=0 and new_step[0]<=7
                    and new_step[1]>=0 and new_step[1]<=7
                    and new_step not in not_solutions):
                        np_solutions.append(new_step) #adding new step to next possible solutions

        step_count+=1
        possible_solutions=np_solutions
        np_solutions=[]



test=solution(0,63)
print(test)
