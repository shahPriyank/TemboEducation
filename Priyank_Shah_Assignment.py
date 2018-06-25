parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

will=input("Do you want to add an activity? ")
if will=="yes":
    name = input("Enter parent's name: ")
    if name not in parents:
        print("Your name is not in our data")
    elif not parents[name]:
        print("You do not have a child listed in our data")
    else:
        activityAdd=input("Enter activity for age: "+ str(parents[name]['age'])+" ")
        flag=0
        for a in activities:
            for k, v in a.items():
                if k == 'age' and v==parents[name]['age']:
                    a['activity'].append(activityAdd) 
                    flag=1
        if flag==0:
            activities.append({'age':parents[name]['age'],'activity':activityAdd})
#for p in activities:
#    print(str(p['activity'])+" "+str(p['age']))


#Iterating through parents dict
day=1
for x in range(5):      #Could not figure out for how long this loop should run
    print("Day: "+str(day))
    for par,child in parents.items():
        if child:
            print(str(par) + " "+ str(child))
            print("Activities for Day: "+ str(day))
            childAge=child['age']
            print(childAge)
            for act in activities:
                for ag,ac in act.items():
                    if ag=='age' and ac==childAge:
                        if day<len(act['activity']):
                            print(par+" : " + str(act['activity'][day-1]))
                        else:
                            print("Curriculum Complete.")
                        
    day+=1
