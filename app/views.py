import json
from flask import render_template, flash, redirect, request, url_for, g, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, googlelogin
from .models import Log, Fact, User
from .forms import AddNewFact, LoginForm

"""
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('views.py')
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/var/log/botstats/botstats.log',when='midnight')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
"""

@app.route('/oauth2callback')
@googlelogin.oauth2callback
def login(token, userinfo, **params):

    next_url = request.args.get('next') or url_for('index')

    user = User.query.filter_by(google_id=userinfo['id']).first()

    if user is not None:
        user.name = userinfo['name']
        user.family_name = userinfo['family_name']
        user.given_name = userinfo['given_name']
        user.picture = userinfo['picture']
        user.link = userinfo['link']
    else:
        user = User(google_id = userinfo['id'], name = userinfo['name'], family_name = userinfo['family_name'], given_name = userinfo['given_name'], picture=userinfo['picture'], link=userinfo['link'])

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:  
        db.session.rollback()


    login_user(user)
    session['token'] = json.dumps(token)
    return redirect(url_for('manage'))

@app.route('/Logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))


@googlelogin.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():

    print "hello from index"
#    user = g.user
    totalProcessed = Log.query.count()
    repliedTo = Log.query.filter_by(replied=1)
    repliedToCount = Log.query.filter_by(replied=1).count()
    
    totalFacts = Fact.query.count()

    if repliedTo is None:
        repliedTo = "No records to return"


    return render_template('index.html',
                            title='Home',
                            repliedTo = repliedTo,
                            repliedToCount = repliedToCount,
                            totalProcessed = totalProcessed,
                                totalFacts = totalFacts)


@app.route('/Manage/Delete', methods=['POST'])
@login_required
def delete():
    if request.method == 'POST':
        try:
            id = request.args.get('id')
            f = Fact.query.get(id)
            db.session.delete(f)
            db.session.commit()
            flash('Fact {0} removed from database'.format(id))
        except Exception as e:
            flash(e)
            db.session.rollback()
    
    return redirect(url_for('manage'))


@app.route('/Manage', methods=['GET', 'POST'])
@login_required
def manage():

    facts = Fact.query.all()
    form = AddNewFact()

    if form.validate_on_submit():
        newFact = form.fact.data
        flash('New fact {0}'.format(newFact))

        try:
            f = Fact(fact=newFact)
            db.session.add(f)
            db.session.commit()
        except Exception as e:
            flash(e)
            db.session.rollback()
#            raise e

    return render_template('manage.html',
                            title='Manage',
                            facts = facts,
                            form = form)
