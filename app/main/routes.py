from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app.main.forms import AddCharacterForm
from app.models import User, Character
from app.main import bp
from app import db

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@login_required
def index():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    c = Character()
    characters = c.get_characters(user_id=current_user.id)
    return render_template("index.html", title='Home Page', characters=characters, user=user)

@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=current_user.username).first_or_404()
    c = Character()
    characters = c.get_characters(user_id=current_user.id)
    return render_template('user.html', user=user, characters=characters)

@bp.route('/ac', methods=['GET', 'POST'])
@bp.route('/addcharacter', methods=['GET', 'POST'])
@login_required
def add_character():
    form = AddCharacterForm()
    user = User.query.filter_by(username=current_user.username).first_or_404()
    if form.validate_on_submit():
        character = Character(name=form.name.data,
                              level=form.level.data,
                              char_class=form.char_class.data,
                              char_race=form.char_race.data,
                              specialization=form.specialization.data,
                              profession0=form.profession0.data,
                              profession1=form.profession1.data,
                              needs=form.needs.data,
                              user_id=current_user.id
                              )
        db.session.add(character)
        db.session.commit()
        flash('Character Created!')
        return redirect(url_for('main.index'))
    c = Character()
    characters = c.get_characters(user_id=current_user.id)
    return render_template('addcharacter.html', title="Add Character", form=form, characters=characters)
