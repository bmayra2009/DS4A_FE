# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:19:05 2020

@author: 28dan
"""
import numpy as np
import pandas as pd
from skimage import io, data, transform
from time import sleep
from datetime import datetime,timedelta

import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from appraisal_app import Appraisal_calculator
#from app_layout import App

from flask import Flask                                                             ####-----
server = Flask(__name__) 
app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.PULSE],server=server
)
app.config.suppress_callback_exceptions = True

body = html.Div(style={
#'background-image': 'url("/assets/logo_diego2.jpg")',
'background-image': 'url("/assets/960w.jpg")',
#'background-image': 'url("/assets/ejecafetero2.jpg")',
'background-repeat': 'no-repeat',
'background-position': 'center top',
'background-size': '1350px 600px'
},children = [html.Br(),
html.Div(id= "main_buttons",
         style    = {'width' : "100%"},
         children = [html.Div([dbc.Row([dbc.Col([dbc.Button(
                            "APPRAISAL CALCULATOR",
                            id="appraisal-calculator-button", color="info",#outline=True,
                            style={'text-align':'center', 'margin-left': '850px'}
                            #style={'backgroundColor': 'transparent', 'color':'black','width':'10%', 'border':'1.5px black solid', 'height': '50px','text-align':'center', 'marginRight': '100px'}
                        )], width=9),
         dbc.Col([dbc.Button(
                            "TEAM MEMBERS",
                            id="team-member-button", color="info"#,outline=True
                        )],
         width=3)])
                       ])]),
html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
dbc.Row([html.H1('Welcome to AvalPredict',style={'text-align': 'center','margin-left':'300px','color':'black', 'background-color': 'white'}),
                                                           html.P(id='err')]),
dbc.Row([
                          html.Label("Choose a municipality", 
                                     style={'margin-left':'300px','color':'white'}),
                          dcc.Dropdown(
                                        id='drop_municipality', 
                                        options= [{'label': k, 'value': k} for k in ['Chiquinquira','Cumaribo']], 
                                        clearable=False,
                                        value="Chiquinquira",
                                        style={'font-size': "100%", "width":"75%",'margin-left':'12%'}
                                        )]),
dbc.Row([
    
    ]),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br()
])
    
app.layout = html.Div([dcc.Location(id = 'url', refresh = False),
					             html.Div(id ='page-content',children=body)])

@app.callback([dash.dependencies.Output('err', 'children'),dash.dependencies.Output('page-content', 'children')],
              [dash.dependencies.Input('appraisal-calculator-button', 'n_clicks')])
def validacion_user(n_clicks):
    if n_clicks is None:
        return dash.no_update,dash.no_update
    else:
        print("clic")
        return html.P("Ingresando",style={'font-weight': 'bold','color': 'green'}),Appraisal_calculator()

app.run_server(port = 805,debug=True)