from otree.api import *
import numpy as np
import pandas as pd
import random

doc = """
This is a coordination game with 4 players.
"""


colors = ['Purple','Green','Yellow','Unknown']
players = ['Q', 'R', 'T', 'S', 'Unknown']

class Constants(BaseConstants):
    name_in_url = 'star_understanding_b1'
    players_per_group = 4
    num_rounds = 1
    block_number = 1
    network_name = "star"

    instructions_template = '_templates/global/instructions.html'
    instructions_new_template = '_templates/global/repeat_instructions_template.html'



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass






class Player(BasePlayer):

    Q1 = models.StringField(
            label= 'What is your maximum payoff in each round?', min=3, max=3,
            choices= ['28 points', '20 points', '12 points', '4 points', 'Unknown']

        #widget=widgets.Select
        )

    Q2 =models.StringField(
            label ='Which player are you?',
            choices = players
        )

    Q3 =  models.StringField(
            label = 'Whose payoffs are shown to you at the end of each round?',
            choices = {'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}
        )
    Q4 =  models.StringField(
            label =  'Can the way payoffs are calculated change within each block of ten rounds?',
            choices =  random.sample(['Yes', 'No'], 2)
        )
    Q5 = models.StringField(
            label =  'Can the way payoffs are calculated change from block to block?',
            choices =  ['Yes (and you will be told if they changed)', 'No']
        )

    Q6 = models.StringField(
            label =  'Which color did Player Q choose?', 
            choices =  colors
        )

    Q7 = models.StringField(
            label =  'Which color did Player R choose?', 
            choices =  colors
        )
    Q8 =  models.StringField(
            label =  'Which color did Player S choose?', 
            choices =  colors
        )
    Q9 = models.StringField(
            label =  'Which color did Player T choose?', 
            choices =  colors
        )
    comprehension_wrong_attempts = models.PositiveIntegerField()   # number of wrong attempts on understanding quesions page



class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Sorting you into a group. If it has been awhile, refresh the page."

    @staticmethod
    def after_all_players_arrive(group: Group):
        # save each participant's current group ID so it can be
        # accessed in the next app.
        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id

class Introduction(Page):
    pass

class Q(Page):
    def is_displayed(self):
        return self.id_in_group == 1

    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'


    form_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']


    @staticmethod
    def error_message(player, values):
        solutions = dict(
            Q1='12 points',
            Q2='Q',
            Q3='Only your own',
            Q4='No',
            Q5='Yes (and you will be told if they changed)',
            Q6='Purple',
            Q7='Unknown',
            Q8='Yellow',
            Q9='Unknown'
        )
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
                player.comprehension_wrong_attempts = 1

        return error_messages

   

class R(Page):
    def is_displayed(self):
        return self.id_in_group == 2
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']


    @staticmethod
    def error_message(player, values):
        solutions = dict(
            Q1='12 points',
            Q2='R',
            Q3='Only your own',
            Q4='No',
            Q5='Yes (and you will be told if they changed)',
            Q6='Unknown',
            Q7='Purple',
            Q8='Yellow',
            Q9='Unknown'
        )
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
                player.comprehension_wrong_attempts = 1

        return error_messages


class T(Page):
    def is_displayed(self):
        return self.id_in_group == 3
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']


    @staticmethod
    def error_message(player, values):
        solutions = dict(
            Q1='12 points',
            Q2='T',
            Q3='Only your own',
            Q4='No',
            Q5='Yes (and you will be told if they changed)',
            Q6='Unknown',
            Q7='Unknown',
            Q8='Yellow',
            Q9='Purple'
        )
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
                player.comprehension_wrong_attempts = 1

        return error_messages


class S(Page):
    def is_displayed(self):
        return self.id_in_group == 4
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']


    @staticmethod
    def error_message(player, values):
        solutions = dict(
            Q1='12 points',
            Q2='S',
            Q3='Only your own',
            Q4='No',
            Q5='Yes (and you will be told if they changed)',
            Q6='Yellow',
            Q7='Purple',
            Q8='Purple',
            Q9='Green'
        )
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
                player.comprehension_wrong_attempts = 1

        return error_messages

page_sequence = [MyWaitPage, Introduction, Q, R, S, T]