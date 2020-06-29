def ramr(filename, line):
    fi = open(filename, 'r')
    l = fi.read()
    l = l.split('\n')
    i=0
    for item in l:
        if l[i].startswith('#'):
            l.remove(l[i])
        i = i+1
    del i
    return l[line]
def rr(filename):
    fi = open(filename, 'r')
    l = fi.read()
    l = l.split('\n')
    return l
def get_pkg_attr(attr, filename):
    reg = rr(filename)
    i=0
    try:
        reg.remove('')
    except:
        print(end='')
    indices = []
    for i, elem in enumerate(reg):
        if attr  in elem:
            indices.append(i)
    #print(indices)
    #print(f'Emum found {attr} at {i}. reg[i] reads:')
    return reg[indices[0]].replace(attr,'',1)
def set_pkg_attr(attr,val,filename):
    fi = rr(filename)
    is1 = []

    for i, elem in enumerate(fi):
        if attr  in elem:
            is1.append(i)
    fi[is1[0]]=attr + val
    print(fi[is1[0]])
    fil = open(filename,'w')
    fil.write('')
    fil.close()
    fil = open(filename, 'a')
    for item in fi:
        fil.write(item + '\n')
    fil.close()
