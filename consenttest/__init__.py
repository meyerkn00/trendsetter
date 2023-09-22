from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = 4
    num_rounds = 1

    zerotoseven_choices = [[1, ''],
                   [2, ''], [3, ''],
                   [4, ''],
                   [5, ''], [6, ''],
                   [7, '']]
    zerotoseven_ints=[1,2,3,4,5,6,7]

    Autonomy_1_table = 'survey/Autonomy_1.html'
    Autonomy_2_table = 'survey/Autonomy_2.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def assign_surveys(self):
        import random
        if random.random() < 0.5:
            value = True
        else:
            value = False

        for p in self.get_players():
            p.assign_surveys_player(value)





class Player(BasePlayer):

    signature = models.StringField(label="Signature")

    #firstname = models.StringField(label="First name")

    #lastname = models.StringField(label="Last name")

    #address = models.StringField(label='Mailing address')

    WBL_ID = models.StringField(label='WBL ID')

    #city = models.StringField(label='City')

    #state = models.StringField(label='State')

    #zip = models.FloatField(label='ZIP Code')

    #birthdate = models.StringField(label="Date of birth (mm/dd/yyyy)")

    #SSN = models.StringField(label="Social Security Number (if applicable; enter NA if it is not)")
    
    #email = models.StringField(label='Your email address')

    #dropped = models.StringField(initial="False")

    accept = models.StringField(
        choices=[['I APPROVE', 'I APPROVE'], ['I DO NOT APPROVE', 'I DO NOT APPROVE']],
        label='',
        widget=widgets.RadioSelect
    )

    before = models.StringField(label="Survey")

    def error_message(self, values):
        print('values is', values)
        return 'A response has indicated that you are not paying attention. Please revisit the questions below.'

    def setSurvey(self, status):
        self.before = status

    def assign_surveys_player(self, value):
        import random
        #set dropped var to false to begin 
        self.participant.vars['dropped'] = False
        if value == True:
            self.participant.vars['survey_before'] = True
            self.before = "True"
        else:
            self.participant.vars['survey_before'] = False
            self.before = "False"

    age = models.FloatField(label='Age', min=18)

    #pid = models.StringField(label='What is your Prolific ID?')

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'],
                 ['Other','Other'], ['Prefer not to say','Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )



class Consent_form(Page):
    form_model = 'player'
    form_fields = ['signature']

    

class Payment_info(Page):
    form_model = 'player'
    form_fields = ["WBL_ID"]




class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']




#class ConsentWaitPage(WaitPage):
#    after_all_players_arrive = "assign_surveys"

 
        

page_sequence = [Consent_form, Payment_info]
