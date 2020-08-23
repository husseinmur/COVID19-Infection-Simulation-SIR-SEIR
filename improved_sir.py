import matplotlib.pyplot as plt

def gen(S0 ,In0 ,Is0, R0 ,i ,r , p, dt):
    S, In, Is, R = S0, In0, Is0, R0
    N = S + In + Is + R
    while True :gf
        yield S, In, Is, R
        S, In, Is, R = (S - i*S/N*In*dt,
                        In + ((1-p)*i*S/N*In - r*In)* dt,
                        Is + (p*i*S/N*In-r*Is)*dt,
                        R + (r*In+r*Is)*dt)

def trajectory(S0 ,In0 ,Is0, R0 ,i ,r , p):
    t = 0
    T = 100
    dt = 0.1
    tlist = [0]
    Slist, Inlist, Islist, Rlist = [S0], [Is0], [In0], [R0]
    i = gen(S0 ,In0 ,Is0, R0 ,i ,r , p, dt)
    while (t<=T):
        t+=dt
        tlist += [t]
        S, In, Is, R = next(i)
        Slist += [S]
        Inlist += [In]
        Islist += [Is]
        Rlist += [R]
    return Slist, Inlist, Islist, Rlist, tlist

S, In, Is, R, tlist= trajectory(99980,2000,100,0,0.7,0.14,0.7)

plt.plot(tlist,S)
plt.plot(tlist,In)
plt.plot(tlist,Is)
plt.plot(tlist,R)
plt.show()
print(S)