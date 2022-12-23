from itertools import *
from functools import *
import operator
from iterthings import *
from copy import deepcopy
import numpy as np
from dataclasses import dataclass, field
from typing import *
from collections import deque
from heapq import *
from time import sleep
from math import *
from bisect import insort

import re

def ints(s):
    return map(int, re.findall("-?\d+", s))