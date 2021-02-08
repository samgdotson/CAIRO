import numpy as np
import os
import glob
import sys
import getopt
import matplotlib.pyplot as plt
from tools import NRMSE


plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['figure.edgecolor'] = 'k'
plt.rcParams['figure.facecolor'] = 'w'
plt.rcParams['savefig.dpi'] = 400
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "serif"


options_dict = {'-u': 'windspeed',
                '-w': 'wettemp',
                '-d': 'drytemp',
                '-p': 'pressure',
                '-h': 'humidity',
                }


def get_prediction_data():
    """
    This function returns a list of paths to all .npy loss
    files.

    Returns
    -------
    path_list : list of strings
        The list of paths to output files
    """

    path = "./data/*_prediction.npy"

    path_list = glob.glob(path, recursive=True)
    return path_list


def get_metadata(data_file):
    """
    This function accepts a file name and returns the parameters
    for the simulation.

    Parameters
    ----------
    data_file : string
        The name of the file that contains the simulation data.
    """

    params = {'n_reservoir': 1000,
              'sparsity': 0.1,
              'rand_seed': 85,
              'rho': 1.5,
              'noise': 0.0001,
              'future': 48,
              'window': 48,
              'trainlen': 5000}

    param_names = {'Reservoir Size':'n_reservoir',
                   'Sparsity':'sparsity',
                   'Spectral Radius':'rho',
                   'Noise':'noise',
                   'Training Length':'trainlen',
                   'Prediction Window':'window'}

    splitstring = data_file.split('/')[-1]
    # print(splitstring)
    target_file = splitstring.replace('npy', 'png')
    simulation_name = splitstring.split('_prediction.npy')[0]
    # print(simulation_name)

    with open("./data/simulation_MD.txt", 'r') as file:
        metadata = file.readlines()

    for i, line in enumerate(metadata):
        if simulation_name in line:
            param_string = metadata[i+1]
            break

    param_list = param_string.split(',')
    for p in param_list:
        splitp = p.split(':')
        name,value = splitp[0].strip(), splitp[1].strip()
        # print(name,value)
        key = param_names[name]
        if name in ['Reservoir Size', 'Training Length', 'Prediction Window']:
            params[key] = int(value)
        else:
            params[key] = float(value)

    # print(params)

    return params, param_string, target_file


def get_training_data(simulation_name):
    """
    This function gets the training data used in a particular simulation.

    Parameters
    ----------
    simulation_name : string
        The name of the simulation

    Returns
    -------
    training_data : numpy array
        The array of testing and prediction data
        used to plot.
    """

    data = None
    if 'demand' in simulation_name:
        primary_data = pd.read_csv('uiuc_demand_data.csv',
                                   usecols=['time, kw'],
                                   parse_dates=True,
                                   index_col='time')
    elif 'wind' in simulation_name:
        primary_data = pd.read_csv('railsplitter_data.csv',
                                   usecols=['time, kw'],
                                   parse_dates=True,
                                   index_col='time')
    elif 'solar' in simulation_name:
        primary_data = pd.read_csv('solarfarm_data.csv',
                                   usecols=['time, kw'],
                                   parse_dates=True,
                                   index_col='time')

    if any(list(options_dict.values)) in simulation_name:
        if 'wind' in simulation_name;
        
    return


def get_parameters(pstring):
    """
    This function returns a dictionary of parameters given
    a parameters string. Reverses the function ``param_string``.
    """

    return

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'ai:',
                                   ['infile=', ])
    except getopt.GetoptError:
        print(f'Valid options are: -a, -i, --infile')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-i', '--infile'):
            prediction_files = [arg]
        if opt in ('-a'):
            prediction_files = get_prediction_data()

    # print(len(prediction_files))

    target_folder = "./figures/"

    if not os.path.isdir(target_folder):
        os.mkdir(target_folder)

    # print(prediction_files)

    if len(prediction_files) == 1:
        parameters = get_metadata(prediction_files)
    else:
        for file in prediction_files:
            if 'lorenz' in file:
                continue
            else:
                params, pstring, target_file = get_metadata(file)
                simulation_data = np.load(file)
                # print(len(simulation_data))
