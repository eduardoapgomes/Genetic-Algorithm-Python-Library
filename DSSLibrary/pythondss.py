import py_dss_interface
import pandas as pd
import seaborn as sns
import numpy as np

from DSSLibrary.pythondss import *
from DSSLibrary.modeling import *
from DSSLibrary.costs import *

def start_dss():
    dss = py_dss_interface.DSSDLL()
    return dss


def run_dss_model(dss_model, dss):
    for model in dss_model:
        dss.text(f'{model}')
    return dss


def get_dss_voltages_dataframe(dss):
    NodeNames = dss.circuit_all_node_names()
    VoltagePu = dss.circuit_all_bus_vmag_pu()
    Bus = [Node.split('.')[0] for Node in NodeNames]
    Phase = [Node.split('.')[1] for Node in NodeNames]
    Buss_Data = pd.DataFrame({'Bus': Bus,
                              'Phase': Phase,
                              'Voltage': VoltagePu})
    return Buss_Data


def plot_voltages_dataframe(df):
    sns.set_theme(style="white")
    sns.set_context("paper")
    g = sns.catplot(data=df,
                    x="Voltage", y="Bus",
                    col='Phase',
                    height=6, aspect=.35,
                    size=7)
    sns.despine(left=True, bottom=True)
    for ax in g.axes.flat:
        ax.grid(True, axis='y', color="k",)
        ax.grid(True, axis='x', linestyle="--")


def get_line_df(dss):
    df1 = get_line_branch_df(dss)
    df2 = get_line_loss_df(dss)
    return pd.merge(df1, df2, on='Name')


def get_line_loss_df(dss):
    Elements = dss.circuit_all_element_names()
    Losses = np.array(dss.circuit_all_element_losses())
    P = Losses[0::2]
    Q = Losses[1::2]*1j
    S = P + Q
    LineLoss = pd.DataFrame({'Name': Elements, 'PowerLoss': S})
    LineLoss = LineLoss.query('Name.str.contains("Line")').copy()
    LineLoss.loc[:, 'Name'] = LineLoss.loc[:,
                                           'Name'].str.replace('Line.', '', regex=True)
    return LineLoss


def get_line_branch_df(dss):
    NumberofLines = dss.lines_count()
    dss.lines_first()
    for k in range(NumberofLines):
        BusA = dss.lines_read_bus1().split('.', 1)[0]
        BusB = dss.lines_read_bus2().split('.', 1)[0]
        Type = 'Line'
        # Length = dss.lines_read_length()
        if k == 0:
            branch_name = dss.lines_read_name()
            Branch = np.array([[BusA, BusB, Type, branch_name]])
            # ranchName = dss.lines_read_name()
        if (BusA != BusB):
            new_branch_name = dss.lines_read_name()
            new_branch = np.array([[BusA, BusB, Type, new_branch_name]])
            Branch = np.vstack((Branch, new_branch))
        dss.lines_next()
        TransmissionLines = pd.DataFrame(
            Branch, columns=['Bus1', 'Bus2', 'Type', 'Name'])
    return TransmissionLines
