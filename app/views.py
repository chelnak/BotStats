from flask import render_template
from app import app, db
from .models import Log, Fact

@app.route('/')
@app.route('/index')

def index():
    
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
