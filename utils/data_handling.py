import yaml
import os
import glob
import pickle
import numpy as np


def load_config():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config'), 'r') as ymlf:
        cfg = yaml.load(ymlf, Loader=yaml.FullLoader)
    return cfg


def load_data(experiment_dir="experiments_01_28", methods=['sq', 'q'], exp_version='-1.0-linear',
              episodes=50_000, max_skip=6, max_steps=100, local=True):
    cfg = load_config()
    method_test_rewards = {}
    method_test_lengths = {}
    method_steps_per_episodes = {}
    if not local:
        print('Loading from')
        print(os.path.join(cfg['data']['local' if local else 'remote'], experiment_dir))
    for method in methods:
        print(method)
        files = glob.glob(
            os.path.join(cfg['data']['local' if local else 'remote'], experiment_dir,
                         '{:s}-experiments{:s}'.format(method, exp_version),
                         '{:d}_{:d}_{:d}_*', 'test_data.pkl'
                         ).format(
                episodes,
                max_skip,
                max_steps
            ))
        test_rewards, test_lens, steps_per_eps = [], [], []
        for file in files:
            with open(file, 'rb') as fh:
                data = pickle.load(fh)
                test_rewards.append(data[0])
                test_lens.append(data[1])
            try:
                with open(file.replace('test_data', 'steps_per_episode'), 'rb') as fh:
                    data = pickle.load(fh)
                    steps_per_eps.append(data[1])
            except FileNotFoundError:
                print('No steps data found')

        method_test_rewards[method] = np.array(test_rewards)
        method_test_lengths[method] = np.array(test_lens)
        method_steps_per_episodes[method] = np.array(steps_per_eps)
    return method_test_rewards, method_test_lengths, method_steps_per_episodes
