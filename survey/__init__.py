from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    zerotoseven_choices = [[1, ''],
                   [2, ''], [3, ''],
                   [4, ''],
                   [5, ''], [6, ''],
                   [7, '']]
    zerotoseven_ints=[1,2,3,4,5,6,7]

    zerototen_ints  =[0,1,2,3,4,5,6,7,8,9,10]
    
    zerototen_choices = [[1, ''],
                   [2, ''], [3, ''],
                   [4, ''],
                   [5, ''], [6, ''],
                   [7, ''], [8, ''],
                   [9, ''] ,[10,'']]

    Autonomy_1_table = 'survey/Autonomy_1.html'
    Autonomy_2_table = 'survey/Autonomy_2.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    

    def error_message(self, values):
        print('values is', values)
        return 'A response has indicated that you are not paying attention. Please revisit the questions below.'



    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'],
                 ['Other','Other'], ['Prefer not to say','Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    autgen_1_1 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel like I am free to decide for myself how to live my life.',
        widget=widgets.RadioSelect
    )

    autgen_1_2 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel pressured in my life.',
        widget=widgets.RadioSelect
    )

    autgen_1_3 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I generally feel free to express my ideas and opinions.',
        widget=widgets.RadioSelect
    )

    autgen_1_4 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='In my daily life, I frequently have to do what I am told.',
        widget=widgets.RadioSelect
    )

    autgen_1_5 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='People I interact with on a daily basis tend to take my feelings into consideration.',
        widget=widgets.RadioSelect
    )

    autgen_1_6 = models.IntegerField(
        choices=Constants.zerotoseven_ints, min=3, max=3,
        label='Please click three in order to show that you are paying attention.',
        widget=widgets.RadioSelect
    )

    autgen_1_7 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel like I can pretty much be myself in my daily situations.',
        widget=widgets.RadioSelect
    )

    autgen_1_8 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='There is not much opportunity for me to decide for myself how to do things in my daily life.',
        widget=widgets.RadioSelect
    )

    autgen_2_1 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I can always manage to solve difficult problems if I try hard enough',
        widget=widgets.RadioSelect
    )

    autgen_2_2 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='If someone opposes me, I can find the ways and means to get what I want.',
        widget=widgets.RadioSelect
    )

    autgen_2_3 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I am certain that I can accomplish my goals.',
        widget=widgets.RadioSelect
    )

    autgen_2_4 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I am confident that I could deal efficiently with unexpected events.',
        widget=widgets.RadioSelect
    )

    autgen_2_5 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='Thanks to my resourcefulness, I can handle unforeseen situations.',
        widget=widgets.RadioSelect
    )

    autgen_2_6 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I can solve most problems if I invest the necessary effort.',
        widget=widgets.RadioSelect
    )

    autgen_2_7 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I can remain calm when facing difficulties because I can rely on my coping abilities.',
        widget=widgets.RadioSelect
    )

    autgen_2_8 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='When I am confronted with a problem, I can find several solutions.',
        widget=widgets.RadioSelect
    )

    autgen_2_9 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
    label="If I am in trouble, I can think of a good solution.",
    widget=widgets.RadioSelect
    )
    
    autgen_2_10 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
    label="I can handle whatever comes my way.",
    widget=widgets.RadioSelect
    )

    risk_preference = models.IntegerField(
        choices=Constants.zerototen_ints,
    label="How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?",
    widget=widgets.RadioSelect
    )

    autonomy_attention_check = models.IntegerField()



class Autonomy_1(Page):
    form_model = 'player'
    form_fields = ['autgen_1_1', 'autgen_1_2', 'autgen_1_3', 'autgen_1_4', 'autgen_1_5', 'autgen_1_6', 'autgen_1_7', 'autgen_1_8']

    @staticmethod
    def error_message(player, values):
        
        error_messages = dict()


        if values["autgen_1_6"] != 3:
            error_messages["autgen_1_6"] = 'Failed Attention Check'
            player.autonomy_attention_check = 1

        return error_messages

class SE(Page):
    form_model = 'player'
    form_fields = ['autgen_2_1', 'autgen_2_2', 'autgen_2_3', 'autgen_2_4', 'autgen_2_5', 'autgen_2_6', 'autgen_2_7', 'autgen_2_8', 'autgen_2_9', 'autgen_2_10']

class RP(Page):
    form_model = 'player'
    form_fields = ['risk_preference']

#class Risk(Page):
        

page_sequence = [RP, Autonomy_1, SE]
