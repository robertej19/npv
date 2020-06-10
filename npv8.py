import plotly.graph_objects as go
import numpy as np
from plotly.graph_objects import *



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



for speci100 in np.arange(1, 100, 1):
    speci = speci100/100
    sense = 0.8
    sick = 20
    scaler = 2
    healthy = 100 - sick
    numSickPos = round(sense*sick)
    numSickNeg = sick - numSickPos
    numHealthyPos = round((1-speci)*healthy)
    numHealthyNeg = healthy - numHealthyPos

    #print(numSickNeg)
    #print(numSickPos)
    #print(numHealthyNeg)
    #print(numHealthyPos)
    #Total number of sick people

    fig.add_trace(go.Scatter(
        visible = False,
        x=[2, 2.3],
        y=[1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(100),
                    scaler*(numSickNeg+numHealthyNeg)],
                    color=['green','green']),
        name="Healthy, Negative",
        opacity=1
    ))

    fig.add_trace(go.Scatter(
        visible = False,
        x=[1.7, 2,2,2, 2.3],
        y=[1.5, 1,1,1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(numSickPos+numHealthyPos), scaler*(100-numHealthyNeg)],
                    color=['blue','blue']),
        name="Healthy, Positive",
        opacity=1
    ))


    fig.add_trace(go.Scatter(
        visible = False,
        x=[1.7, 2,2,2, 2.3],
        y=[1.5, 1,1,1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(numSickPos), scaler*(sick)],
                    color=['red','red']),
        name="Sick, Positive",
        opacity=1
    ))

    fig.add_trace(go.Scatter(
        visible = False,
        x=[2, 2.3],
        y=[1, 1.5],
        mode='markers',
        marker=dict(size=[scaler*(numSickNeg), scaler*(numSickNeg)],
                    color=['orange', 'orange'], opacity = 1),
        name="Sick, Negative",
        opacity=1
    ))





fig.update_yaxes({
    'range': [0.6, 1.9],
    'showgrid': False, # thin lines in the background
    'zeroline': False, # thick line at x=0
    'visible': False,  # numbers below
}) # the same for yaxis

fig.update_xaxes({
    'range': [1.4, 2.6],
    'showgrid': False, # thin lines in the background
    'zeroline': False, # thick line at x=0
    'visible': False,  # numbers below
}) # the same for yaxis


# Make 10th trace visible
#fig.data[0].visible = True
#fig.data[11].visible = True
#fig.data[12].visible = True
#fig.data[13].visible = True

fig.update_layout(title={'text':'Test Specificity: 40%'})

# Create and add slider
steps = []
for j in range(int(int(len(fig.data)-1)/4)):
    i = j*4
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Test specificity: " + str(j) + "%"}],  # layout attribute
              ()
    )
    step["args"][0]["visible"][0] = True
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i-1] = True
    step["args"][0]["visible"][i-2] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i-3] = True
    #step["args"][0]["visible"][i-4] = True
    steps.append(step)
    #step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    #steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "specificity: "},
    pad={"t": 50},
    steps=steps,
    tickcolor='white',
    font={'color': 'white'}
)]

fig.data[161].visible = True
fig.data[162].visible = True
fig.data[163].visible = True
fig.data[164].visible = True




"""Need to fix this to display always the PPV and NPV"""

fig.add_annotation(
        x=1.72,
        y=1.8,
        #xref="x",
        #yref="y",
        text="Test Positive",
        #showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="white"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="rgba(0,0,0,0)",
        #ax=20,
        #ay=-30,
        bordercolor="black",
        borderwidth=2,
        borderpad=4,
        bgcolor="Red",
        opacity=1
        )


fig.add_annotation(
        x=2.32,
        y=1.8,
        #xref="x",
        #yref="y",
        text="Test Negative",
        #showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="white"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="rgba(0,0,0,0)",
        #ax=20,
        #ay=-30,
        bordercolor="black",
        borderwidth=2,
        borderpad=4,
        bgcolor="blue",
        opacity=1
        )

fig.add_annotation(
        x=2.02,
        y=1.3,
        #xref="x",
        #yref="y",
        text="Total Population",
        #showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="white"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="rgba(0,0,0,0)",
        #ax=20,
        #ay=-30,
        bordercolor="black",
        borderwidth=2,
        borderpad=4,
        bgcolor="black",
        opacity=1
        )



layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


fig.update_layout({'paper_bgcolor':'rgba(0,0,0,0)', 'plot_bgcolor':'rgba(0,0,0,0)'})

fig.update_layout(
    sliders=sliders
)


fig.show()
