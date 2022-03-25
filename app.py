# ***************************************
# Imports
# ***************************************
# Dash
from turtle import color
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from matplotlib.pyplot import colorbar, polar

# Div.
import pandas as pd
import numpy as np
import calendar

# Plotly
import plotly.express as px
import plotly.graph_objects as go

# ***************************************
# Get data
# ***************************************
import datamodel
order = datamodel.get_data()
df_year = datamodel.get_year()
df_month = datamodel.get_month()

# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_employee = px.bar(order, 
    x='emp_name', y='total', 
    color='type', text='total', title='Sales by Employee',
    hover_data=[],
    labels={'total':'Total sales', 'emp_name':'Employee', 'type':'Product Type'})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

fig_orderfigure = px.bar(order, 
    
    x='productname', y='total', 
    color='type', text='total', title='Sales by Products', 
    hover_data=[],
    labels={'total':'Total sales', 'type':'Product Type', 'productname':'Products'})
fig_orderfigure.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_orderfigure.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)


# ***************************************
# Activate the app
# ***************************************
#app = dash.Dash(__name__)

dash_app = dash.Dash(__name__)
app = dash_app.server

# ***************************************
# Layout
# ***************************************
dash_app.layout = html.Div(
    children=[
        html.Div(className='eight columns div-for-charts bg-grey',
            children=[
                dcc.Graph(id="sales_employee", figure=fig_employee),
                dcc.Graph(id="sales_productname", figure=fig_orderfigure)])

            
    ]
        )

# ***************************************
# Callbacks
# ***************************************
# Output er diagrammet
# Input er DropDown
# @dash_app.callback(Output('sales_employee', 'figure'),
#               [Input('drop_month', 'value')],
#               [Input('drop_year', 'value')])

# def update_graph(drop_month, drop_year):
#     if drop_year:
#         if drop_month:
#             # Data i både drop_month og drop_year
#             order_fig1 = order.loc[(order['orderyear'] == drop_year) & (order['ordermonth'] == drop_month)]
#         else:
#             # Data i drop_year. men ikke drop_month
#             order_fig1 = order.loc[order['orderyear'] == drop_year]
#     else:
#         if drop_month:
#             # Data i drop_month, men ikke drop_year
#             order_fig1 = order.loc[order['ordermonth'] == drop_month]
#         else:
#             # Ingen data - ikke noget valgt
#             order_fig1 = order
        
#     return {'data':[go.Bar(
#         x = order_fig1['emp_name'],
#         y = order_fig1['total'], title = 'Employee sales'
#             )
#         ]
#     }

# ***************************************
# Run the app
# ***************************************
if __name__ == '__main__':
    dash_app.run_server(debug=True)
