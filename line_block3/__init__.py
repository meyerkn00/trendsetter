#from ._builtin import Page, WaitPage
from otree.api import *
#from .models import Constants


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


class Constants(BaseConstants):
    name_in_url = 'line_block3'
    players_per_group = 4
    num_rounds = 10

    #instructions_template = 'line_block3/instructions.html'
    instructions_new_template = 'line_block3/instructions_new.html'

    # payoffs if player picks green""",
    #onegreen_payoff = c(0)
    #twogreen_payoff = c(0)
    #threegreen_payoff = c(0)
    #fourgreen_payoff = c(0)

    # payoffs if player picks purple
    #onepurple_payoff = c(0)
    #twopurple_payoff = c(0)
    #threepurple_payoff = c(0)
    #fourpurple_payoff = c(0)

    # payoffs if player picks yellow
    #oneyellow_payoff = c(3)
    #twoyellow_payoff = c(6)
    #threeyellow_payoff = c(9)
    #fouryellow_payoff = c(12)


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        decisions = [
            p.decision for p in self.get_players() if p.decision != None
        ]
        if decisions:
            return dict(
                decisionlist=decisions
            )
        else:
            return dict(
                decisionlist='(no data)',
            )

def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    # we now place users into different baskets, according to their group in the previous app.
    # the dict 'd' will contain all these baskets.
    d = {}
    for p in waiting_players:
        group_id = p.participant.past_group_id
        if group_id not in d:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            d[group_id] = []
        players_in_my_group = d[group_id]
        players_in_my_group.append(p)
        if len(players_in_my_group) == 4:
            return players_in_my_group
        # print('d is', d)

class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.set_payoff()


class Player(BasePlayer):
    #decision = models.StringField(
        #widget=widgets.RadioSelectHorizontal
    #)
    decision = models.StringField(
        choices=[['Green', 'Green'], ['Purple', 'Purple'], ['Yellow', 'Yellow']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )    

    def decision_choices(self):
        import random
        choices = [['Green', 'Green'], ['Purple', 'Purple'], ['Yellow', 'Yellow']]
        random.shuffle(choices)
        return choices

    #decision = models.StringField(widget = widgets.RadioSelectHorizontal, choices=decision_choices())


    def other_player1(self):
        return self.get_others_in_group()[0]
    def other_player2(self):
        return self.get_others_in_group()[1]
    def other_player3(self):
        return self.get_others_in_group()[2]
 



def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)

def set_payoff(player: Player):
    greenval = 7
    purpleval = 5
    yellowval = 3
    todf = {'Green': [greenval, 2*greenval, 3*greenval, 4*greenval],
            'Purple': [purpleval, 2*purpleval, 3*purpleval, 4*purpleval],
            'Yellow': [yellowval, 2*yellowval, 3*yellowval, 4*yellowval]}

    payoff_matrix = pd.DataFrame(todf)

    

    choicecolumn = payoff_matrix[player.decision]
    player.payoff = choicecolumn[[player.get_others_in_group()[0].decision,
                                player.get_others_in_group()[1].decision,
                                player.get_others_in_group()[2].decision].count(player.decision)]



    


   
# def get_payoff(self):
#     greenval = 0
#     purpleval = 0
#     yellowval = 3
#     todf = {'Green': [greenval, 2*greenval, 3*greenval, 4*greenval],
#             'Purple': [purpleval, 2*purpleval, 3*purpleval, 4*purpleval],
#             'Yellow': [yellowval, 2*yellowval, 3*yellowval, 4*yellowval]}
#     payoff_matrix = pd.DataFrame(todf)

#     choicecolumn = payoff_matrix[self.decision]
#     self.payoff = choicecolumn[[self.other_player1().decision,
#                                 self.other_player2().decision,
#                                 self.other_player3().decision].count(self.decision)]
#     return self.payoff



class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Waiting for other participants. If it has been awhile, refresh the page."

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    body_text = "Waiting for other participants. If it has been awhile, refresh the page."


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group())

class newResults(Page):
    pass


page_sequence = [MyWaitPage, Decision, ResultsWaitPage, Results]