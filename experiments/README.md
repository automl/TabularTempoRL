# Experiments
We provide all data we obtained when running vanilla q-learning and tempoRL q-learning.

This data can be visualized with the notebook big_workshop_plots in the folder above.
## Folder structure
For every experiment we track the command that was used to create the output as well as the resulting rewards/episode lengths.
The folder structure is as follows:
```
Big Workshop
└───bridge
│   └───q-experiment-0.1-const           (method-eperiment-StartEpsilon-EpsilonSchedule, maxSkip is irrelevant for q)
│   │   └───10000_7_100_1                (numTrainEpisodes_maxSkip_MaxStepsInEnv_Seed)
│   │   │   │    args.txt                (args stored in argparse namespace)
│   │   │   │    command.txt             (command used to generate output)
│   │   │   │    steps_per_episode.pkl   (Number of steps per episode over the whole training process)
│   │   │   │    test_data.pkl           (Recorded test (epsilon=0) reward and decision points per evaluation episode)
│   │   │   │    train_data.pkl          (Recorded train (epsilon=0) reward and decision points per training episode)
│   │   │ 
│   │   └───10000_7_100_2
│   │   │   │    ...            (Same files as above)
│   │   │   ...
│   │   │ 
│   │   └───10000_7_100_100
│   │   │   │    ...            (for all 100 seeds)
│   │   │ 
│   └───q-experiment-1.0-linear
│   │   ...                     (same subfolders as above. Contains results for 100 seeds)
│   │
│   └───q-experiment-1.0-log
│   │   ...
│   │
│   └───sq-experiment-0.1-const 
│   │   ...
│   │
│   └───sq-experiment-1.0-linear
│   │   ...
│   │
│   └───sq-experiment-1.0-log
│   │   ...
│   
└───cliff
│   ...  (same subfolder structure as for bridge, evaluated on 100 seeds)
│   
└───zigzag
│   ...  (same subfolder structure as for bridge, evaluated on 100 seeds)
│   
└───cliff
│   └───j_ablation    
│   │   └───zigzag  (we performed this ablation study only on zigzag)
│   │   │   └───sq-experiment-0.1-const
│   │   │   │   └───10000_2_100_1                (numTrainEpisodes_maxSkip_MaxStepsInEnv_Seed)
│   │   │   │   │   │    ...
│   │   │   │   │   ...              (subfolder structure as before, evaluated on only 10 seeds with max_skip=2)
│   │   │   │   │ 
│   │   │   │   └───10000_2_100_10
│   │   │   │   │   │    ...
│   │   │   │   │   ...
│   │   │   │   │ 
│   │   │   │   └───10000_16_100_1
│   │   │   │   │   │    ...         (subfolder structure as before, evaluated on only 10 seeds with max_skip=16)
│   │   │   │   │   ...
│   │   │   │   │ 
│   │   │   │   └───10000_16_100_10
│   │   │   │   │   │    ...
```