from dash import Dash, dash_table
import pandas as pd
import services

def get_data():
    return services.get_wikipedia_data()

def get_layout():
    df = get_data()
    layout = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        page_size=10,
        style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
        ],
        style_data={
        'color': 'black',
        'backgroundColor': 'white',
        'whiteSpace': 'normal',
        'height': 'auto',
        },
        style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
         ],
        style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
        }
        )
    return layout





