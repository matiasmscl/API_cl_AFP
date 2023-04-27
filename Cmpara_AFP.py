#!/usr/bin/env python
# coding: utf-8

import pandas

Tabla=pandas.read_csv('API_AFP.csv').drop(columns=['Unnamed: 0'])

Tabla_comparadora=pandas.DataFrame()

Fondo_A=pandas.DataFrame()
Fondo_B=pandas.DataFrame()
Fondo_C=pandas.DataFrame()
Fondo_D=pandas.DataFrame()
Fondo_E=pandas.DataFrame()

for k in Tabla.index:   
    Tabla_comparadora.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']+'_'+Tabla.loc[k,'fondo']]=Tabla.loc[k,'valor']
    if Tabla.loc[k,'fondo']=='A':
        Fondo_A.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']]=Tabla.loc[k,'valor']
    if Tabla.loc[k,'fondo']=='B':
        Fondo_B.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']]=Tabla.loc[k,'valor']
    if Tabla.loc[k,'fondo']=='C':
        Fondo_C.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']]=Tabla.loc[k,'valor']
    if Tabla.loc[k,'fondo']=='D':
        Fondo_D.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']]=Tabla.loc[k,'valor']
    if Tabla.loc[k,'fondo']=='E':
        Fondo_E.loc[Tabla.loc[k,'fecha'],Tabla.loc[k,'afp']]=Tabla.loc[k,'valor']

Tabla_comparadora.to_csv('Comparacion_Fondos.csv')

