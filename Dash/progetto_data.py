import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os


df = pd.read_csv('users_trend_30days.csv')




def generate_table_user_trend(dataframe, max_rows=30):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H1(children='MPROG Analysis'),
    html.H4(children='User trend in 30 days'),
    html.P('IL trend degli utenti nei 30 giorni è tendenzialmende descrescente'),
    html.P('La media degli utenti nei 30 giorni è di 2901'),

    dcc.Graph(
    id='example-graph',
    figure={
        'data': [
            {'x': df['day'], 'y': df['users'], 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'User Trend Visualization'
        }
    }
    ),
    generate_table_user_trend(df),
])

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
# )

if __name__ == '__main__':
    app.run_server(debug=True)