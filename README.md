# TempoRL

Code for the BIG@ICML Workshop paper<BR>
**Towards TempoRL: Learning When to Act**

    @inproceedings{biedenkapp-bigicml20,
      author    = {A. Biedenkapp and R. Rajan and F. Hutter and M. Lindauer},
      title     = {Towards {T}empo{RL}: Learning When to Act},
      booktitle = {Workshop on Inductive Biases, Invariances and Generalization in {RL} ({BIG@ICML}'20)},
      year = {2020},
      month     = jul,
    }

## Setup
You only need to install the dependencies
```bash
pip install -r requirements.txt
```

To make use of the provided jupyter notebook you optionally have to install jupyter
```bash
pip install jupyter
```

## How to train tabular agents
To run an agent on any of the below listed environments run
```bash
python tabular_agents.py -e 10000 --agent Agent --env env_name --eval-eps 500
```
replace Agent with `q` for vanilla q-learning and `sq` for our method.

## Envs
Currently 6 simple environments available.
Per default all environments give a reward of 1 when reaching the goal (X).
The agents start in state (S) and can traverse open fields (o).
When falling into "lava" (.) the agent receives a reward of -1.
For no other transition are rewards generated. (When rendering environments the agent is marked with *)
An agent can use at most 100 steps to reach the goal.

Modifications of the below listed environments can run without goal rewards (env_name ends in _ng)
or reduce the goal reward by the number of taken steps (env_name ends in _perc).
* lava (Cliff)
    ```console
    S  o  .  .  .  .  .  .  o  X
    o  o  .  .  .  .  .  .  o  o
    o  o  .  .  .  .  .  .  o  o
    o  o  o  o  o  o  o  o  o  o
    o  o  o  o  o  o  o  o  o  o
    o  o  o  o  o  o  o  o  o  o
    ```

* lava2 (Bridge)
    ```console
    S  o  .  .  .  .  .  .  o  X
    o  o  .  .  .  .  .  .  o  o
    o  o  o  o  o  o  o  o  o  o
    o  o  o  o  o  o  o  o  o  o
    o  o  .  .  .  .  .  .  o  o
    o  o  .  .  .  .  .  .  o  o
    ```

* lava3 (ZigZag)
    ```console
    S  o  .  .  o  o  o  o  o  o
    o  o  .  .  o  o  o  o  o  o
    o  o  .  .  o  o  .  .  o  o
    o  o  .  .  o  o  .  .  o  o
    o  o  o  o  o  o  .  .  o  o
    o  o  o  o  o  o  .  .  o  X
    ```
  
## Experiment data
All data for experiments we ran for the BIG@ICML workshop can be found in the experiments folder

To load and plot the data you can make use of the big_workshop_plots notebook which uses the methods in utils to load
and plot the data.