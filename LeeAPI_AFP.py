#!/usr/bin/env python
# coding: utf-8

import requests
from datetime import date
import pandas
import json

# info en https://www.quetalmiafp.cl/AccederCuotas

today = date.today()
URL_API='https://www.quetalmiafp.cl/api/Cuota/ObtenerCuotas?'
Liasta_AFP='listaAFPs=CAPITAL,CUPRUM,HABITAT,MODELO,PLANVITAL,PROVIDA,UNO'
Liasta_Fondos='&listaFondos=A,B,C,D,E'
Fecha_ini='&fechaInicial=01/01/2003'
Fecha_fin="&fechaFinal=%s/%s/%s" % (today.day, today.month, today.year)
dls = URL_API+Liasta_AFP+Liasta_Fondos+Fecha_ini+Fecha_fin
resp = requests.get(dls)

res = json.loads(resp.content)
Tabla=pandas.DataFrame.from_dict(res)
Tabla.to_csv('API_AFP.csv')
