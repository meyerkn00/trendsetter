#from ._builtin import Page, WaitPage
from otree.api import *

import numpy as np
import pandas as pd
import random
import sys

sys.path.append("/Users/meyerkn/Documents/GitHub/Trendsetter") 

from templates import gameblock as gb


import numpy as np
import pandas as pd
import random

doc = """
This is a coordination game with 4 players.
"""

network = "complete"
blocknum = 1
apptype = "gameblock"

class Constants(gb.Constants):
    pass

class Subsession(gb.Subsession):
    pass

class Group(gb.Group):
    pass

class Player(gb.Player):
    pass

class MyWaitPage(gb.WaitPage):
    pass

class Decision(gb.Page):
    pass

class ResultsWaitPage(gb.WaitPage):
    pass

class Results(gb.Page):
    pass

class newResults(gb.Page):
    pass

page_sequence = gb.page_sequence