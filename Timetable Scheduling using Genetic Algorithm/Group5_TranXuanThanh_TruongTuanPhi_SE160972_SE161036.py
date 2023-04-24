import random

class Data:
    def __init__(self):
        self.classes = []
        self.teachers = []
        self.rooms = []
        self.subjects = []
        self.semesters = []
        self.majors = []
        self.syllabuses = []
        self.currentSem = None
        self.currentNumSlotDay = 0
        self.currentNumDayWeek = 0
        self.listAssign = []
        self.classSubjectsNumSlotWeek = None
        self.subjectAndClasses = None

class Teacher:
    def __init__(self,code,name,Email,Phone,Studying,Subjects,minSlot,maxSlot,skipDays):
        self.code = code
        self.name = name
        self.email = Email
        self.phone = Phone
        self.studying = Studying
        subjects = Subjects.strip().replace(' ','').split(',')
        self.subjects = subjects
        self.minSlot = int(minSlot)
        self.maxSlot = int(maxSlot)
        self.skipDays_text = skipDays.strip().replace(' ','').split(',') #load file
        skipDays = []
        for day in self.skipDays_text:
            if day == 'Mon':
                skipDays.append(2)
            elif day == 'Tue':
                skipDays.append(3)
            elif day == 'Wed':
                skipDays.append(4)
            elif day == 'Thu':
                skipDays.append(5)
            elif day == 'Fri':
                skipDays.append(6)
            elif day == 'Sat':
                skipDays.append(7)
            elif day == 'Sun':
                skipDays.append(8)
        self.skipDays = skipDays
        self.key = self.code
        self.currentSlot = 0
        self.numSloteachSubject = {}

class Classes:
    def __init__(self,name,Major):
        self.name = name
        self.major = Major
        self.key = self.name

class Major:
    def __init__(self,major,nameMajor):
        self.major = major
        self.nameMajor = nameMajor
        self.key = self.major

class Subject:
    def __init__(self,codeSubject,nameSubject,numberOfSlots):
        self.code = codeSubject
        self.name = nameSubject
        self.numSlot = int(numberOfSlots)
        self.key = self.code

class Syllabus:
    def __init__(self,codeSemester,Major,Subjects):
        self.codeSem = codeSemester
        self.major = Major
        self.subjects = Subjects
        self.key = (self.major,self.codeSem)

class Semester:
    def __init__(self,codeSemester,nameSemester,numberOfWeeks):
        self.code = codeSemester
        self.name = nameSemester
        self.numWeek = int(numberOfWeeks)
        self.key = self.code

class Room:
    def __init__(self,nameRoom,typeRoom,Description):
        self.name = nameRoom
        self.type = typeRoom
        self.des = Description
        self.key = self.name

class Individual:
    def __init__(self,chromosomes):
        self.chromosomes = chromosomes
    def fitness(self):
        score = 0
        check_conflicts_Lecturer = []
        check_conflicts_Location = []
        check_conflicts_Class = []
        check_double_slot = {}
        for k in self.chromosomes:
            if (k[3],k[4],k[5]) in check_conflicts_Location:
                score -= 1
            else:
                check_conflicts_Location.append((k[3], k[4], k[5]))
            if (k[0],k[3],k[4]) in check_conflicts_Class:
                score -= 1
            else:
                check_conflicts_Class.append((k[0], k[3], k[4]))
            if (k[2],k[3],k[4]) in check_conflicts_Lecturer:
                score -= 1
            else:
                check_conflicts_Lecturer.append((k[2],k[3],k[4]))
            if k[3] in k[2].skipDays:
                score -= 1
            # check double slot: only use this if you are sure about your data.
            if (k[3], k[1], k[0]) in check_double_slot:
                info = check_double_slot[(k[3], k[1], k[0])]
                if k[5] != info[0]:
                    score -= 0.1
                if abs(k[4] - info[1]) > 1:
                    score -= 0.1
            else:
                check_double_slot[(k[3], k[1], k[0])] = (k[5], k[4])  # room, slot
            # end check double slot

        return score

    def printWeeklySchedule(self,Data):
        print()
        # print Schedule for classes:
        print('=' * (10 + 7 * 25 + 8))
        print()
        for clas in Data.classes:
            print(('WEEKLY SCHEDULE FOR CLASS: '+str(clas.name)).center(10 + 7 * 25 + 8,' '))
            print(('Semester: '+str(Data.currentSem.name)).center(10 + 7 * 25 + 8,' '))
            print('=' * (10 + 7 * 25 + 8))
            print(' '*10,'Monday'.center(25,' '),'Tuesday'.center(25,' '),'Wednesday'.center(25,' '),'Thursday'.center(25,' '),'Friday'.center(25,' '),'Saturday'.center(25,' '),'Sunday'.center(25,' '),sep='|')
            print('-'* (10 + 7 * 25 + 8))
            for slot in range(1,Data.currentNumSlotDay+1):
                line1 = {2:'',3:'',4:'',5:'',6:'',7:'',8:''}
                line2 = {2:'',3:'',4:'',5:'',6:'',7:'',8:''}
                # line 1: print info about room, subject
                print(('Slot '+str(slot)).center(10,' '),end='|')
                for k in self.chromosomes:
                    if k[0] == clas:
                        if int(k[4]) == slot:
                            line1[int(k[3])] += k[1].code + ' at: '+k[5].name
                            line2[int(k[3])] += 'Teacher: '+k[2].code
                for k in line1:
                    if line1[k] == '':
                        line1[k] = ' '*25
                for k in line2:
                    if line2[k] == '':
                        line2[k] = ' '*25
                for a,b in line1.items():
                    print(b.center(25,' '),end='|')
                print()
                print(' '*10,end='|')
                # line 2: print info about lecturer
                for a,b in line2.items():
                    print(b.center(25,' '),end='|')
                print()
            print('=' * (10 + 7 * 25 + 8))
            print()
        #print Schedule for teachers:
        print('='*(10+7*25+8))
        print()
        for teacher in Data.teachers:
            print(('WEEKLY SCHEDULE FOR TEACHER: ' + str(teacher.name)).center(10 + 7 * 25 + 8, ' '))
            print(('Teacher code: '+str(teacher.code)).rjust(10 + 7 * 25 + 8, ' '))
            print(('Semester: ' + str(Data.currentSem.name)).center(10 + 7 * 25 + 8, ' '))
            print('=' * (10 + 7 * 25 + 8))
            print(' ' * 10, 'Monday'.center(25, ' '), 'Tuesday'.center(25, ' '), 'Wednesday'.center(25, ' '),'Thursday'.center(25, ' '), 'Friday'.center(25, ' '), 'Saturday'.center(25, ' '),'Sunday'.center(25, ' '), sep='|')
            print('-' * (10 + 7 * 25 + 8))
            for slot in range(1, Data.currentNumSlotDay + 1):
                # line 1: print info about room, subject
                line1 = {2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
                line2 = {2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
                print(('Slot ' + str(slot)).center(10, ' '), end='|')
                for k in self.chromosomes:
                    if k[2] == teacher:
                        if int(k[4]) == slot:
                            line1[int(k[3])] += k[1].code + ' at: ' + k[5].name
                            line2[int(k[3])] += 'Class: ' + k[0].name
                for k in line1:
                    if line1[k] == '':
                        line1[k] = ' ' * 25
                for k in line2:
                    if line2[k] == '':
                        line2[k] = ' ' * 25
                for a, b in line1.items():
                    print(b.center(25, ' '), end='|')
                print()
                # line 2: print info about class
                print(' ' * 10, end='|')
                for a, b in line2.items():
                    print(b.center(25, ' '), end='|')
                print()
            print('=' * (10 + 7 * 25 + 8))
            print()

    def printWeeklyManagement(self,Data):
        print('\n')
        print()
        # print Schedule for classes:
        print('=' * (100))
        print()
        # chromo = (Class, subject, teacher, day, slot, room, label)
        print('weekly work plan'.upper().center(100,' '))
        print(('Semester: ' + str(Data.currentSem.name)).center(100, ' '))
        print('=' * (100))
        print()
        days = {2: 'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday',8:'Sunday'}
        for k in range(Data.currentNumDayWeek):
            print()
            print(('* '+str(days[k+2])+' *').upper().center(100,'-'))
            print()
            for slot in range(Data.currentNumSlotDay):
                print((' - Slot: ' + str(slot+1)))
                for chromosome in self.chromosomes:
                    if chromosome[3] == (k+2) and chromosome[4] == (slot+1):
                        print('     + Lecturer: ',chromosome[2].name\
                              , ' - teaching Class: ',chromosome[0].name,\
                              ' - at room: ',chromosome[5].name)
            print()
        print('=' * (100))
        print('\n\n')


class Population:
    def __init__(self,Data,size):
        self.individuals = []
        for k in range(size):
            chromosomes = makeChromosomes(Data)
            individual = Individual(chromosomes)
            self.individuals.append(individual)

class Load_File:
    def load_Lecturer_file(self):
        teachers = []
        fileName = input('Enter your lecturers file name: ')
        if len(fileName) < 1:
            fileName = 'Lecturers.txt'
        gv = open(fileName, 'r', encoding='UTF-8')
        gv = gv.readlines()
        checkFirst = True
        for line in gv:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            teachers.append(Teacher(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], ))
        checkFile(teachers, fileName)
        return teachers

    def load_Classes_file(self):
        classes = []
        fileName = input('Enter your classes file name: ')
        if len(fileName) < 1:
            fileName = 'Classes.txt'
        cl = open(fileName, 'r', encoding='UTF-8')
        cl = cl.readlines()
        checkFirst = True
        for line in cl:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            classes.append(Classes(line[0], line[1]))
        checkFile(classes, fileName)
        return classes

    def load_Majors_file(self):
        majors = []
        fileName = input('Enter your majors file name: ')
        if len(fileName) < 1:
            fileName = 'Majors.txt'
        mj = open(fileName, 'r', encoding='UTF-8')
        mj = mj.readlines()
        checkFirst = True
        for line in mj:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            majors.append(Major(line[0], line[1]))
        checkFile(majors, fileName)
        return majors

    def load_Subjects_file(self):
        subjects = []
        fileName = input('Enter your subjects file name: ')
        if len(fileName) < 1:
            fileName = 'Subjects.txt'
        sb = open(fileName, 'r', encoding='UTF-8')
        sb = sb.readlines()
        checkFirst = True
        for line in sb:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            subjects.append(Subject(line[0], line[1], line[2]))
        checkFile(subjects, fileName)
        return subjects

    def load_Syllabuses_file(self):
        syllabuses = []
        fileName = input('Enter your syllabuses file name: ')
        if len(fileName) < 1:
            fileName = 'Syllabuses.txt'
        sy = open(fileName, 'r', encoding='UTF-8')
        sy = sy.readlines()
        checkFirst = True
        for line in sy:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            sub = line[-1].strip().replace(' ', '').split(',')
            syllabuses.append(Syllabus(line[0], line[1], sub))
        checkFile(syllabuses, fileName)
        return syllabuses

    def load_Semester_file(self):
        semesters = []
        fileName = input('Enter your semesters file name: ')
        if len(fileName) < 1:
            fileName = 'Semesters.txt'
        S = open(fileName, 'r', encoding='UTF-8')
        S = S.readlines()
        checkFirst = True
        for line in S:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            semesters.append(Semester(line[0], line[1], line[2]))
        checkFile(semesters, fileName)
        return semesters

    def load_Rooms_file(self):
        rooms = []
        fileName = input('Enter your rooms file name: ')
        if len(fileName) < 1:
            fileName = 'Rooms.txt'
        r = open(fileName, 'r', encoding='UTF-8')
        r = r.readlines()
        checkFirst = True
        for line in r:
            if checkFirst == True:
                checkFirst = False
                continue
            if len(line) <= 1:
                continue
            line = line.strip().split('\t')
            rooms.append(Room(line[0], line[1], line[2]))
        checkFile(rooms, fileName)
        return rooms

def checkFile(listObject,fileName):
    print('Your file ', fileName, ' is being processed...')
    listCheck = []
    for ob in listObject:
        if ob.key in listCheck:
            print('The key ',ob.key,' is NOT UNIQUE! Please check your ',fileName,' file again.')
            quit()
        else:
            listCheck.append(ob.key)
    print('Congratulation. Your ',fileName,' file is imported successfully!')
    print('='*20)

def makeClassSubjectsNumSlotWeek(Data):
    classSubjectsNumSlotWeek = {}
    for clas in Data.classes:
        classSubjectsNumSlotWeek[clas] = {}
        for sy in Data.syllabuses:
            if sy.key == (clas.major, Data.currentSem.code):
                subs = sy.subjects
                for sub in subs:
                    for k in Data.subjects:
                        if k.code == sub:
                            if k.numSlot % Data.currentSem.numWeek == 0:
                                classSubjectsNumSlotWeek[clas][k] = k.numSlot // Data.currentSem.numWeek
                            else:
                                classSubjectsNumSlotWeek[clas][k] = k.numSlot // Data.currentSem.numWeek + 1
    return classSubjectsNumSlotWeek

def makeSubjectAndClasses(Data):
    subjectAndClasses = {}
    for subject in Data.subjects:
        subjectAndClasses[subject] = {}
        subjectAndClasses[subject]['num'] = 0
        subjectAndClasses[subject]['classes'] = []
        for a,b in Data.classSubjectsNumSlotWeek.items():
            for c,d in b.items():
                if c.code == subject.code:
                    subjectAndClasses[subject]['num'] = d
                    subjectAndClasses[subject]['classes'].append(a)
    return subjectAndClasses

def makeAssignList(Data):
    listAssign = []
    for subject, b in Data.subjectAndClasses.items():
        if b['num'] == 0:
            continue
        total = b['num'] * len(b['classes'])
        Data.subjectAndClasses[subject]['teachers'] = []
        for teacher in Data.teachers:
            for k in teacher.subjects:
                if k == subject.code:
                    Data.subjectAndClasses[subject]['teachers'].append(teacher)
        if Data.subjectAndClasses[subject]['teachers'] == []:
            print('\n','='*50,'\n','CANNOT MAKE SCHEDULE: Not enough lecturer for the subject: ', subject.code)
            quit()
        sumMin = 0
        sumMinTuple = 0
        sumMax = 0
        for teacher in Data.subjectAndClasses[subject]['teachers']:
            sumMin += teacher.minSlot
            if teacher.minSlot % b['num'] == 0:
                sumMinTuple += teacher.minSlot // b['num']
            elif teacher.minSlot % b['num'] != 0:
                sumMinTuple += teacher.minSlot // b['num'] + 1
            sumMax += teacher.maxSlot
        if sumMax < total:
            print('\n','='*50,'\n','CANNOT MAKE SCHEDULE: Not enough lecturer fo the subject: ', subject.code)
            quit()
        for teacher in Data.teachers:
            teacher.numSloteachSubject[subject] = 0
        teacherList = Data.subjectAndClasses[subject]['teachers'].copy()
        teacherList = sorted(teacherList, key=lambda x: x.minSlot, reverse=True)
        while total > 0 and teacherList != []:
            teacherList = sorted(teacherList, key=lambda x: (x.currentSlot + 0.0001) / (x.minSlot + 0.0001),reverse=False)
            if teacherList[0].currentSlot + b['num'] <= teacherList[0].maxSlot:
                teacherList[0].currentSlot += b['num']
                teacherList[0].numSloteachSubject[subject] += b['num']
                total -= b['num']
            else:
                teacherList.remove(teacherList[0])
        if total > 0:
            print('\n','='*50,'\n','CANNOT MAKE SCHEDULE: Not enough lecturer for the subject:', subject.code)
            quit()
        classListtoAssign = Data.subjectAndClasses[subject]['classes'].copy()
        for teacher in Data.subjectAndClasses[subject]['teachers']:
            numOfClass = teacher.numSloteachSubject[subject] // b['num']
            for j in range(numOfClass):
                which = random.randint(0, len(classListtoAssign) - 1)
                cl = classListtoAssign[which]
                if (cl, subject, teacher, b['num']) not in listAssign:
                    listAssign.append((cl, subject, teacher, b['num']))
                classListtoAssign.remove(cl)
        if classListtoAssign != []:
            print('\n','='*50,'\n','CANNOT MAKE SCHEDULE: Not enough lecturer.')
            quit()
    return listAssign

def makeChromosomes(Data):
    chromosomes = []
    '''#try  THIS USE FOR COMPARISION 2 ALGS
    lst_lo = []
    lst_p = []
    lst_pG = []
    #end'''
    for k in Data.listAssign:
        for j in range(k[3]):
            '''#try THIS USE FOR COMPARISION 2 ALGS
            while True:
                day = random.randint(2, numDayWeek + 1)
                slot = random.randint(1, numSlotDay)
                r = random.randint(0, len(Data.rooms) - 1)
                nst = (k[0], k[1], k[2], day, slot, Data.rooms[r], 'label: ' + str(j + 1) + '/' + str(k[3]))
                if (nst[3],nst[4],nst[5]) not in lst_lo and (nst[0],nst[3],nst[4]) not in lst_p and (nst[1],nst[3],nst[4]) not in lst_pG:
                    lst_lo.append((nst[3],nst[4],nst[5]))
                    lst_p.append((nst[0],nst[3],nst[4]))
                    lst_pG.append((nst[1],nst[3],nst[4]))
                    break
                else:
                    continue
            chromosomes.append(nst)
            #end'''
            day = random.randint(2, Data.currentNumDayWeek + 1)
            slot = random.randint(1, Data.currentNumSlotDay)
            r = random.randint(0, len(Data.rooms) - 1)
            chromosome = (k[0], k[1], k[2], day, slot, Data.rooms[r], 'label: ' + str(j + 1) + '/' + str(k[3]))
            chromosomes.append(chromosome)
    return chromosomes

def crossOver(individual_1,individual_2):
    fatherChromosomes = individual_1.chromosomes
    motherChromosomes = individual_2.chromosomes
    childChromosomes = []
    for k in range(len(individual_1.chromosomes)):
        which = random.randint(1,10)
        if which > 5:
            childChromosomes.append(fatherChromosomes[k])
        else:
            childChromosomes.append(motherChromosomes[k])
    individual_child = Individual(childChromosomes)
    return individual_child

def mutateIndividual(currentIndividual):
    currentChromosomes = currentIndividual.chromosomes
    randomChromosomes = makeChromosomes(Data)
    mutateChromosomes = []
    for k in range(len(currentChromosomes)):
        which = random.randint(0,100)
        if which <= RATE_INDIVIDUAL_MUTATE:
            mutateChromosomes.append(randomChromosomes[k])
        else:
            mutateChromosomes.append(currentChromosomes[k])
    mutate_individual = Individual(mutateChromosomes)
    return mutate_individual

def chooseTopFromHalfPopulation(population):
    l = len(population.individuals)//2+1
    listCandidate = []
    for i in range(l):
        while True:
            which = random.randint(0,len(population.individuals)-1)
            if population.individuals[which] not in listCandidate:
                listCandidate.append(population.individuals[which])
                break
    listCandidate = sorted(listCandidate,key=lambda x:x.fitness(),reverse=True)
    return listCandidate[0]

def makeCrossoverPop(population):
    crossOverPop = Population(Data,0)
    population.individuals = sorted(population.individuals,key=lambda x:x.fitness(),reverse=True)
    for k in range(NUMBER_POPULATION_SELECTION):
        crossOverPop.individuals.append(population.individuals[k])
    for k in range(NUMBER_POPULATION_SELECTION,SIZE_POPULATION,1):
        individual_1 = chooseTopFromHalfPopulation(population)
        individual_2 = chooseTopFromHalfPopulation(population)
        individual_child = crossOver(individual_1,individual_2)
        crossOverPop.individuals.append(individual_child)
    return crossOverPop

def mutatePopulation(population):
    mutate_population = Population(Data,0)
    population.individuals = sorted(population.individuals,key=lambda x:x.fitness(),reverse=True)
    for k in range(NUMBER_POPULATION_SELECTION):
        mutate_population.individuals.append(population.individuals[k])
    for k in range(NUMBER_POPULATION_SELECTION,SIZE_POPULATION):
        currentIndividual = population.individuals[k]
        mutate_individual = mutateIndividual(currentIndividual)
        mutate_population.individuals.append(mutate_individual)
    return mutate_population


if __name__ == '__main__':

    Data = Data()

    #=== LOAD FILE ===
    print(' LOAD DATA FROM FILE '.center(50,'='),'\n')
    fhandle = Load_File()
    # create teacher list = teachers:
    Data.teachers = fhandle.load_Lecturer_file()
    # create class list = classes:
    Data.classes = fhandle.load_Classes_file()
    # create major list = majors:
    Data.majors = fhandle.load_Majors_file()
    #finish creating major list of majors (type: class Major)
    # create subject list = subjects:
    Data.subjects = fhandle.load_Subjects_file()
    #finish creating subject list of subjects (type: class Subject)
    # create syllabus list = syllabuses:
    Data.syllabuses = fhandle.load_Syllabuses_file()
    #finish creating syllabus list of syllabuses (type: class Syllabus)
    # create semester list = semesters:
    Data.semesters = fhandle.load_Semester_file()
    #finish creating semester list of semesters (type: class Semester)
    # create room list = rooms:
    Data.rooms = fhandle.load_Rooms_file()
    #finish creating room list of rooms (type: class Room)

    #=== START MAKING SCHEDULE ===

    while True:
        try:
            print('\n')
            print(' Semesters '.upper().center(50, '='))
            k=1
            for sem in Data.semesters:
                print(k,'. ',sem.name,sep='')
                k+=1
            chooseSem = int(input('Choose the semester you want to make schedule for:  '))
            numSlotDay = int(input('How many slots are there in a day: '))
            numDayWeek = int(input('How many learning days are there in a week: '))
        except:
            continue
        else:
            if numDayWeek > 7 or numDayWeek <= 0 or numSlotDay <= 0 or chooseSem < 1 or chooseSem > k-1:
                print('ERROR: Please enter again.')
                continue
            break


    currentSemester = Data.semesters[chooseSem-1]

    Data.currentNumSlotDay = numSlotDay
    Data.currentNumDayWeek = numDayWeek
    Data.currentSem = currentSemester

    Data.classSubjectsNumSlotWeek = makeClassSubjectsNumSlotWeek(Data)
    Data.subjectAndClasses = makeSubjectAndClasses(Data)
    Data.listAssign = makeAssignList(Data)


    SIZE_POPULATION = 9
    NUMBER_POPULATION_SELECTION = 3
    RATE_INDIVIDUAL_MUTATE = 10

    population = Population(Data,SIZE_POPULATION)

    if Data.currentNumSlotDay * Data.currentNumDayWeek * len(Data.rooms) < len(population.individuals[0].chromosomes):
        print('\n','='*50,'\n','CANNOT MAKE SCHEDULE: Not enough rooms.')
        quit()

    population.individuals = sorted(population.individuals, key=lambda x: x.fitness(), reverse=True)
    number_of_generation = 1

    from datetime import datetime
    now = datetime.now()
    before_time = float(str(now.time()).split(':')[-1])

    print("We're making schedule for you...")
    print()

    while population.individuals[0].fitness() < 0:
        number_of_generation += 1
        #print('Thế hệ thứ: ', number_of_generation)
        #print('fitness của cá thể mạnh nhất đến nay là: ', population.individuals[0].fitness())
        crossOverPop = makeCrossoverPop(population)
        population = mutatePopulation(crossOverPop)
        population.individuals = sorted(population.individuals, key=lambda x: x.fitness(), reverse=True)

    now = datetime.now()
    after_time = float(str(now.time()).split(':')[-1])

    # print Results:
    #print('=' * 20)
    #print('Fitness của cá thể mạnh nhất đến nay là: ', population.individuals[0].fitness())
    population.individuals[0].printWeeklySchedule(Data)
    population.individuals[0].printWeeklyManagement(Data)

    print('DONE. Time: ', after_time - before_time,'s.')
    print('='*30)
    print('\nThank you for using our services! <3 <3')

    input()

#this