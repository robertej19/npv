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
V = .8
P = .9

#Total number of people
fig.add_trace(go.Scatter(
    visible = True,
    x = np.arange(0,100,1),
    y = np.ones(100),
    mode='markers',
    marker=dict(
        size=16,
        color='black', #set color equal to a variable
        #colorscale='Viridis', # one of plotly colorscales
        #showscale=True
    ),
    name="Healthy"
))

for step in np.arange(0, 100, 1):
    x = np.arange(0,step,1)
    healthy = 100 - step

    #Total number of sick people
    fig.add_trace(go.Scatter(
        visible = False,
        x = x,
        y = np.ones(len(x)),
        mode='markers',
        marker=dict(
            size=16,
            color='red', #set color equal to a variable
            #colorscale='Viridis', # one of plotly colorscales
            #showscale=True
        ),
        name="Sick"
    ))

    numhavepos = round(V*step)
    x = np.arange(0,numhavepos,1)
    #Number of sick people testing positive
    fig.add_trace(go.Scatter(
        visible = False,
        x = x,
        y = 3*np.ones(len(x)),
        mode='markers',
        marker=dict(
            size=16,
            color='blue', #set color equal to a variable
            #colorscale='Viridis', # one of plotly colorscales
            #showscale=True
        ),
        name="Sick, Positive"
    ))

    x = np.arange(numhavepos,step,1)
    #Number of sick people testing negative
    fig.add_trace(go.Scatter(
        visible = False,
        x = x,
        y = 3*np.ones(len(x)),
        mode='markers',
        marker=dict(
            size=16,
            color='orange', #set color equal to a variable
            #colorscale='Viridis', # one of plotly colorscales
            #showscale=True
        ),
        name="Sick, Negative"
    ))

    numnohavepos = round((1-P)*healthy)
    x = np.arange(0,numnohavepos,1)
    #Number of sick people testing positive

    fig.add_trace(go.Scatter(
        visible = False,
        x = x,
        y = 2*np.ones(len(x)),
        mode='markers',
        marker=dict(
            size=16,
            color='purple', #set color equal to a variable
            #colorscale='Viridis', # one of plotly colorscales
            #showscale=True
        ),
        name="Healthy, Positive"
    ))


    healthy = 100 - step

    #print(healthy)
    x = np.arange(numnohavepos,healthy,1)
    #Number of sick people testing positive



    fig.add_trace(go.Scatter(
        visible = False,
        x = x,
        y = 2*np.ones(len(x)),
        mode='markers',
        marker=dict(
            size=16,
            color='yellow', #set color equal to a variable
            #colorscale='Viridis', # one of plotly colorscales
            #showscale=True
        ),
        name="Healthy, Negative"
    ))


fig.update_yaxes(range=[0,5])
fig.update_xaxes(range=[0,100])



# Make 10th trace visible
fig.data[0].visible = True
fig.data[11].visible = True
fig.data[12].visible = True
fig.data[13].visible = True



# Create and add slider
steps = []
for j in range(int(int(len(fig.data)-1)/5)):
    i = j*5
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Disease Prevalence: " + str(j) + "%"}],  # layout attribute
    )
    step["args"][0]["visible"][0] = True
    step["args"][0]["visible"][i-3] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i-2] = True
    step["args"][0]["visible"][i-1] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i-4] = True
    step["args"][0]["visible"][i-5] = True
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




fig.update_layout(
    sliders=sliders
)

fig.show()
