import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html

#pip install dash-dangerously-set-inner-html


df = pd.read_csv('userAndEdge_trends_30days.csv')
edgesTrend = pd.read_csv('edgesTrend.csv')
communitiesNumberTrend = pd.read_csv('communitiesNumberTrend.csv')
communitiesDissolvedTrend = pd.read_csv('communitiesDissolvedTrend.csv')
communitiesCreationTrend = pd.read_csv('communitiesCreationTrend.csv')

averageDegreeAttack=pd.read_csv('AverageDegree/AttackGraphData.csv')
averageDegreeMessage=pd.read_csv('AverageDegree/MessageGraphData.csv')
averageDegreeTrade=pd.read_csv('AverageDegree/TradeGraphData.csv')

inDegreeDistribution=pd.read_csv('InDegreeDistribution/GraphData.csv')






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

      dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
       <center><img src="https://i.imgur.com/1WNmA0N.png" alt="slide 1" width="500"> </center>
        <center>See our <a href="https://github.com/Villone96/Data-Analytics-Project">GitHub Repo</a></center>

    '''),



    dcc.Tabs(id="tabs", children=[

        dcc.Tab(label='Introduzione', children=[
                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <center><img src="https://i.imgur.com/z1tFvav.png" alt="slide 1" width="1000"> </center>
    '''),
        ]),

        dcc.Tab(label='Il dataset', children=[
            #Codice
        ]),

        dcc.Tab(label='Obiettivi di Analisi', children=[
                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <h4>Le nostre analisi preventivate di analisi</h4>
        <ul>
        <li>Analisi numerosità  e numero medio di player.</li>
        <li>Analisi numerosità  e numero medio per ogni tipologia di arco. </li>
        <li>Cercare i nodi con outdegree (di qualsiasi tipo) uguale a 0 e indegree > 0 per gli attacchi (valutare anche altri possibili indegree); questo per identificare i villaggi abbandonati.</li>
        <li>Cercare i nodi con indegree (di qualsiasi tipo) uguale a 0 e outdegree > 0 per i trades (valutare che siano un unico outdegree); in questo modo si identificano quei villaggi che vengono utilizzati dallo stesso player (con nomi diversi) per rifornire il villaggio principale (valutare quindi che tutti gli archi siano in direzione di un solo player).</li>
        <li>Analisi delle community più grosse (top 3) nell'arco dei 30 giorni e determinare le cause.</li>
        <li>Ricerca della community che cresce (e decresce) di più (e di meno) nei 30 giorni. (Forse meglio valutare numerosità  nell'arco dei 30 giorni date tutte le community > 1)</li>
        <li>Valutare la edge betweenness date le community per ogni tipologia (attacco, commercio, messaggi); per i messaggi andiamo a identificare i capi diplomatici per ogni community.</li>
        <li>Valutare date le community più grosse la presenza di guerre (grande commercio e grande scambio di messaggi).</li>
        <li>Valutare l'evoluzione delle community in assenza di elementi centrali.</li>
        <li>Ricerca di nodi pozzo/sorgente per ogni tipo di relazioni e fare ipotesi sul perchè e per come.</li>
        <li>Fare confronto tra le diverse metodologie di community detection e valutare quale da risultati piÃÂ¹ simili a quelle fornite.</li>
        <li>Modifiche delle community in seguito agli attacchi.</li>
        <li></li>
        </ul>
    '''),
        ]),

        dcc.Tab(label='Trend nodi e archi', children=[
            html.P('La media degli utenti nei 30 giorni è di 2901'),
            dcc.Graph(
        id='life-exp-vs-gdp',
         figure={
            'data': [
                go.Scatter(
                    x=df[df['type'] == i]['day'],
                    y=df[df['type'] == i]['quantity'],
                    text=df[df['type'] == i]['type'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.type.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Giorni'},
                yaxis={'title': 'Quantità', 'type':'log'},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                #hovermode='closest'
            )
        }
    ),

    #GRafico a torta

    dcc.Graph(id="my-graph"),

    dcc.Slider(
        id='day-selected',
        min=1,
        max=30,
        step=1,
        value=15,
        marks={
            1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
            11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21',
            22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30'
    },
    ),
    html.Div(id='slider-output-container'),



        ]),
        dcc.Tab(label='Communities Trend', children=[
                    dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': communitiesNumberTrend.day, 'y': communitiesNumberTrend.quantity, 'type': 'bar', 'name': 'communities Number'},
                            {'x': communitiesDissolvedTrend.day, 'y': communitiesDissolvedTrend.quantity, 'type': 'bar', 'name': 'communities Dissolved'},
                            {'x': communitiesCreationTrend.day, 'y': communitiesCreationTrend.quantity, 'type': 'bar', 'name': 'communities Creation'},

                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Giorni'},
                            yaxis={'title': 'Quantità'},
                            #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            #legend={'x': 0, 'y': 1},
                            #hovermode='closest'
                        )
                    }
                ),
        ]),
        dcc.Tab(label='Average Degree', children=[
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': averageDegreeAttack.Day, 'y': averageDegreeAttack.AverageDegree,
                                'type': 'bar', 'name': 'Attack'},
                             {'x': averageDegreeMessage.Day, 'y': averageDegreeMessage.AverageDegree,
                                'type': 'bar', 'name': 'Message'},
                                 {'x': averageDegreeTrade.Day, 'y': averageDegreeTrade.AverageDegree,
                                'type': 'bar', 'name': 'TRade'},
                        ]
                    }
                )
        ]),
        dcc.Tab(label='In Degree Distribution', children=[
                dcc.Graph(id="DegreeDistributionGraph"),
                dcc.Slider(
                    id='day-selected2',
                    min=1,
                    max=30,
                    step=1,
                    value=15,
                    marks={
                        1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
                        11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21',
                        22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30'
                },
                ),
                html.Div(id='SelectionDegreeDistributionGraph'),



        ]),
    ])
])

@app.callback(
    dash.dependencies.Output("DegreeDistributionGraph", "figure"),
    [dash.dependencies.Input("day-selected2", "value")])
    
def update_output(day):
    
    return {
        'data': [
                go.Histogram(
                        print(d),

                        print(inDegreeDistribution[inDegreeDistribution['Type'] == d][inDegreeDistribution['Day'] == day]['Value']),
                        x=inDegreeDistribution[inDegreeDistribution['Day']==day]["Range"],
                        y=inDegreeDistribution[inDegreeDistribution['Type'] == d][inDegreeDistribution['Day'] == day]['Value'],
                        text=inDegreeDistribution[inDegreeDistribution['Type'] == d]['Type'],
                        #mode='markers',
                        opacity=0.7,
                        #marker={
                            #'size': 15,
                            #'line': {'width': 0.5, 'color': 'white'}
                        #},
                        name=d
                    )for d in inDegreeDistribution.Type.unique()],

            'layout': go.Layout(
                xaxis={'title': 'Giorni'},
                yaxis={'title': 'Quantità'},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                #hovermode='closest'
            )}

                            
@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("day-selected", "value")])

    
def update_output2(value):
    return {
        "data": [go.Pie(labels=edgesTrend["type"].unique().tolist(), values=edgesTrend[edgesTrend["day"] == value]["quantity"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B']}, textinfo='label')],
        "layout": go.Layout(title=f"Trend report daily", margin={"l": 200, "r": 200, },
                            legend={"x": 1, "y": 0.7})}

'''app.layout = html.Div(children=[

    html.H1(children='MPROG Analysis'),
    html.H4(children='User trend in 30 days'),
    html.P('IL trend degli utenti nei 30 giorni è tendenzialmende descrescente'),
    html.P('La media degli utenti nei 30 giorni è di 2901'),

    dcc.Markdown(),
    dcc.Graph(
        id='life-exp-vs-gdp',
         figure={
            'data': [
                go.Scatter(
                    x=df[df['type'] == i]['day'],
                    y=df[df['type'] == i]['quantity'],
                    text=df[df['type'] == i]['type'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.type.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Giorni'},
                yaxis={'title': 'Quantità', 'type':'log'},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                #hovermode='closest'
            )
        }
    ),



    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

])'''

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
# )

if __name__ == '__main__':
    app.run_server(debug=True)