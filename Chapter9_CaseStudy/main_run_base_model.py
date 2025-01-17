# Import Python Packages
import gc
import numpy as np
from datetime import datetime
from glob import glob
import os

from default_parameters_config import _default_algo_params_lgbm, _default_fit_params_lgbm, _default_model_lgbm, _default_skfold_params 
from default_parameters_config import _default_algo_params_logistic,_default_fit_params_logistic, _default_model_logistic
from default_parameters_config import _default_algo_params_nn, _default_fit_params_nn, _default_model_neuralnetwork

from preprocessing import *
from model_helper import *
from model_train import *

cur_dir = os.getcwd()
input_dir = cur_dir + "//input//"
output_dir = cur_dir + "//output//"
if os.path.isdir(output_dir)==False: os.mkdir(output_dir)

#-----------------------------------------#
def run_model(model_type,model_map,input_dir, output_dir):
    save_dir = '{}/model_{}'.format(output_dir,model_type)
    print('------- run model: {} '.format(model_type))
    if model_type.lower() in ['lgbm']:
      x_train, x_test, y_train, ids = build_model_input(input_dir=input_dir)
    else:
      x_train, x_test, y_train, ids = build_model_input_extended(input_dir=input_dir)
    # get train results
    res = train_results(x_train, x_test, y_train, ids, model_map[model_type])

    if os.path.isdir(save_dir)==False:
      os.mkdir(save_dir)
    print('-------- save results to {f}:{m}'.format(m=model_type, f=save_dir))
    save_training_results(res,model_type=model_type, save_dir=save_dir)

#------------------------------#
model_map = {
    'logistic': _default_model_logistic,
    'neuralnetwork': _default_model_neuralnetwork,
    'lgbm': _default_model_lgbm}

run_model('lgbm', model_map, input_dir, output_dir)

run_model('logistic', model_map, input_dir, output_dir)

run_model('neuralnetwork', model_map, input_dir, output_dir)



