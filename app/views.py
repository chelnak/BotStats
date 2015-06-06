import json
from flask import render_template, flash, redirect, request, url_for, g, session
from app import app,db
from .models import Log, Fact
from .forms import AddNewFact, LoginForm


@app.route('/')
def index():

    print "hello from index"
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
