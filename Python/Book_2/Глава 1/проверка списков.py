#печатает список по строкам
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()
'''
#метод сравнения символов списков,
#сравнивает символы одного списка с символами других
def compList(s):
    print('1', s)
    for j in range(len(s[0])-1):  #главный цикл метода
        print('2', s)
        cmm = s[0][j]   #переменная, в которой находится символ 1 списка
        nes = 0         #счетчик количество несовпадений при сравнении
        ex = []      #если True - n'ые символы всех списков равны

        k = len(s) - 1       #Выбирает последний список, для сравнения с первым

        if(k < 1):      #проверяет, остались ли еще списки для сравнения
            print('ВСЕ')
            return s

        else:
            for i in s[k][j:len(s[k])]:     #помещаем в i поочередно все символы списка k от j до последнего
                if (cmm == i):              #сравнивает символ списка 0 с символом списка k

                    if (nes != 0):          #удаляет из списка k символы,
                        for p in range(nes):#которые были до первого совпадения
                            s[k].pop(p)     #

                    print(nes)
                    ex.append(compList(s[j:k]))     #если совпадают, сравнивает этот же символ со следующим списком
                    #s.append(ex)
                    fin = True
                    nes = 0                 #сбрасывает счетчик ошибок
                else:           #если символы не совпадают
                    if (nes != (len(s[k]) - 1)):    #проверяет, совпал ли символ cmm хоть с одним символом списка k
                        nes += 1                    # если совпал, то nes += 1
                    else:                       #если не совпал, удаляет символ cmm и загружает в переменную следующий из s[0]
                        s[0].pop(j)
                        cmm = s[0][j]

            if fin:  #if (k+1 != len(s) and nes == 0):
                return s

    printList2D(s)
'''
#
'''
#метод сравнения символов списков,
#сравнивает символы одного списка с символами других
def compList(s):
    print(s)
    for j in range(len(s[0])-1):  #главный цикл метода
        print('j',j)
        print('s[0]', s[0])
        cmm = s[0][j]   #переменная, в которой находится символ 1 списка
        nes = 0         #счетчик количество несовпадений при сравнении
#        ex = False      #если True - n'ые символы всех списков равны

#        k = len(s) - 1       #Выбирает последний список, для сравнения с первым

        for o in range(1, len(s)):

            for i in range(len(s[o])):     #помещаем в i поочередно все символы списка o от j до последнего
                q = s[o][i]
                print('cmm',cmm)
                print('q',q)
                if (cmm == q):              #сравнивает символ списка 0 с символом списка k
                    print('nes',nes)
                    if (nes != 0):          #удаляет из списка o символы,
                        print('nes1',nes)
                        for p in range(nes-j):#которые были до первого совпадения
                            print('p',p)
                            s[o].pop(j)     #

                    print('nes2',nes)
#                    ex = compList(s[j:o])     #если совпадают, сравнивает этот же символ со следующим списком
                    nes = 0                 #сбрасывает счетчик ошибок
                    break
                else:           #если символы не совпадают
                    if (nes != (len(s[o]) - 1)):    #проверяет, совпал ли символ cmm хоть с одним символом списка k
                        nes += 1                    # если совпал, то nes += 1
                        print('nes3',nes)
                        print('len[s0]-1',len(s[0])-1)
                    else:                       #если не совпал, удаляет символ cmm и загружает в переменную следующий из s[0]
                        if (i != len(s[0])):
                            s[0].pop(j)
                            cmm = s[0][j]
                            nes = 0
                            qwer = j

#                if ex:  #if (k+1 != len(s) and nes == 0):
#                    return True

    printList2D(s)
'''
'''
i - счетчик символов списка 1
j - счетчик списков
o - счетчик символов списка 2
k - счетчик есть ли символ cmm в других списках
'''
a = [[1,4,3],
     [1,2,3],
     [1,2,4]]

res1 = False #список 1 не кончился
cmm = ''    #символ списка 1
CMM = ''    #символ списка 2
dell = False

i = 0       #счетчик символов списка 1
while (not res1):
    cmm = a[0][i]
    res2 = False    #список 2 не кончился

    j = 1   #счетчик списков
    o = i   #счетчик символов списка 2
    while (not res2):
        CMM = a[j][o]

        if (cmm == CMM):
            j += 1
            if (j == len(a)):
                res2 = True
        else:
            for k in range(1, len(a)):
                if(not(cmm in a[k])):       #если символа cmm нет в списке 2 - удаляет
                    dell = True
                else:
                    dell = False
            if(dell):
                a[0].pop(i)
                if (i < len(a[0])):
                    cmm = a[0][i]
                else:
                    res2 =  True
            else:
                a[j].pop(o)
            dell = False
                #o += 1 - без этого все работает

            print('0')


    i += 1
    if (i >= len(a[0])):
        res1 = True

printList2D(a)
