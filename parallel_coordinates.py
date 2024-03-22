import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

df = pd.read_excel('Agora_analysis.xlsx')

fig = go.Figure(data=
    go.Parcoords(
        #fig.update_traces(name=<VALUE>, selector=dict(type='parcoords'))
        name = "Agora",
        visible = True, 
        #labelfont= "Balto",

        line = dict(color = df['Total LCA'],
                   colorscale = 'Fall', #Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividis.
                   showscale = True,
                   cmin = -5,
                   cmax = 30),
        #fig.update_traces(dimensions=list(...), selector=dict(type='parcoords'))
        dimensions = list([
                 #constraintrange = [100000,150000],
            dict(tickvals = [1,2],
                 ticktext = ['Gas boiler','Wood boiler'],
                 label = 'Heating type', values = df['Heating system']),            
            dict(tickvals = [1,2,3,4,5,6,7],
                 ticktext = ['Wood fiber','Hempcrete', 'Hemp mat', 'Straw', 'EPS', 'Rockwool', 'Aerogel'],
                 label = 'Insulation type', values = df['Insulation option']),                  
            dict(range = [0, 700],
                 label = 'Insulation thickness', values = df['Thickness']),
            dict(tickvals = [1,2,3,4,5],
                 ticktext = ['Current','Wood, 2 pane (1.4)','Wood, 3 pane (1.1)','PVC, 3 pane (0.9)','PVC, 3 pane (0.8)'],
                 label = 'Window type', values = df['Window type']),
            dict(range = [-5,16],
                 #tickvals = [0,1,2,3],
                 label = 'Emb+repl CO2', values = df['Embodied LCA + replacement']),
            dict(range = [0,25],
                 label = 'Operational CO2', values = df['Operational LCA']),
            dict(range = [130, 760],
                 label = 'Inv + repl cost', values = df['Investment cost+replacement']), 
            dict(range = [90, 440],
                 label = 'Operational cost', values = df['Operational cost']),
            dict(range = [25, 105],
                 label = 'Heating demand', values = df['Heating demand'])])
    )
)
fig.update_layout(
    font = dict(
        family = "Balto, sans serif",
        size = 16,
        color = "#08003d"

    )
)

fig.write_html(r'P:\Agora\Parallel coordinates\Parallel_coordinated.html')#Add path to folder (X)
fig.write_image('P:\Agora\Parallel coordinates\agora.png')