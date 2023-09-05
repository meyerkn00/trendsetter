from otree.api import *
import numpy as np
import pandas as pd
import random

doc = """
This is a coordination game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'complete_understanding_b4'
    players_per_group = 4
    num_rounds = 1

    instructions_new_template = 'complete_understanding_b4/instructions_new.html'
    instructions_template = 'complete_understanding_b4/instructions.html'


class Subsession(BaseSubsession):
    pass

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
    pass

class Player(BasePlayer):
    Q = models.StringField(
        label= 'What is your maximum payoff in each round?',
        choices= ['28 points', '20 points', '12 points', '4 points', 'Unknown']

    #widget=widgets.Select
    )
    comprehension_wrong_attempts = models.PositiveIntegerField()   # number of wrong attempts on understanding quesions page




class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Waiting for other participants. If it has been awhile, refresh the page."

class Introduction(Page):
    pass

class Q(Page):
    page_title = 'Comprehension Question'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_fields = ['Q']
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'

    @staticmethod
    def error_message(player, values):
        error_messages = dict()

        if values['Q'] != "28 points":
            error_messages["Q"] = 'Wrong answer'
            player.comprehension_wrong_attempts = 1

        return error_messages

    


page_sequence = [MyWaitPage, Introduction, Q]