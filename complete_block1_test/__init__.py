#from ._builtin import Page, WaitPage
from otree.api import *

import numpy as np
import pandas as pd
import random
import sys

sys.path.append("/Users/meyerkn/Documents/GitHub") 
#from .models import Constants
from templates import gameblock1


#from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG
#from otree.api import (
#    models,
#    widgets,
#    BaseConstants,
#    BaseSubsession,
#    BaseGroup,
#    BasePlayer,
#    Currency as c,
#    currency_range,

import numpy as np
import pandas as pd
import random

doc = """
This is a coordination game with 4 players.
"""

class Constants(GameBlock.Constants):
    pass

class Subsession(GameBlock.Subsession):
    pass

class Group(GameBlock.Group):
    pass

class Player(GameBlock.Player):
    pass

class MyWaitPage(GameBlock.WaitPage):
    pass

class Decision(GameBlock.Page):
    pass

class ResultsWaitPage(GameBlock.WaitPage):
    pass

class Results(GameBlock.Page):
    pass

class newResults(GameBlock.Page):
    pass

page_sequence = GameBlock.page_sequence