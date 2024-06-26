# -*- coding: utf-8 -*-
"""
Spyder Editor
programa: selector
creado por Carlos Ramirez
"""

texto = r'SDD Dominican data 201701.out'
entrada = open(texto)
lineas = entrada.readlines()
linea = lineas[:50]

def get_select(lineas,start,end):
    return lineas[start:end]

def get_indices(lineas):
    indices = []
    i = 0
    while i < len(lineas):
        if lineas[i][-2]=='1':
            ind = lineas.index(lineas[i])
            indices.append(ind)
        i+=1
    indices.append(lineas.index(lineas[-2]))
    return indices
v = get_indices(lineas)
selec = get_select(lineas,v[0],v[1])

def formatear(select):
    
    l1 = ''
    l2 = ''
    for n in select:
        if n[-2] == '1':
            l1 = n
        if n[-2] == 'E':
            l2 = n
    l1 = l1.split()
    l2 = l2.split()
    #hacer fecha
    anio =l1[0]
    if len(l1[1])==1:
        mes = '0'+l1[1]
    else:
        mes = l1[1]
    if len(l1[2])==1:
        dia = '0'+l1[2]
    else:
        dia = l1[2]
    fecha = anio+'-'+mes+'-'+dia
    #hacer hora
    hora = l1[3][:2]+':'+l1[3][2:]
    if len(l1[4][:-2])==1:
        sec = '0'+l1[4][:-2]
    else:
        sec = l1[4][:-2]
    hora+=':'+sec
    print (hora)
    lat = l1[6]
    lon = l1[7]
    #la profundidad(dep) siempre debe tener 5 cs
    dep = l1[8]
    dif = 5 - len(dep)
    dep = dif*' '+dep
    print (dep)
    rms = l1[11]
    mc = '  '
    ml = '  '
    mw = '  '
    for n in l1:
        if 'L' in n:
            ml = n[:3]
        if 'C' in n:
            mc = n[:3]
        if 'W' in n:
            mw = n[:3]
    gap = l2[0][4:]
    error_dep = l2[4]
    print (gap,error_dep)
formatear(selec)
        
