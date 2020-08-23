import matplotlib.pyplot as plt
import numpy as np

def iterate_sir(S0,I0,R0,i,r,dt):
    S,I,R = S0,I0,R0

    N = S0 + I0 + R0
    while True:
        yield S,I,R
        S,I,R = ( S - i*S/N*I*dt,
                  I + (i*S/N*I - r*I)*dt,
                  R + r*I*dt )

def do_sir(S0,I0,R0,i,r,dt,T):

    N0 = S0 + I0 + R0

    get_next = iterate_sir(S0,I0,R0,i,r,dt)

    tlist = np.arange(0,T,dt)
    Slist,Ilist,Rlist = np.zeros((3,len(tlist)))

    for i,t in enumerate(np.arange(0,T,dt)):
        S,I,R = next(get_next)
        Slist[i],Ilist[i],Rlist[i] = S,I,R
        N = S + I + R
        assert abs(N - N0) <= 0.01*N0
    
    return tlist,Slist,Ilist,Rlist

def plot_sir(S0,I0,R0,i,r,dt,T):
    tlist,Slist,Ilist,Rlist = do_sir(S0,I0,R0,i,r,dt,T)
    fig,ax = plt.subplots(figsize=[11,4])
    
    for y,c in zip([Slist,Ilist,Rlist],['orange','red','blue']):
        ax.plot(tlist,y,color=c,lw=2)

    ax.set_ylim(top=S0+I0+R0)
    ax.grid()
    ax.legend(["Susceptible","Infected","Recovered"])

    fig.set_tight_layout(True)
    fig.savefig("out.pdf")

def plot_sir_separate(S0,I0,R0,i,r,dt,T):
    tlist,Slist,Ilist,Rlist = do_sir(S0,I0,R0,i,r,dt,T)

    fig,ax = plt.subplots(3,1,figsize=[11,6],sharey=True)

    for i,y,c,lab in zip([0,1,2],
                     [Slist,Ilist,Rlist],
                     ['orange','red','blue'],
                     ["Susceptible","Infected","Recovered"]):
        ax[i].plot(tlist,y,color=c,lw=2)
        ax[i].grid()
        ax[i].legend(lab)

    ax[0].set_ylim(-10000,S0+I0+R0 + 10000)

    fig.set_tight_layout(True)
    fig.savefig("out.pdf")

# Test
if __name__ == '__main__':
    plot_sir(99960,40,0,2/7,1/7,0.5e-4,200)
