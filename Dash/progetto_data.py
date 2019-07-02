import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html

# pip install dash-dangerously-set-inner-html

df = pd.read_csv('userAndEdge_trends_30days.csv')
edgesTrend = pd.read_csv('edgesTrend.csv')
communitiesNumberTrend = pd.read_csv('communitiesNumberTrend.csv')
communitiesDissolvedTrend = pd.read_csv('communitiesDissolvedTrend.csv')
communitiesCreationTrend = pd.read_csv('communitiesCreationTrend.csv')

averageDegreeAttack = pd.read_csv('AverageDegree/AttackGraphData.csv')
averageDegreeMessage = pd.read_csv('AverageDegree/MessageGraphData.csv')
averageDegreeTrade = pd.read_csv('AverageDegree/TradeGraphData.csv')

inDegreeDistribution = pd.read_csv('InDegreeDistribution/GraphData.csv')
outDegreeDistribution = pd.read_csv('OutDegreeDistribution/GraphData.csv')

AverageShortestPathAttack = pd.read_csv(
    'AverageShortestPath/AttackGraphData.csv')
AverageShortestPathMessage = pd.read_csv(
    'AverageShortestPath/MessageGraphData.csv')
AverageShortestPathTrade = pd.read_csv(
    'AverageShortestPath/TradeGraphData.csv')

DensityM_NS = pd.read_csv('Density/DE_densityN_MData.csv')
DensityT_NS = pd.read_csv('Density/DE_densityN_TData.csv')

DensityM_S = pd.read_csv('Density/DE_densityS_MData.csv')
DensityT_S = pd.read_csv('Density/DE_densityS_TData.csv')

DiameterValueA = pd.read_csv('DiameterValue/AttackGraphData.csv')
DiameterValueM = pd.read_csv('DiameterValue/MessageGraphData.csv')
DiameterValueT = pd.read_csv('DiameterValue/TradeGraphData.csv')

ReciprocityM_S = pd.read_csv('Reciprocity/RE_reciprocityS_MData.csv')
ReciprocityT_S = pd.read_csv('Reciprocity/RE_reciprocityS_TData.csv')

ReciprocityM_NS = pd.read_csv('Reciprocity/RE_reciprocityN_MData.csv')
ReciprocityT_NS = pd.read_csv('Reciprocity/RE_reciprocityN_TData.csv')

Diplomatics = pd.read_csv(
    'SingleCommunityStudy/DiplomatsVsNoDiplomats/data.csv')

Trickster = pd.read_csv('TricksterDetection/tricksterActivityDay.csv', sep=';')
TricksterData = pd.read_csv('TricksterDetection/tricksterData.csv', sep=';')

InTotalDegreeD_T = pd.read_csv('InDegreeDistribution/TotalTradeData.csv')
InTotalDegreeD_M = pd.read_csv('InDegreeDistribution/TotalMessageData.csv')
InTotalDegreeD_A = pd.read_csv('InDegreeDistribution/TotalAttackData.csv')


OutTotalDegreeD_T = pd.read_csv('OutDegreeDistribution/TotalTradeData.csv')
OutTotalDegreeD_M = pd.read_csv('OutDegreeDistribution/TotalMessageData.csv')
OutTotalDegreeD_A = pd.read_csv('OutDegreeDistribution/TotalAttackData.csv')

# Coefficiente di clustering
CCoeffM_S = pd.read_csv(
    'ClusteringCoefficient/CC_clusteringS_MCoefficientData.csv')
CCoeffT_S = pd.read_csv(
    'ClusteringCoefficient/CC_clusteringS_TCoefficientData.csv')
CCoeffM_NS = pd.read_csv(
    'ClusteringCoefficient/CC_clusteringN_MCoefficientData.csv')
CCoeffT_NS = pd.read_csv(
    'ClusteringCoefficient/CC_clusteringN_TCoefficientData.csv')

# Numero di archi
ADM_S = pd.read_csv('EdgesInAllianceGraph/SameMessage_NEdges.csv')
ADT_S = pd.read_csv('EdgesInAllianceGraph/SameTrade_NEdges.csv')
ADM_NS = pd.read_csv('EdgesInAllianceGraph/NoSameMessage_NEdges.csv')
ADT_NS = pd.read_csv('EdgesInAllianceGraph/NoSameTrade_NEdges.csv')


# diametro
DM_S = pd.read_csv('AllianceGraph/D_diameterS_MData.csv')
DT_S = pd.read_csv('AllianceGraph/D_diameterS_TData.csv')
DM_NS = pd.read_csv('AllianceGraph/D_diameterN_MData.csv')
DT_NS = pd.read_csv('AllianceGraph/D_diameterN_TData.csv')

# Shortest Path
SPM_S = pd.read_csv('AllianceGraph/AP_averageS_MPathLengthData.csv', sep=';')
SPT_S = pd.read_csv('AllianceGraph/AP_averageS_TPathLengthData.csv', sep=';')
SPM_NS = pd.read_csv('AllianceGraph/AP_averageN_MPathLengthData.csv', sep=';')
SPT_NS = pd.read_csv('AllianceGraph/AP_averageN_TPathLengthData.csv', sep=';')

# averageDegree
ADegreeM_S = pd.read_csv('AllianceGraph/averageS_MDegree.csv')
ADegreeT_S = pd.read_csv('AllianceGraph/averageS_TDegree.csv')
ADegreeM_NS = pd.read_csv('AllianceGraph/averageN_MDegree.csv')
ADegreeT_NS = pd.read_csv('AllianceGraph/averageN_TDegree.csv')

# IN/OUT degree distr alliance graph
InDMD = pd.read_csv('AllianceGraph/inDegreeMean.csv')
OutDMD = pd.read_csv('AllianceGraph/outDegreeMean.csv')

# User e Edges trend in single comm
# IN/OUT degree distr alliance graph
SCS_edge = pd.read_csv('SingleCommunityStudy/CSVFILE/nEdgeTrend.csv')
SCS_user = pd.read_csv('SingleCommunityStudy/CSVFILE/nUserTrend.csv')

# Reciprocità sigola comm
RE_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/RE_reciprocityMData.csv')
RE_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/RE_reciprocityTData.csv')

# densità sigola comm
DE_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/DE_densityMData.csv')
DE_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/DE_densityTData.csv')

# Coeff di clustering sigola comm
CC_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/CC_clusteringMCoefficientData.csv')
CC_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/CC_clusteringTCoefficientData.csv')

# diametro sigola comm
DI_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/D_diameterMData.csv')
DI_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/D_diameterTData.csv')

# Shortest path sigola comm
SP_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/AP_averageMPathLengthData.csv', sep=';')
SP_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/AP_averageTPathLengthData.csv', sep=';')

# Grado medio Messaggi e trade
AD_SCS_M = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/averageMessageDegree.csv')
AD_SCS_T = pd.read_csv(
    'SingleCommunityStudy/StaticAnalysis/averageTradeDegree.csv')

# IN/OUT degree distr community single
InDMD_S = pd.read_csv('SingleCommunityStudy/StaticAnalysis/InDegreeMean.csv')
OutDMD_S = pd.read_csv('SingleCommunityStudy/StaticAnalysis/OutDegreeMean.csv')

# Dissolved Number
DN_Comm = pd.read_csv('DissolvedNumber/AboutAllPeriod.csv')

# Dissolved Community on Black Day
DN_Comm_Black = pd.read_csv('DissolvedNumber/BlackDayCommunityNumber.csv')

# Dissolved Community single user
DN_Comm_Single = pd.read_csv(
    'DissolvedNumber/AboutSinglePlayerCommunityAllPeriod.csv')

# Dissolved Community on Black Day single user
DN_Comm_Black_Single = pd.read_csv(
    'DissolvedNumber/BlackDaySingleInCommunity.csv')

# Activity Time
ActivityAttack = pd.read_csv('ActivityHour/Attack.csv')
ActivityMessage = pd.read_csv('ActivityHour/Message.csv')
ActivityTrade = pd.read_csv('ActivityHour/Trade.csv')
ActivityTotal = pd.read_csv('ActivityHour/Total.csv')

# Barbarian
Barbarian = pd.read_csv('Barbarian.csv')


available_indicators = Trickster['Suspect'].unique()
available_trickster = TricksterData['Suspect'].unique()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
       <center><img src='https://i.ibb.co/2tVxf15/image.png' alt="slide 1" width="300"> </center>
        <center>See our <a href="https://github.com/Villone96/Data-Analytics-Project">GitHub Repo</a></center>

    '''),



    dcc.Tabs(id="tabs", children=[

        dcc.Tab(label='Introduzione', children=[

            dcc.Tabs(id="introtabs", children=[
                dcc.Tab(label='Titolo', children=[
                    html.Div([], style={'height': 50}),

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                <center><img src="https://i.ibb.co/MMYYPLY/Schermata-2019-06-25-alle-10-18-53.png" alt="slide 1" width="1100"> </center>
                '''),


                ]),

                dcc.Tab(label='Giochi MMOG', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/LN2t4pc/capture-20190702155113895.png" alt="slide 1" width="1100"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/6m1PdLx/Schermata-2019-06-25-alle-10-20-22.png" alt="slide 1" width="1100"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/zQCPWdG/Schermata-2019-06-25-alle-10-28-11.png" alt="slide 1" width="1100"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/xmHPk8X/Schermata-2019-06-25-alle-10-30-10.png
        " alt="slide 1" width="1000"> </center>
            '''),

                ]),
                dcc.Tab(label='Il dataset', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/M2LJfHb/Schermata-2019-06-25-alle-10-32-55.png
        " alt="slide 1" width="1000"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/5WS96K5/Schermata-2019-06-25-alle-10-36-30.png
        " alt="slide 1" width="1000"> </center>
            '''),

                ]),
                dcc.Tab(label='Pre-Processing', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/M8DWpjS/capture-20190702155317347.png
        " alt="slide 1" width="1000"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/xgwKmcW/Schermata-2019-06-25-alle-10-38-09.png
        " alt="slide 1" width="1000"> </center>
            '''),

                ]),

                dcc.Tab(label='Obiettivi di Analisi', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/b53ygTS/Schermata-2019-06-25-alle-10-39-27.png
        " alt="slide 1" width="1000"> </center>
            '''),

                ]),

            ]),
        ]),
        dcc.Tab(label='La rete', children=[

            dcc.Tabs(id="retetab", children=[
                dcc.Tab(label='Trend Nodi e Archi', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/47cwJMM/Schermata-2019-06-25-alle-10-43-10.png
            " alt="slide 1" width="900"> </center>
            '''),

                    dcc.Graph(
                        id='life-exp-vs-gdp',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=df.day.unique(),
                                    y=df[df['type'] == 'nMessage'].quantity,
                                    name='Numero di messaggi',
                                    mode='markers+lines',
                                    opacity=0.7,
                                    line=dict(
                                        color=('rgb(76, 153, 0)'),
                                    ),
                                    marker={
                                        'size': 12,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },

                                ),
                                go.Scatter(
                                    x=df.day.unique(),
                                    y=df[df['type'] == 'nTrade'].quantity,
                                    name='Numero di commerci',
                                    mode='markers+lines',
                                    opacity=0.7,
                                    line=dict(
                                        color=('rgb(255, 170, 102)'),
                                    ),
                                    marker={
                                        'size': 12,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },
                                ),
                                go.Scatter(
                                    x=df.day.unique(),
                                    y=df[df['type'] == 'nAttack'].quantity,
                                    name='Numero di attacchi',
                                    mode='markers+lines',
                                    opacity=0.7,
                                    line=dict(
                                        color=('rgb(255, 0, 0)'),
                                    ),
                                    marker={
                                        'size': 12,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },
                                ),
                                go.Scatter(
                                    x=df.day.unique(),
                                    y=df[df['type'] == 'nUsers'].quantity,
                                    name='Numero di Utenti',
                                    mode='markers+lines',
                                    opacity=0.7,
                                    line=dict(
                                        color=('rgb(31, 119, 180)'),
                                    ),
                                    marker={
                                        'size': 12,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },
                                ),

                                go.Scatter(
                                    x=Barbarian.day.unique(),
                                    y=Barbarian.nBarbaria,
                                    name='Numero di Barbari',
                                    mode='markers+lines',
                                    opacity=0.7,
                                    line=dict(
                                        color=('rgb(228, 81, 255)'),
                                    ),
                                    marker={
                                        'size': 12,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },
                                ),

                            ],

                            'layout': go.Layout(
                                xaxis={'title': 'Giorni'},
                                yaxis={'title': 'Quantità', 'type': 'log'},
                                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                # legend={'x': 0, 'y': 1},+
                                # hovermode='closest'
                            )
                        }
                    ),

                    # GRafico a torta

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

                dcc.Tab(label='Tempo di Attività', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/NjWB7Qh/Schermata-2019-06-25-alle-10-47-55.png
            " alt="slide 1" width="900"> </center>
            '''),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x=ActivityTotal.Hour,
                                    y=ActivityTotal.NumberOfEdges,
                                    mode='markers+lines',
                                    name='Attività totali',
                                ),
                                go.Scatter(
                                    x=ActivityAttack.Hour,
                                    y=ActivityAttack.NumberOfEdges,
                                    mode='markers+lines',
                                    name='Attività di Attacco',
                                    line=dict(
                                        color=('rgb(255, 0, 0)'),
                                    ),
                                ),
                                go.Scatter(
                                    x=ActivityMessage.Hour,
                                    y=ActivityMessage.NumberOfEdges,
                                    mode='lines+markers',
                                    name='Attività di Messaggi',
                                    line=dict(
                                        color=('rgb(76, 153, 0)'),
                                    ),
                                ),
                                go.Scatter(
                                    x=ActivityTrade.Hour,
                                    y=ActivityTrade.NumberOfEdges,
                                    mode='lines+markers',
                                    name='Attività di Commercio',
                                    line=dict(
                                        color=('rgb(255, 170, 102)'),
                                    ),
                                ),

                            ],
                            layout=go.Layout(
                                title='Attività per tipo di arco',
                                xaxis={'title': 'Orario',
                                       'tickmode': 'linear'},
                                yaxis={'title': 'N. Attività', 'type': 'log'},
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='activityHours'
                    ),


                ]),

                dcc.Tab(label='Communities Trend', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/4tG8396/Schermata-2019-06-25-alle-10-48-31.png" alt="slide 1" width="1100"> </center>
            '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/CvVZ72R/Schermata-2019-06-25-alle-10-53-40.png" alt="slide 1" width="1100"> </center>
            '''),
                    html.Div([

                        dcc.Graph(
                             figure=go.Figure(
                              data=[
                                  go.Scatter(
                                      x=communitiesNumberTrend.day,
                                      y=communitiesNumberTrend.quantity,
                                      mode='markers+lines',
                                      name='Numero di Comunità',
                                  ),
                                  go.Scatter(
                                      x=communitiesDissolvedTrend.day,
                                      y=communitiesDissolvedTrend.quantity,
                                      mode='lines+markers',
                                      name='Comunità dissolte'
                                  ),
                                  go.Scatter(
                                      x=communitiesCreationTrend.day,
                                      y=communitiesCreationTrend.quantity,
                                      mode='lines+markers',
                                      name='Comunità Create'
                                  ),

                              ],
                                 layout=go.Layout(
                                  title='Communities Trends',
                                  showlegend=True,
                                  legend=go.layout.Legend(
                                      x=0,
                                      y=1.0
                                  ),
                                  margin=go.layout.Margin(
                                      l=40, r=0, t=40, b=30)
                              )
                             ),
                             style={'height': 300},
                             id='commtrend'
                             ), ]),


                    html.Div([
                        html.Div([

                             dcc.Graph(
                                 figure=go.Figure(
                                     data=[
                                         go.Pie(labels=DN_Comm.PeopleIn, values=DN_Comm.NCommunity,
                                                hoverinfo='label+percent', textinfo='label',
                                                marker={'colors': [
                                                    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']},
                                                )


                                     ],
                                     layout=go.Layout(
                                         title='Numero di utenti delle 127 community dissolte nei 30 giorni',
                                         showlegend=True,
                                         legend=go.layout.Legend(
                                             x=0,
                                             y=1.0
                                         ),
                                         margin=go.layout.Margin(
                                             l=40, r=0, t=40, b=30)
                                     )
                                 ),
                                 style={'height': 300},
                                 id='commdissolvedtrend1'
                             ),
                             ], className="six columns"),

                        html.Div([

                            dcc.Graph(
                                 figure=go.Figure(
                                     data=[
                                         go.Pie(
                                             labels=DN_Comm_Single.Type, values=DN_Comm_Single.Number,
                                             hoverinfo='label+percent', textinfo='label',
                                             marker={'colors': [
                                                 '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']},
                                         )


                                     ],
                                     layout=go.Layout(
                                         title='Anzianità utenti delle community dissolte nei 30 giorni',
                                         showlegend=True,
                                         legend=go.layout.Legend(
                                             x=0,
                                             y=1.0
                                         ),
                                         margin=go.layout.Margin(
                                             l=40, r=0, t=40, b=30)
                                     )
                                 ),
                                 style={'height': 300},
                                 id='singleAllPeriod1'
                                 ),
                        ], className="six columns"),
                    ], className="row"),

                    html.Div([
                        html.Div([

                             dcc.Graph(
                                 figure=go.Figure(
                                     data=[
                                         go.Pie(labels=DN_Comm_Black.PeopleIn, values=DN_Comm_Black.NCommunity,
                                                hoverinfo='label+percent', textinfo='label',
                                                marker={'colors': [
                                                    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']},
                                                )


                                     ],
                                     layout=go.Layout(
                                         title='Numero di utenti delle 24 community dissolte nel Giorno peggiore',
                                         showlegend=True,
                                         legend=go.layout.Legend(
                                             x=0,
                                             y=1.0
                                         ),
                                         margin=go.layout.Margin(
                                             l=40, r=0, t=40, b=30)
                                     )
                                 ),
                                 style={'height': 300},
                                 id='commdissolvedonblacktrend'
                             ),
                             ], className="six columns"),

                        html.Div([

                            dcc.Graph(
                                 figure=go.Figure(
                                     data=[
                                         go.Pie(labels=DN_Comm_Black_Single.Type, values=DN_Comm_Black_Single.Number,
                                                hoverinfo='label+percent', textinfo='label',
                                                marker={'colors': [
                                                    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']},
                                                )


                                     ],
                                     layout=go.Layout(
                                         title='Anzianità degli utenti delle 24 community dissolte nel Giorno peggiore',
                                         showlegend=True,
                                         legend=go.layout.Legend(
                                             x=0,
                                             y=1.0
                                         ),
                                         margin=go.layout.Margin(
                                             l=40, r=0, t=40, b=30)
                                     )
                                 ),
                                 style={'height': 300},
                                 id='singleblacktrend'
                                 ),
                        ], className="six columns"),
                    ], className="row"),




                ]),
                dcc.Tab(label='Average Degree and Degree Distribution', children=[
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/ts0HSjb/capture-20190628143801106.png" alt="slide 1" width="1150"> </center>
            '''),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x=averageDegreeAttack.Day,
                                    y=averageDegreeAttack.AverageDegree,
                                    mode='markers+lines',
                                    name='Grado medio Attacchi',
                                    line=dict(
                                        color=('rgb(255, 0, 0)'),
                                    ),


                                ),
                                go.Scatter(
                                    x=averageDegreeMessage.Day,
                                    y=averageDegreeMessage.AverageDegree,
                                    mode='lines+markers',
                                    name='Grado medio Messaggi',
                                    line=dict(
                                        color=('rgb(76, 153, 0)'),
                                    ),
                                ),
                                go.Scatter(
                                    x=averageDegreeTrade.Day,
                                    y=averageDegreeTrade.AverageDegree,
                                    mode='lines+markers',
                                    name='Grado medio Commercio',
                                    line=dict(
                                        color=('rgb(255, 170, 102)'),
                                    ),
                                ),

                            ],
                            layout=go.Layout(
                                title='Grado medio per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageDedree'
                    ),
                    html.Hr(),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/mhZ65Dn/capture-20190628143849434.png" alt="slide 1" width="1150"> </center>
            '''),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=InTotalDegreeD_T.Range,
                                    y=InTotalDegreeD_T.Value,
                                    name='In Degree medio Commercio',
                                    marker=dict(
                                        color=('rgb(255, 170, 102) '),
                                    ),


                                ),
                                go.Bar(
                                    x=InTotalDegreeD_M.Range,
                                    y=InTotalDegreeD_M.Value,
                                    name='In Degree medio Messaggi',
                                    marker=dict(
                                        color=(' rgb(76, 153, 0) '),
                                    ),



                                ),

                                go.Bar(
                                    x=InTotalDegreeD_A.Range,
                                    y=InTotalDegreeD_A.Value,
                                    name='In Degree medio Attacchi',
                                    marker=dict(
                                        color=('rgb(255, 0, 0) '),
                                    ),


                                ),


                            ],
                            layout=go.Layout(
                                title='In Degree medio Messaggi, Commercio ed Attacchi',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageInDegreeAMT'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=OutTotalDegreeD_T.Range,
                                    y=OutTotalDegreeD_T.Value,
                                    name='Out Degree medio Commercio',
                                    marker=dict(
                                        color=('rgb(255, 170, 102) '),
                                    ),


                                ),
                                go.Bar(
                                    x=OutTotalDegreeD_M.Range,
                                    y=OutTotalDegreeD_M.Value,
                                    name='Out Degree medio Messaggi',
                                    marker=dict(
                                        color=(' rgb(76, 153, 0) '),
                                    ),


                                ),

                                go.Bar(
                                    x=OutTotalDegreeD_A.Range,
                                    y=OutTotalDegreeD_A.Value,
                                    name='Out Degree medio Attacchi',
                                    marker=dict(
                                        color=('rgb(255, 0, 0) '),
                                    ),


                                ),


                            ],
                            layout=go.Layout(
                                title='Out Degree medio Messaggi, Commercio ed Attacchi',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageOutDegreeAMT'
                    ),

                    html.Div([], style={'height': 150},),




                ]),
                dcc.Tab(label='In/Out Degree Distribution sul periodo', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/K5yvSrt/capture-20190702155531467.png" alt="slide 1" width="1150"> </center>
            '''),

                    dcc.Graph(id="InDegreeDistributionGraph"),
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
                    html.Hr(),

                    dcc.Graph(id="OutDegreeDistributionGraph"),
                    dcc.Slider(
                        id='day-selected3',
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
                dcc.Tab(label='Average Shortest Path e Diametro', children=[
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/2YLLRzL/image.png" alt="slide 1" width="1100"> </center>
            '''),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x=AverageShortestPathAttack.Day,
                                    y=AverageShortestPathAttack.AverageShortestPath,
                                    mode='markers+lines',
                                    name='SP medio Attacchi',
                                    line=dict(
                                        color=('rgb(255, 0, 0)'),
                                    ),


                                ),
                                go.Scatter(
                                    x=AverageShortestPathMessage.Day,
                                    y=AverageShortestPathMessage.AverageShortestPath,
                                    mode='lines+markers',
                                    name='SP medio Messaggi',
                                    line=dict(
                                        color=('rgb(76, 153, 0)'),
                                    ),
                                ),
                                go.Scatter(
                                    x=AverageShortestPathTrade.Day,
                                    y=AverageShortestPathTrade.AverageShortestPath,
                                    mode='lines+markers',
                                    name='SP medio Commercio',
                                    line=dict(
                                        color=('rgb(255, 170, 102)'),
                                    ),
                                ),

                            ],
                            layout=go.Layout(
                                title='Shortest Path medio per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageSHP'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x=DiameterValueA.Day,
                                    y=DiameterValueA.Diameter,
                                    mode='markers+lines',
                                    name='Diametro Attacchi',
                                    line=dict(
                                        color=('rgb(255, 0, 0)'),
                                    ),

                                ),
                                go.Scatter(
                                    x=DiameterValueM.Day,
                                    y=DiameterValueM.Diameter,
                                    mode='lines+markers',
                                    name='Diametro Messaggi',
                                    line=dict(
                                        color=('rgb(76, 153, 0)'),
                                    ),
                                ),
                                go.Scatter(
                                    x=DiameterValueT.Day,
                                    y=DiameterValueT.Diameter,
                                    mode='lines+markers',
                                    name='Diametro Commercio',
                                    line=dict(
                                        color=('rgb(255, 170, 102)'),
                                    ),
                                ),

                            ],
                            layout=go.Layout(
                                title='Diametro per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageDiameter'
                    ),


                ]),


            ]),
        ]),

        dcc.Tab(label='Trickster Detection', children=[

                dcc.Tabs(id="Trickster tabs", children=[
                    dcc.Tab(label='Introduzione', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/q0x9ZwB/Schermata-2019-06-25-alle-11-03-43.png
            " alt="slide 1" width="1150"> </center>
            '''),

                    ]),

                    dcc.Tab(label='Logica di funzionamento', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/30f2p9j/Schermata-2019-06-25-alle-11-07-39.png
            " alt="slide 1" width="1000"> </center>'''),

                    ]),

                    dcc.Tab(label='Risultati', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/nCQjHY5/Schermata-2019-06-25-alle-11-11-22.png
            " alt="slide 1" width="1000"> </center>'''),


                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                            '''<br><h4>Seleziona il cheater:</h4>'''),
                        html.Div([  # menu per selezionare il cheater
                            dcc.Dropdown(
                                id='suspect-column',
                                options=[{'label': i, 'value': i}
                                         for i in available_indicators],
                                value=7855
                            ),

                        ]
                            #style={'width': '15%', 'float': 'right', 'display': 'inline-block'}
                        ),
                        html.Hr(),
                        html.H4(id='index'),
                        dcc.Graph(id='cheat-graphic'),  # grafico

                        # Secondo plot -----------------------------------------------------------------------------

                        #dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<br><h4>Seleziona il cheater:</h4>'''),
                        # html.Div([                      #menu per selezionare il cheater
                        # dcc.Dropdown(
                        # id='suspect-column',
                        #options=[{'label': i, 'value': i} for i in available_trickster],
                        # value=7855
                        #  ),

                        # ]
                        #style={'width': '15%', 'float': 'right', 'display': 'inline-block'}
                        # )

                        html.Div([
                            html.Div([

                                dcc.Graph(id='cheat-data-in'),  # grafico
                            ], className="six columns"),

                            html.Div([

                                dcc.Graph(id='cheat-data-out'),  # grafico
                            ], className="six columns"),
                        ], className="row"),
                        html.H5(id='to', style={
                            'textAlign': 'center',
                        }),
                        html.H5(id='from', style={
                            'textAlign': 'center',
                        }),


                        # dcc.Graph(id='cheat-data'), #grafico

                    ]),

                ]),
                ]),

        dcc.Tab(label='Commercio e Messaggi', children=[
                dcc.Tabs(id="commerciotradetabs", children=[

                    dcc.Tab(label='Introduzione', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/3smtRMG/Schermata-2019-06-25-alle-11-12-48.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                         ]),

                    dcc.Tab(label='Reciprocità', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/khhSBqD/Schermata-2019-06-25-alle-11-17-16.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ReciprocityM_S.day,
                                        y=ReciprocityM_S.Reciprocity,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ReciprocityM_NS.day,
                                        y=ReciprocityM_NS.Reciprocity,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto Reciprocità Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messagereciprocity'
                        ),



                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/cw7nnFT/Schermata-2019-06-25-alle-11-17-48.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ReciprocityT_S.day,
                                        y=ReciprocityT_S.Reciprocity,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ReciprocityT_NS.day,
                                        y=ReciprocityT_NS.Reciprocity,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto Reciprocità Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='Tradesreciprocity'
                        ),

                    ]),

                    dcc.Tab(label='Densità', children=[
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/9yCGvvC/Schermata-2019-06-26-alle-12-29-24.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=DensityM_S.day,
                                        y=DensityM_S.density,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=DensityM_NS.day,
                                        y=DensityM_NS.density,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto Densità Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messagedensity'
                        ),



                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/N267wXQ/Schermata-2019-06-25-alle-11-26-29.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=DensityT_S.day,
                                        y=DensityT_S.density,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=DensityT_NS.day,
                                        y=DensityT_NS.density,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),
                                ],
                                layout=go.Layout(
                                    title='Confronto Densità Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tardesdensity'
                        ),


                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/G3tvbgk/Schermata-2019-06-26-alle-12-31-09.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ADM_S.day,
                                        y=ADM_S.TotalWeight,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ADM_NS.day,
                                        y=ADM_NS.TotalWeight,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto numero di archi Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messaggena'
                        ),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ADT_S.day,
                                        y=ADT_S.TotalWeight,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ADT_NS.day,
                                        y=ADT_NS.TotalWeight,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto numero di archi di Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradena'
                        ),

                    ]),

                    dcc.Tab(label='Clustering Coefficient', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/M9yZJ1n/Schermata-2019-06-26-alle-12-29-46.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=CCoeffM_S.day,
                                        y=CCoeffM_S.clusteringCoefficient,
                                        mode='markers+lines',
                                        line=dict(
                                            color=('rgb(76, 153, 0)'),
                                        ),
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=CCoeffT_S.day,
                                        y=CCoeffT_S.clusteringCoefficient,
                                        mode='markers+lines',
                                        line=dict(
                                            color=('rgb(255, 170, 102)'),
                                        ),
                                        name='Commercio intra comunità',
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto coefficiente di clustering Messaggi e Commercio dentro la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messaggeCoeff'
                        ),


                    ]),
                    dcc.Tab(label='Diametro e Average Shortest', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/82j0Bsz/Schermata-2019-06-26-alle-12-31-45.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=DM_S.day,
                                        y=DM_S.diameter,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=DM_NS.day,
                                        y=DM_NS.diameter,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto diametro Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messaggediam'
                        ),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=DT_S.day,
                                        y=DT_S.diameter,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=DT_NS.day,
                                        y=DT_NS.diameter,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto diametro Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradediam'
                        ),

                        # SHORTEST PATH
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/7SSLCDh/Schermata-2019-06-26-alle-12-32-35.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=SPM_S.day,
                                        y=SPM_S.averagePathLength,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=SPM_NS.day,
                                        y=SPM_NS.averagePathLength,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto shortest path medio Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messaggesp'
                        ),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=SPT_S.day,
                                        y=SPT_S.averagePathLength,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=SPT_NS.day,
                                        y=SPT_NS.averagePathLength,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto shortest path medio Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradesp'
                        ),

                    ]),

                    # AVERAGE DEGREE
                    dcc.Tab(label='Average Degree & In/Out Degree', children=[
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/tpNLWD5/capture-20190628142526309.png
                    " alt="slide 1" width="1100"> </center>
                    '''),



                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ADegreeM_S.day,
                                        y=ADegreeM_S.averageDegree,
                                        mode='markers+lines',
                                        name='Messaggi intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ADegreeM_NS.day,
                                        y=ADegreeM_NS.averageDegree,
                                        mode='lines+markers',
                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto grado medio Messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),
                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messaggeadegree'
                        ),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=ADegreeT_S.day,
                                        y=ADegreeT_S.averageDegree,
                                        mode='markers+lines',
                                        name='Commercio intra comunità',


                                    ),
                                    go.Scatter(
                                        x=ADegreeT_NS.day,
                                        y=ADegreeT_NS.averageDegree,
                                        mode='lines+markers',
                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto grado medio Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradeadegree'
                        ),
                        # TRADE IN DEGREE DISTR


                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/X549z8y/capture-20190628142706778.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=InDMD.range.unique(),
                                        y=InDMD[InDMD['type'] == 'S_T'].value,

                                        name='Commercio intra comunità',


                                    ),
                                    go.Bar(
                                        x=InDMD.range.unique(),
                                        y=InDMD[InDMD['type'] == 'N_T'].value,

                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto in degree distribution dei Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradeInDegree'
                        ),

                        # TRADE OUT DEGREE DISTR

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=OutDMD.range.unique(),
                                        y=OutDMD[OutDMD['type']
                                                 == 'S_T'].value,

                                        name='Commercio intra comunità',


                                    ),
                                    go.Bar(
                                        x=OutDMD.range.unique(),
                                        y=OutDMD[OutDMD['type']
                                                 == 'N_T'].value,

                                        name='Commercio extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto out degree distribution dei Commercio dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='tradeOutDegree'
                        ),
                        html.Hr(),

                        # MESSAGE IN DEGREE DISTR


                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/bX0FcR1/capture-20190628142824687.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=InDMD.range.unique(),
                                        y=InDMD[InDMD['type'] == 'S_M'].value,

                                        name='Messaggi intra comunità',


                                    ),
                                    go.Bar(
                                        x=InDMD.range.unique(),
                                        y=InDMD[InDMD['type'] == 'N_M'].value,

                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto in degree distribution dei messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messageInDegree'
                        ),



                        # MESSAGE OUT DEGREE DISTR
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=OutDMD.range.unique(),
                                        y=OutDMD[OutDMD['type']
                                                 == 'S_M'].value,

                                        name='Messaggi intra comunità',


                                    ),
                                    go.Bar(
                                        x=OutDMD.range.unique(),
                                        y=OutDMD[OutDMD['type']
                                                 == 'N_M'].value,

                                        name='Messaggi extra comunità'
                                    ),


                                ],
                                layout=go.Layout(
                                    title='Confronto out degree distribution dei messaggi dentro e fuori la Comunità',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0
                                    ),

                                    margin=go.layout.Margin(
                                        l=40, r=0, t=40, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='messageOutDegree'
                        ),


                    ]),

                ]),
                ]),


        dcc.Tab(label='Studio Singola Community', children=[
            dcc.Tabs(id="communitystudytabs", children=[
                     dcc.Tab(label='Introduzione', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/bmQ4QF6/Schermata-2019-06-26-alle-12-33-03.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                     ]),


                     dcc.Tab(label='User and Edge Trend', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/pxnRwWm/Schermata-2019-06-27-alle-19-02-19.png
            " alt="slide 1" width="1150"> </center>
            '''),

                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                   go.Scatter(
                                       x=SCS_user.day,
                                       y=SCS_user.totalSign,
                                       mode='lines+markers',
                                       name='Utenti segnati',


                                   ),
                                     go.Scatter(
                                       x=SCS_user.day,
                                       y=SCS_user.presentInNet,
                                       mode='lines+markers',
                                       name='Utenti attivi nella rete'
                                   ),
                                     go.Scatter(
                                       x=SCS_user.day,
                                       y=SCS_user.activeInCommunity,
                                       mode='lines+markers',
                                       name='Utenti attivi nella community'
                                   ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto tra utenti teorici ed attivi per ogni giorno della community',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),

                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='usertrendcomm'
                         ),

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/8z66q74/Schermata-2019-06-27-alle-19-02-59.png
            " alt="slide 1" width="1150"> </center>
            '''),
                         # numero MESSAGE e trade
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=SCS_edge.day.unique(),
                                         y=SCS_edge[SCS_edge['type']
                                                    == 'nMessage'].quantity,
                                         mode='lines+markers',
                                         name='Numero di messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),



                                     ),
                                     go.Scatter(
                                         x=SCS_edge.day.unique(),
                                         y=SCS_edge[SCS_edge['type']
                                                    == 'nTrade'].quantity,
                                         mode='lines+markers',
                                         name='Numero di Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto tra numero di messaggi e numero di Commercio nella community',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),

                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradecomm'
                         ),


                     ]),

                     dcc.Tab(label='Analisi Strutturale 1', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/Ptpy6hd/Schermata-2019-06-27-alle-19-03-24.png
            " alt="slide 1" width="1150"> </center>
            '''),

                         # reciprocità messaggi e trade
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=RE_SCS_M.day,
                                         y=RE_SCS_M.Diameter,
                                         mode='markers+lines',
                                         name='reciprocità messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),


                                     ),
                                     go.Scatter(
                                         x=RE_SCS_T.day,
                                         y=RE_SCS_T.Diameter,
                                         mode='lines+markers',
                                         name='Reciprocità Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto Reciprocità Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradereciprocitycomm'
                         ),

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/DKq9ckn/Schermata-2019-06-27-alle-19-04-14.png
            " alt="slide 1" width="1150"> </center>
            '''),
                         # densità messaggi e trade
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=DE_SCS_M.day,
                                         y=DE_SCS_M.density,
                                         mode='markers+lines',
                                         name='Densità messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),


                                     ),
                                     go.Scatter(
                                         x=DE_SCS_T.day,
                                         y=DE_SCS_T.density,
                                         mode='lines+markers',
                                         name='Densità Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto densità media Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradedensitycomm'
                         ),

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/yyQHnB1/capture-20190628143525258.png
            " alt="slide 1" width="1150"> </center>
            '''),

                         # coeff di clustering messaggi e trade
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=CC_SCS_M.day,
                                         y=CC_SCS_M.clusteringCoefficient,
                                         mode='markers+lines',
                                         name='Coeff. di clustering messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),



                                     ),
                                     go.Scatter(
                                         x=CC_SCS_T.day,
                                         y=CC_SCS_T.clusteringCoefficient,
                                         mode='lines+markers',
                                         name='Coeff. di clustering Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto Coeff. di clustering medio Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradeCCcomm'
                         ),

                     ]),

                     dcc.Tab(label='Analisi Strutturale 2', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/7XjHBSJ/Schermata-2019-06-27-alle-19-04-36.png
            " alt="slide 1" width="1150"> </center>
            '''),
                         # Diametro
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                   go.Scatter(
                                       x=DI_SCS_M.day,
                                       y=DI_SCS_M.diameter,
                                       mode='markers+lines',
                                       name='Diametro messaggi',
                                       line=dict(
                                           color=('rgb(76, 153, 0)'),
                                       ),


                                   ),
                                     go.Scatter(
                                       x=DI_SCS_T.day,
                                       y=DI_SCS_T.diameter,
                                       mode='lines+markers',
                                       name='Diametro Commercio',
                                       line=dict(
                                           color=('rgb(255, 170, 102)'),
                                       ),
                                   ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto diametro medio Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradediametercomm'
                         ),

                         # Shortest path
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=SP_SCS_M.day,
                                         y=SP_SCS_M.averagePathLength,
                                         mode='markers+lines',
                                         name='Shortest Path messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),


                                     ),
                                     go.Scatter(
                                         x=SP_SCS_T.day,
                                         y=SP_SCS_T.averagePathLength,
                                         mode='lines+markers',
                                         name='Shortest Path Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Shortest Path medio di clustering Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtradeSPcomm'
                         ),
                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/TtSkzRH/capture-20190628145334914.png
            " alt="slide 1" width="1150"> </center>
            '''),


                         # Grado medio
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Scatter(
                                         x=AD_SCS_M.day,
                                         y=AD_SCS_M.averageDegree,
                                         mode='markers+lines',
                                         name='Grado medio Messaggi',
                                         line=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),


                                     ),
                                     go.Scatter(
                                         x=AD_SCS_T.day,
                                         y=AD_SCS_T.averageDegree,
                                         mode='lines+markers',
                                         name='Grado medio Commercio',
                                         line=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Grado medio Messaggi e Commercio nella Comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),
                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='messageandtrademeandegreecomm'
                         ),

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/syRc5HX/Schermata-2019-06-27-alle-19-04-59.png
            " alt="slide 1" width="1150"> </center>
            '''),
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Bar(
                                         x=InDMD_S.range.unique(),
                                         y=InDMD_S[InDMD_S['type']
                                                   == 'Message'].value,
                                         marker=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),

                                         name='Messaggi',


                                     ),
                                     go.Bar(
                                         x=InDMD_S.range.unique(),
                                         y=InDMD_S[InDMD_S['type']
                                                   == 'Trade'].value,
                                         marker=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),

                                         name='Commercio'
                                     ),

                                 ],
                                 layout=go.Layout(
                                     title='Confronto IN Degree distribution di Messaggi, Commercio ed entrambi dentro la comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),

                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='MeanINDegreeSingle'
                         ),
                         dcc.Graph(
                             figure=go.Figure(
                                 data=[
                                     go.Bar(
                                         x=OutDMD_S.range.unique(),
                                         y=OutDMD_S[OutDMD_S['type']
                                                    == 'Message'].value,
                                         marker=dict(
                                             color=('rgb(76, 153, 0)'),
                                         ),

                                         name='Messaggi',


                                     ),
                                     go.Bar(
                                         x=OutDMD_S.range.unique(),
                                         y=OutDMD_S[OutDMD_S['type']
                                                    == 'Trade'].value,
                                         marker=dict(
                                             color=('rgb(255, 170, 102)'),
                                         ),

                                         name='Commercio'
                                     ),


                                 ],
                                 layout=go.Layout(
                                     title='Confronto Out Degree distribution di Messaggi, Commercio ed entrambi dentro la comunità',
                                     showlegend=True,
                                     legend=go.layout.Legend(
                                         x=0,
                                         y=1.0
                                     ),

                                     margin=go.layout.Margin(
                                         l=40, r=0, t=40, b=30)
                                 )
                             ),
                             style={'height': 300},
                             id='MeanOUTDegreeSingle'
                         ),

                     ]),



                     dcc.Tab(label='Leader', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/jhyNfmk/Ricerca-Leader.png
            " alt="slide 1" width="1150"> </center>
            '''),
                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/P6qVw5D/image.png
            " alt="slide 1" width="1150"> </center>
            '''),


                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
           <center><iframe width="1000" height="930" src="//www.cincopa.com/media-platform/iframe.aspx?fid=AQCA4j-SyJr1" frameborder="0" allowfullscreen scrolling="no"></iframe></center>
    '''),







                     ]),
                     dcc.Tab(label='Relazioni con i diplomatici', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/n8q1KNC/capture-20190628141656963.png
            " alt="slide 1" width="1150"> </center>
            '''),

                         dcc.Graph(
                             id='DiplomaticiNotDiplomatici',
                             figure={
                                 'data': [
                                     {'x': 'Diplomatici', 'y': Diplomatics.DiplomatsLeaderMessage,
                                      'type': 'bar', 'name': 'Messaggi Diplomatici'},
                                     {'x': 'Non Diplomatici', 'y': Diplomatics.NormalUserLeaderMessage,
                                      'type': 'bar', 'name': 'Messaggi utenti comuni'}, ],
                                 'layout': {
                                     'title': 'Confronto tra media messaggi di diplomatici e utenti comuni'
                                 }
                             }
                         ),


                     ]),
                     dcc.Tab(label='Eliminazione del leader', children=[

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/HDKy2kq/Schermata-2019-06-27-alle-19-11-37.png
            " alt="slide 1" width="1150"> </center>
            '''),

                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
           <center><iframe width="1000" height="930" src="//www.cincopa.com/media-platform/iframe.aspx?fid=AMKAajOCCeai" frameborder="0" allowfullscreen scrolling="no"></iframe></center>
    '''),

                     ]),


                     ]),

        ]),

        dcc.Tab(label='Conclusioni', children=[

            dcc.Tabs(id="conclusionitabs", children=[
                dcc.Tab(label='Conclusioni', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/GQK2VPJ/capture-20190628141844159.png
            " alt="slide 1" width="1150"> </center>
            '''),

                        ]),
                dcc.Tab(label='Sviluppi futuri', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <center><img src="https://i.ibb.co/F4FVjKs/Schermata-2019-06-27-alle-19-12-38.png
            " alt="slide 1" width="1150"> </center>
            '''),

                        ]),
                dcc.Tab(label='Footer', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <br><br><br><br><center><img src="https://i.ibb.co/HgtghLD/Schermata-2019-06-27-alle-19-13-05.png
            " alt="slide 1" width="1150"> </center>
            '''),

                        ]),
            ]),

        ]),



    ])
])


@app.callback(
    dash.dependencies.Output("InDegreeDistributionGraph", "figure"),
    [dash.dependencies.Input("day-selected2", "value")])
def update_output(day):

    #print(inDegreeDistribution[inDegreeDistribution['Type']=='Attack'][inDegreeDistribution['Day'] == 1]['Value'])

    return {
        'data': [

            go.Bar(
                x=inDegreeDistribution.Range.unique(),
                y=inDegreeDistribution[inDegreeDistribution['Type'] ==
                                       'Attack'][inDegreeDistribution['Day'] == day]['Value'],
                name='Attacchi',
                marker=dict(
                    color=('rgb(255, 0, 0) '),
                ),


            ),
            go.Bar(
                x=inDegreeDistribution.Range.unique(),
                y=inDegreeDistribution[inDegreeDistribution['Type'] ==
                                       'Message'][inDegreeDistribution['Day'] == day]['Value'],
                name='Messaggi',
                marker=dict(
                    color=('rgb(76, 153, 0)'),

                ),


            ),
            go.Bar(
                x=inDegreeDistribution.Range.unique(),
                y=inDegreeDistribution[inDegreeDistribution['Type'] ==
                                       'Trade'][inDegreeDistribution['Day'] == day]['Value'],
                name='Commercio',
                marker=dict(
                    color=('rgb(255, 170, 102)'),

                ),

            ),
        ],



        'layout': go.Layout(
            xaxis={'title': 'Range'},
            yaxis={'title': 'Valori'},
            title='In Degree Distribution',
        )}


@app.callback(
    dash.dependencies.Output("OutDegreeDistributionGraph", "figure"),
    [dash.dependencies.Input("day-selected3", "value")])
def update_output(day):

    #print(inDegreeDistribution[outDegreeDistribution['Type']=='Attack'][outDegreeDistribution['Day'] == 1]['Value'])

    return {
        'data': [
            go.Bar(
                x=outDegreeDistribution.Range.unique(),
                y=outDegreeDistribution[outDegreeDistribution['Type'] ==
                                        'Attack'][outDegreeDistribution['Day'] == day]['Value'],
                name='Attacchi',
                marker=dict(
                    color=('rgb(255, 0, 0) '),
                ),


            ),
            go.Bar(
                x=outDegreeDistribution.Range.unique(),
                y=outDegreeDistribution[outDegreeDistribution['Type'] ==
                                        'Message'][outDegreeDistribution['Day'] == day]['Value'],
                name='Messaggi',
                marker=dict(
                    color=('rgb(76, 153, 0)'),

                ),


            ),
            go.Bar(
                x=outDegreeDistribution.Range.unique(),
                y=outDegreeDistribution[outDegreeDistribution['Type'] ==
                                        'Trade'][outDegreeDistribution['Day'] == day]['Value'],
                name='Commercio',
                marker=dict(
                    color=('rgb(255, 170, 102)'),

                ),

            ),
        ],



        'layout': go.Layout(
            xaxis={'title': 'Range'},
            yaxis={'title': 'Valori'},
            title='Out Degree Distribution',
        )}


@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("day-selected", "value")])
def update_output2(value):
    return {
        "data": [go.Pie(
            labels=edgesTrend["type"].unique().tolist(),
            values=edgesTrend[edgesTrend["day"] == value]["quantity"].tolist(),
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']},
            textinfo='label')],
        "layout": go.Layout(title=f"Trend report daily", margin={"l": 200, "r": 200, },
                            legend={"x": 1, "y": 0.7})}

# Callback trickster


@app.callback(
    dash.dependencies.Output('cheat-graphic', 'figure'),
    [dash.dependencies.Input('suspect-column', 'value')])
def update_pie(xaxis_column_name):
    dff = Trickster[Trickster['Suspect'] == xaxis_column_name]
    # print(dff.head())

    return {
        'data': [go.Bar(
            #print(dff[dff['Type'] == d]['Present']),
            x=dff[dff['Type'] == d]['Day'],
            y=dff[dff['Type'] == d]['Present'],
            text=d,
            name=d,
        ) for d in dff.Type.unique()],

        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear',
                'tickmode': 'linear'
            },
            yaxis={
                'range': [0, 1.5],
                'title': 'Activity',
                'type': 'linear', },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest',

        )
    }


'''  #Callback trickster
@app.callback( 
     dash.dependencies.Output('cheat-data', 'figure'),
     [dash.dependencies.Input('suspect-column', 'value')])

def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    print(dff.head())
   
    x = [dff['TradeIn'], dff['TradeOut']]
    print(x)

    return {
        'data': [go.Pie(
            
            labels=['AttackIn', 'MessageIn', 'TradeIn'], 
            values=[dff['AttackIn'].item(), dff['MessageIn'].item(), dff['TradeIn'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],
       
       

        'layout': go.Layout(
            title=f"IN", 
            margin={"l": 200, "r": 200, },
            legend={"x": 1, "y": 0.7})}
'''


@app.callback(
    dash.dependencies.Output('cheat-data-in', 'figure'),
    [dash.dependencies.Input('suspect-column', 'value')])
def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    # print(dff.head())

    x = [dff['TradeIn'], dff['TradeOut']]
    # print(x)

    return {
        'data': [go.Pie(

            labels=['AttackIn', 'MessageIn', 'TradeIn'],
            values=[dff['AttackIn'].item(), dff['MessageIn'].item(),
                    dff['TradeIn'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']},
            textinfo='label')],



        'layout': go.Layout(
            title=f"IN",
            margin={"l": 200, "r": 200, },
            legend={"x": 1, "y": 0.7})}


@app.callback(
    dash.dependencies.Output('cheat-data-out', 'figure'),
    [dash.dependencies.Input('suspect-column', 'value')])
def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    # print(dff.head())

    x = [dff['TradeIn'], dff['TradeOut']]
    # print(x)

    return {
        'data': [go.Pie(

            labels=['AttackOut', 'MessageOut', 'TradeOut'],
            values=[dff['AttackOut'].item(), dff['MessageOut'].item(),
                    dff['TradeOut'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']},
            textinfo='label')],



        'layout': go.Layout(
            title=f"OUT",
            margin={"l": 200, "r": 200, },
            legend={"x": 1, "y": 0.7})}


@app.callback(
    dash.dependencies.Output('index', 'children'),
    [dash.dependencies.Input('suspect-column', 'value')])
def set_display_children(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    return 'Guilty Index:  {}'.format(round(dff['GuiltyIndex'].item(), 3),)


@app.callback(
    dash.dependencies.Output('to', 'children'),
    [dash.dependencies.Input('suspect-column', 'value')])
def set_display_children(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    return '-> Invia a:  {}'.format(dff['Beneficiary'].item(),)


@app.callback(
    dash.dependencies.Output('from', 'children'),
    [dash.dependencies.Input('suspect-column', 'value')])
def set_display_children(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    return '<- Riceve da:  {}'.format(dff['ReceivedFrom'].item(),)


''' 
@app.callback( 
     dash.dependencies.Output('cheat-data', 'figure'),
     [dash.dependencies.Input('suspect-column', 'value')])

def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    print(dff.head())
   
    x = [dff['TradeIn'], dff['TradeOut']]
    print(x)


    traceIN =  [go.Pie(
            labels=['AttackIn', 'MessageIn', 'TradeIn'], 
            values=[dff['AttackIn'].item(), dff['MessageIn'].item(), dff['TradeIn'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],

    traceOUT =  [go.Pie(
            labels=['AttackOut', 'MessageOut', 'TradeOut'], 
            values=[dff['AttackOut'].item(), dff['MessageOut'].item(), dff['TradeOut'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],

    trace = traceIN + traceOUT,
    return {
        'data': trace,
       
       

        'layout': go.Layout(
            title=f"IN")}'''

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

# dcc.Tab(label='Trickster Detection', children=[
#               dcc.Tabs(id="Trickster tabs", children=[
#                    dcc.Tab(label='Introduzione', children=[
#
#                    ]),
#                ]),
#            ]),
