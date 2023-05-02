import py_dss_interface
import pandas as pd
import seaborn as sns
import numpy as np

from DSSLibrary.pythondss import *
from DSSLibrary.modeling import *
from DSSLibrary.costs import *

def circuit_model(default_lines):
    dss_model = np.concatenate([
        set_feeder(),
        set_line_models(),
        set_lines(default_lines),
        set_loads(),
        set_solver()])
    return dss_model


def set_feeder():
    dss_model = f'''
    Clear
    ! Modelo de Barra infinita
    New Circuit.lineGA basekv = 12.66 pu= 1.0
    ~ bus1 = node1
    ~ Z0=[0.0000001,0.0000001] Z1=[0.0000001,0.0000001]
    '''
    return dss_model.splitlines()


def set_solver():
    dss_model = f'''
    Set VoltageBases = 12.66
    calcvoltagebases
    Solve
    '''
    return dss_model.splitlines()


def set_line_models():
    dss_model = f'''
    New linecode.Cond1 		nphases=3 		R1=0.8190 		X1=0.7070 		units=km
    New linecode.Cond2 		nphases=3 		R1=0.7114 		X1=0.2351 		units=km
    New linecode.Cond3 		nphases=3 		R1=0.1872 		X1=0.6188 		units=km
    New linecode.Cond4 		nphases=3 		R1=0.0922 		X1=0.0470 		units=km
    New linecode.Cond5 		nphases=3 		R1=0.05532 		X1=0.0470 		units=km
    '''
    return dss_model.splitlines()


def set_lines(linelist):
    dss_model = f'''
    new line.L1  linecode=Cond{linelist[0]}  length=1            units=km bus1=sourcebus bus2=node1  phases=3
    new line.L2  linecode=Cond{linelist[1]}  length=5.347071584  units=km bus1=node1     bus2=node2  phases=3
    new line.L3  linecode=Cond{linelist[2]}  length=3.969631236  units=km bus1=node2     bus2=node3  phases=3
    new line.L4  linecode=Cond{linelist[3]}  length=4.13340564   units=km bus1=node3     bus2=node4  phases=3
    new line.L5  linecode=Cond{linelist[4]}  length=1            units=km bus1=node4     bus2=node5  phases=3
    new line.L6  linecode=Cond{linelist[5]}  length=1            units=km bus1=node5     bus2=node6  phases=3
    new line.L7  linecode=Cond{linelist[6]}  length=1            units=km bus1=node6     bus2=node7  phases=3
    new line.L8  linecode=Cond{linelist[7]}  length=1.257631258  units=km bus1=node7     bus2=node8  phases=3
    new line.L9  linecode=Cond{linelist[8]}  length=1.274725275  units=km bus1=node8     bus2=node9  phases=3
    new line.L10 linecode=Cond{linelist[9]}  length=0.27635648   units=km bus1=node9     bus2=node10 phases=3   
    new line.L11 linecode=Cond{linelist[10]} length=0.526286196  units=km bus1=node10    bus2=node11 phases=3  
    new line.L12 linecode=Cond{linelist[11]} length=1.792429792  units=km bus1=node11    bus2=node12 phases=3  
    new line.L13 linecode=Cond{linelist[12]} length=2.893162393  units=km bus1=node12    bus2=node13 phases=3  
    new line.L14 linecode=Cond{linelist[13]} length=0.721611722  units=km bus1=node13    bus2=node14 phases=3  
    new line.L15 linecode=Cond{linelist[14]} length=0.911233211  units=km bus1=node14    bus2=node15 phases=3  
    new line.L16 linecode=Cond{linelist[15]} length=6.885683761  units=km bus1=node15    bus2=node16 phases=3  
    new line.L17 linecode=Cond{linelist[16]} length=0.893772894  units=km bus1=node16    bus2=node17 phases=3  
    new line.L18 linecode=Cond{linelist[17]} length=0.876068376  units=km bus1=node1     bus2=node18 phases=3  
    new line.L19 linecode=Cond{linelist[18]} length=1.836630037  units=km bus1=node18    bus2=node19 phases=3  
    new line.L20 linecode=Cond{linelist[19]} length=2.1875       units=km bus1=node19    bus2=node20 phases=3  
    new line.L21 linecode=Cond{linelist[20]} length=3.786858974  units=km bus1=node20    bus2=node21 phases=3  
    new line.L22 linecode=Cond{linelist[21]} length=0.550915751  units=km bus1=node2     bus2=node22 phases=3  
    new line.L23 linecode=Cond{linelist[22]} length=1.096459096  units=km bus1=node22    bus2=node23 phases=3  
    new line.L24 linecode=Cond{linelist[23]} length=1.094017094  units=km bus1=node23    bus2=node24 phases=3  
    new line.L25 linecode=Cond{linelist[24]} length=2.201735358  units=km bus1=node5     bus2=node25 phases=3  
    new line.L26 linecode=Cond{linelist[25]} length=3.082429501  units=km bus1=node25    bus2=node26 phases=3  
    new line.L27 linecode=Cond{linelist[26]} length=1.293040293  units=km bus1=node26    bus2=node27 phases=3  
    new line.L28 linecode=Cond{linelist[27]} length=0.981929182  units=km bus1=node27    bus2=node28 phases=3  
    new line.L29 linecode=Cond{linelist[28]} length=5.504338395  units=km bus1=node28    bus2=node29 phases=3  
    new line.L30 linecode=Cond{linelist[29]} length=5.205128205  units=km bus1=node29    bus2=node30 phases=3  
    new line.L31 linecode=Cond{linelist[30]} length=1.658653846  units=km bus1=node30    bus2=node31 phases=3  
    new line.L32 linecode=Cond{linelist[31]} length=1.821581197  units=km bus1=node31    bus2=node32 phases=3  
    new line.L33 linecode=Cond{linelist[32]} length=10.68376068  units=km bus1=node7     bus2=node20 phases=3  
    new line.L34 linecode=Cond{linelist[33]} length=10.68376068  units=km bus1=node8     bus2=node14 phases=3  
    new line.L35 linecode=Cond{linelist[34]} length=10.68376068  units=km bus1=node11    bus2=node21 phases=3  
    new line.L36 linecode=Cond{linelist[35]} length=2.670940171  units=km bus1=node17    bus2=node32 phases=3  
    new line.L37 linecode=Cond{linelist[36]} length=2.670940171  units=km bus1=node24    bus2=node28 phases=3
    '''
    return dss_model.splitlines()


def set_loads():
    dss_model = f'''
    new load.Load1  bus1=node1   phases=3 kw=(1 100 *) kVar=(1 60 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load2  bus1=node2   phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load3  bus1=node3   phases=3 kw=(1 120 *) kVar=(1 80 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load4  bus1=node4   phases=3 kw=(1 60 *)  kVar=(1 30 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load5  bus1=node5   phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load6  bus1=node6   phases=3 kw=(1 200 *) kVar=(1 100 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load7  bus1=node7   phases=3 kw=(1 200 *) kVar=(1 100 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load8  bus1=node8   phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load9  bus1=node9   phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load10 bus1=node10  phases=3 kw=(1 45 *)  kVar=(1 30 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load11 bus1=node11  phases=3 kw=(1 60 *)  kVar=(1 35 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load12 bus1=node12  phases=3 kw=(1 60 *)  kVar=(1 35 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load13 bus1=node13  phases=3 kw=(1 120 *) kVar=(1 80 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load14 bus1=node14  phases=3 kw=(1 60 *)  kVar=(1 10 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load15 bus1=node15  phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load16 bus1=node16  phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load17 bus1=node17  phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load18 bus1=node18  phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load19 bus1=node19  phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load20 bus1=node20  phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load21 bus1=node21  phases=3 kw=(1 90 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load22 bus1=node22  phases=3 kw=(1 90 *)  kVar=(1 50 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load23 bus1=node23  phases=3 kw=(1 420 *) kVar=(1 200 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load24 bus1=node24  phases=3 kw=(1 420 *) kVar=(1 200 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load25 bus1=node25  phases=3 kw=(1 60 *)  kVar=(1 25 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load26 bus1=node26  phases=3 kw=(1 60 *)  kVar=(1 25 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load27 bus1=node27  phases=3 kw=(1 60 *)  kVar=(1 20 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load28 bus1=node28  phases=3 kw=(1 120 *) kVar=(1 70 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load29 bus1=node29  phases=3 kw=(1 200 *) kVar=(1 600 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load30 bus1=node30  phases=3 kw=(1 150 *) kVar=(1 70 *)   model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load31 bus1=node31  phases=3 kw=(1 210 *) kVar=(1 100 *)  model=1 kV=(12.66 1 sqrt /)  vminpu=0.5
    new load.Load32 bus1=node32  phases=3 kw=(1 60 *)  kVar=(1 40 *)   model=1 kV=(12.66 1 sqrt /)  Vminpu=0.5
    '''
    return dss_model.splitlines()
