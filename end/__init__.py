from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    feedback = models.StringField(label="Please provide any feedback or suggestions about your experience")

class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback']

class End(Page):
    pass

page_sequence = [Feedback, End]