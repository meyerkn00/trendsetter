from os import environ


SESSION_CONFIGS = [
    dict(
        name='complete',
        display_name="Complete",
        num_demo_participants=4,
        app_sequence=['consent', 'complete_understanding_b1', 'complete_block1', 'complete_understanding_b2', \
        'complete_block2', 'complete_understanding_b3', 'complete_block3', 'complete_understanding_b4', \
        'complete_block4','complete_understanding_b5', 'complete_block5', 'complete_understanding_b6', \
        'complete_block6', 'survey', 'end']
    ), 
    dict(
        name='line',
        display_name="Line",
        num_demo_participants=4,
        app_sequence=['consent','line_understanding_b1', 'line_block1', 'line_understanding_b2', \
        'line_block2', 'line_understanding_b3', 'line_block3', 'line_understanding_b4', 'line_block4', \
        'line_understanding_b5', 'line_block5', 'line_understanding_b6', 'line_block6' , 'survey','end']
    ),
    dict(
        name='star',
        display_name="Star",
        num_demo_participants=4,
        app_sequence=['consent','star_understanding_b1', 'star_block1', 'star_understanding_b2', 'star_block2', \
        'star_understanding_b3', 'star_block3', 'star_understanding_b4', 'star_block4', 'star_understanding_b5', \
        'star_block5', 'star_understanding_b6', 'star_block6' , 'survey','end']
    ), 
    dict(
        name='circle',
        display_name="Circle",
        num_demo_participants=4,
        app_sequence=['consent','circle_understanding_b1', 'circle_block1', 'circle_understanding_b2', \
        'circle_block2', 'circle_understanding_b3', 'circle_block3', 'circle_understanding_b4', \
        'circle_block4', 'circle_understanding_b5', 'circle_block5', 'circle_understanding_b6', 'circle_block6' , 'survey','end']
    ),
    dict(
        name='survey',
        display_name="Survey",
        num_demo_participants=4,
        app_sequence=['survey','end']
    ),
    dict(
        name='circle_test',
        display_name="Circle Test",
        num_demo_participants=4,
        app_sequence=['consent_test', 'circle_understanding_b1', 'circle_block1']
    )

]




# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.20, participation_fee=10.00, doc=""
)

PARTICIPANT_FIELDS = ["past_group_id"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '4664874292208'

INSTALLED_APPS = ['otree']
