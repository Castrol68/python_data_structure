def selection_sort(lists):
    count = len(lists)
    for i in range(count):
        min_index = i
        for j in range(i+1,count):
            if lists[min_index] > lists[j]:
                min_index = j
        lists[min_index], lists[i] = lists[i], lists[min_index]
    return lists

if  __name__=="__main__":
    lists=[3,4,2,8,9,5,1]
    print('排序前序列为:')
    for i in lists:
        print(i,end=' ')
    print('\n排序后结果为:',end=' ')
    for i in selection_sort(lists):
        print(i,end=' ')