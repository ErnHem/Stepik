main_dict = dict()
main_dict['global']=[]
global_ns = main_dict['global']
m = 0
hook = 0

def add(ns, n_val, cur_ns = global_ns):
    if ns == 'global':
        main_dict['global'].append(n_val)
    else:
        for el_ns in cur_ns:
            if type(el_ns)==dict:
                if ns in el_ns:
                    el_ns[ns].append(n_val)
                else:
                    for k in el_ns.keys():
                        add(ns, n_val, el_ns[k])

def create (n_val, ns, cur_ns = global_ns):
    if ns == 'global':
        new_ns = {n_val:[]}
        main_dict['global'].append(new_ns)
    else:
        for el_ns in cur_ns:
            if type(el_ns)==dict:
                if ns in el_ns:
                    new_ns = {n_val:[]}
                    el_ns[ns].append(new_ns)
                else:
                    for el_sub_ns in el_ns.values():
                        create(n_val, ns, el_sub_ns)
def get (ns, n_val, cur_ns = main_dict, z=1):
    global m
    global hook
    if m == 1:
        return
    if ns == 'global':
        if n_val in cur_ns[ns]:
            print ('global')
            m = 1
            return
        else:
            print (None)
            m = 1
    if ns in cur_ns:

        if n_val in cur_ns[ns]:
            print (ns)
            return True
        else:
            get(z, n_val)
    else:
        n=0
        for el_ns in cur_ns:
            for cur_el in cur_ns[el_ns]:

                if type(cur_el)==dict:
                    if(get(ns, n_val, cur_el, el_ns)):
                        m = 1
                        return
com = []
n = input()
for i in range(int(n)):
    a, b, c = map(str,input().split())
    com.append((a,b,c))
for i in range(len(com)):
    if com[i][0]=='add':
        add(com[i][1], com[i][2])
    if com[i][0]=='create':
        create(com[i][1], com[i][2])
    if com[i][0]=='get':
        get(com[i][1], com[i][2])
        m = 0