from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length, URL

classes = [('Druid', 'Druid'),
           ('Hunter', 'Hunter'),
           ('Mage', 'Mage'),
           ('Paladin', 'Paladin'),
           ('Priest', 'Priest'),
           ('Rogue', 'Rogue'),
           # 'Shaman', # Only Alliance.
           ('Warlock', 'Warlock'),
           ('Warrior', 'Warrior'),]

races = [('Dwarf', 'Dwarf'),
         ('Gnome', 'Gnome'),
         ('Human', 'Human'),
         ('Night Elf', 'Night Elf'),]

professions = [('Alchemy', 'Alchemy'),
               ('Blacksmithing', 'Blacksmithing'),
               ('Enchanting', 'Enchanting'),
               ('Engineering', 'Engineering'),
               ('Herbalism', 'Herbalism'),
               ('Leatherworking', 'Leatherworking'),
               ('Mining', 'Mining'),
               ('Skinning', 'Skinning'),
               ('Tailoring', 'Tailoring'),
               ]

def tuple(a,b):
    return (a,b)

class AddCharacterForm(FlaskForm):
    name = StringField('Character Name', validators=[DataRequired(), Length(min=1, max=64)])
    char_class = SelectField('Character Class', choices=classes, validators=[DataRequired()])
    char_race = SelectField('Character race', choices=races, validators=[DataRequired()])
    level = SelectField('Character Level', choices=[tuple(f'{n+1}',f'{n+1}') for n in range(60)], validators=[DataRequired()])
    specialization = StringField('Spec, eg holy(20),discp(21)', validators=[Length(min=0, max=140)])
    profession0 = SelectField('First Profession', choices=professions)
    profession1 = SelectField('Second Profession', choices=professions)
    needs = TextAreaField('Anything you may need', validators=[Length(min=0, max=256)])
    submit = SubmitField('Submit new character')
