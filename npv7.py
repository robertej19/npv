import plotly.graph_objects as go
import numpy as np


import plotly.graph_objects as go
import numpy as np



def PPV(V,D,P):
    ppv = V*D / (V*D + (100-D)*(100-P))
    #print(ppv)
    return ppv

def NPV(V,D,P):
    npv = P*(100-D) / (P*(100-D)+D*(100-V))
    return npv


def Prevalance(D,V,P):
    specificity = np.arange(1,99,1)
    sensitivity = np.arange(1,99,1)
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

    return sensitivity, specificity, ppvs, npvs

xx, yy, zz, W = Prevalance(12,99,99)




# Create figure
fig = go.Figure()

# Add traces, one for each slider step
V = .75
P = .8


fig = go.Figure(data=go.Scatter(
    x=[2,],
    y= [1, ],
    mode='markers',
    marker=dict(size=[200,],
                color=['blue', ], opacity=0),

    showlegend=False
))



for sense100 in np.arange(1, 100, 1):
    sense = sense100/100
    sick = 20
    scaler = 2
    healthy = 100 - sick
    numSickPos = round(sense*sick)
    numSickNeg = sick - numSickPos
    numHealthyPos = round((1-P)*healthy)
    numHealthyNeg = healthy - numHealthyPos

    print(numSickNeg)
    print(numSickPos)
    print(numHealthyNeg)
    print(numHealthyPos)
    #Total number of sick people


    fig.add_trace(go.Scatter(
        visible = False,
        x=[1.5, 2,2,2, 2.5],
        y=[1.5, 1,1,1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(numSickPos+numHealthyPos), scaler*100,
                    scaler*(100-numHealthyNeg),
                    scaler*(sick),
                    scaler*(numSickNeg+numHealthyNeg)],
                    color=['blue', 'green','blue','red','green']),
        name="Healthy"
    ))

    fig.add_trace(go.Scatter(
        visible = False,
        x=[1.5,2, 2.5],
        y=[1.5,1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(numSickPos), scaler*(numSickNeg), scaler*(numSickNeg)],
                    color=['red','yellow',  'yellow'], opacity = 1),
        name="Sick"
    ))






fig.update_yaxes(range=[0.5,2])
fig.update_xaxes(range=[1,3])




# Make 10th trace visible
#fig.data[0].visible = True
#fig.data[11].visible = True
#fig.data[12].visible = True
#fig.data[13].visible = True



# Create and add slider
steps = []
for j in range(int(int(len(fig.data)-1)/2)):
    i = j*2
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Disease Prevalence: " + str(j) + "%"}],  # layout attribute
    )
    step["args"][0]["visible"][0] = True
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i-1] = True
    #step["args"][0]["visible"][i-2] = True  # Toggle i'th trace to "visible"
    #step["args"][0]["visible"][i-3] = True
    #step["args"][0]["visible"][i-4] = True
    steps.append(step)
    #step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    #steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]



"""Need to fix this to display always the PPV and NPV"""
"""
fig.add_annotation(
        x=2,
        y=5,
        xref="x",
        yref="y",
        text="max=5",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )



"""
fig.update_layout(
    sliders=sliders
)


fig.show()
