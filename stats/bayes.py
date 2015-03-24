def f(p):
    return p
def inv(p):
    return 1-p
def prob_n(p,n):
    k=1
    p_total=p
    while k<n:
        p_total=p_total*p
        k+=1
    return p_total
def prob_n_3_1(p):
    return 3*p*inv(p)*inv(p)
def prob_ab(p1,p2):
    return p1*p2
def multi_flip(pa,p1,p2):
    p_total=pa*p1+inv(pa)*p2
    return p_total
def p_pos(pc,p_pc,p_nnc):
    p_total=pc*p_pc+inv(pc)*inv(p_nnc)
    return p_total
def p_neg(pc,p_pc,p_nnc):
    p_total=pc*inv(p_pc)+inv(pc)*p_nnc
    return p_total
def p_a_given_b(pc,p_pc,p_nnc):
    return (pc*p_pc)/p_pos(pc,p_pc,p_nnc)
def p_a_given_nb(pc,p_pc,p_nnc):
    return (pc*inv(p_pc))/p_neg(pc,p_pc,p_nnc)

def p_loaded(p_l,num_h,num_t):

    if num_h!=0:
        p_total_h=p_l
        k=1
        while k<num_h:
            p_total_h*=p_l
            k+=1
    else:
        p_total_h=0
    if num_t!=0:
        l=1
        p_total_t=inv(p_l)
        while l<num_t:
            p_total_t*=inv(p_l)
            l+=1

    else:
        p_total_t=0
    if num_t!=0 and num_h!=0:
        p_total=p_total_h*p_total_t
    else:
        p_total=p_total_t+p_total_h
    print("probability coin is loaded is",p_total)
    return p_total


def p_fair(num_h,num_t):
    p_l=.5
    if num_h!=0:
        p_total_h=p_l
        k=1
        while k<num_h:
            p_total_h*=p_l
            k+=1
    else:
        p_total_h=0
    if num_t!=0:
        l=1
        p_total_t=inv(p_l)
        while l<num_t:
            p_total_t*=inv(p_l)
            l+=1

    else:
        p_total_t=0
    if num_t!=0 and num_h!=0:
        p_total=p_total_h*p_total_t
    else:
        p_total=p_total_t+p_total_h
    print("probability coin is loaded is",p_total)
    return p_total

nh=2
nt=3
p1=.9*p_fair(nh,nt)/(.1*p_loaded(.9,nh,nt)+.9*p_fair(nh,nt))



print(p1)