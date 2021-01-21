class listy:
    def ob(lst=[]):
        lista = [[]]
        for i in range(0,100):
            if (i>(len(lst)-1)):
                break
            else:
                lista.append([lst[i]])
                for j in range(1,10):
                    if i+j>(len(lst)-1):
                        break
                    else:
                        lista.append([lst[i],lst[i+j]])
                        for k in range(1,10):
                            if i+j+k>(len(lst)-1):
                                break
                            else:
                                lista.append([lst[i],lst[i+j],lst[i+j+k]])
                                for m in range(1,10):
                                    if (i+j+k+m)==(len(lst)-1):
                                        break
                                    elif i+j+k+m>(len(lst)-1):
                                        break
                                    else:
                                        lista.append([lst[i],lst[i+j],lst[i+j+k],lst[i+j+k+m]])

        lista.append(lst)
        print(lista)
listy.ob([1,2,3,4])


        