import matplotlib.pyplot as plt
import numpy as np

def PPV(V,D,P):
    ppv = V*D / (V*D + (100-D)*(100-P))
    #print(ppv)
    return ppv

def NPV(V,D,P):
    npv = P*(100-D) / (P*(100-D)+D*(100-V))
    return npv



def Prevalance(D,V,P):
    specificity = np.arange(78,100,3)
    sensitivity = np.arange(100)
    ppvs = []
    npvs = []
    for specs in specificity:
        yppv = []
        ynpv = []
        for sense in sensitivity:
            ppval = PPV(sense,D,specs)
            npval = NPV(sense,D,specs)
            yppv.append(ppval)
            ynpv.append(npval)
        ppvs.append(yppv)
        npvs.append(ynpv)


    fig, ax1 = plt.subplots(figsize=(30,20))

    ax2 = ax1.twinx()




    for ind, result in enumerate(ppvs):
        ax1.plot(sensitivity, result,'o')
        ax2.plot(sensitivity, npvs[ind])

        #plt.plot(sensitivity, result)
    plt.legend(specificity, prop={'size': 16})
    #plt.xlabel('Sensitivity')
    #plt.ylabel('Predictive Value')

    ax1.set_xlabel('Sensitivity',size=20)
    ax1.set_ylim([0,1])
    ax2.set_ylim([0,1])
    ax1.set_ylabel('Positive Predictive Value ("o" marker)',size=20)
    ax2.set_ylabel('Negative Predictive Value (line marker)',size=20)
    ax2.tick_params(axis="y",labelsize=20)
    ax1.tick_params(axis="x",labelsize=20)
    ax1.tick_params(axis="y",labelsize=20)
    plt.title("NPV and PPV with Prevalance of {}%".format(D),size=20)
    #plt.show()
    fig.savefig("NPVandPPVwithPrevalanceof{}%".format(D))
    plt.close(fig)


def Same_Sensitivity(D,V,P):
    specificity = np.arange(78,100,3)
    prevalance = np.arange(100)
    ppvs = []
    npvs = []
    for specs in specificity:
        yppv = []
        ynpv = []
        for prev in prevalance:
            ppval = PPV(V,prev,specs)
            npval = NPV(V,prev,specs)
            yppv.append(ppval)
            ynpv.append(npval)
        ppvs.append(yppv)
        npvs.append(ynpv)


    fig, ax1 = plt.subplots(figsize=(30,20))

    ax2 = ax1.twinx()




    for ind, result in enumerate(ppvs):
        ax1.plot(prevalance, result,'o')
        ax2.plot(prevalance, npvs[ind])

        #plt.plot(prevalance, result)
    plt.legend(specificity, prop={'size': 16})
    #plt.xlabel('prevalance')
    #plt.ylabel('Predictive Value')

    ax1.set_xlabel('prevalance',size=20)
    ax1.set_ylim([0,1])
    ax2.set_ylim([0,1])
    ax1.set_ylabel('Positive Predictive Value ("o" marker)',size=20)
    ax2.set_ylabel('Negative Predictive Value (line marker)',size=20)
    ax2.tick_params(axis="y",labelsize=20)
    ax1.tick_params(axis="x",labelsize=20)
    ax1.tick_params(axis="y",labelsize=20)
    plt.title("NPV and PPV with Sensitivity of {}%".format(V),size=20)
    #plt.show
    fig.savefig("NPVandPPVwithSensitivityof{}%".format(V))
    plt.close(fig)



D = 1
V = 99
P = 99

Prevalance(D,V,P)
Prevalance(10,V,P)
Prevalance(30,V,P)
Prevalance(80,V,P)

Same_Sensitivity(D,V,P)
Same_Sensitivity(D,90,P)
Same_Sensitivity(D,80,P)
