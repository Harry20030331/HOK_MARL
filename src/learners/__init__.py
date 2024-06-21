from .nq_learner import NQLearner
from .qtran_learner import QLearner

REGISTRY = {}

REGISTRY["nq_learner"] = NQLearner
REGISTRY["q_learner"] = QLearner