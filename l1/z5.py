def tabliczka(x1, x2, y1, y2):
    print('\t'+'\t'.join([str(x) for x in range(x1, x2+1)]))
    for j in range(y1,y2+1):
        print(str(j)+'\t'+'\t'.join([str(i*j) for i in range(x1,x2+1)]))

tabliczka(1,10,20,30)
