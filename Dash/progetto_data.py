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
communitiesNumberTrend = pd.read_csv('communitiesNumberTrend.csv')
communitiesDissolvedTrend = pd.read_csv('communitiesDissolvedTrend.csv')
communitiesCreationTrend = pd.read_csv('communitiesCreationTrend.csv')






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
        <img src="https://i.imgur.com/z1tFvav.png" alt="slide 1" width="1700"> 
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
        dcc.Tab(label='Tab three', children=[
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [2, 4, 3],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [5, 4, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                )
        ]),
    ])
])

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