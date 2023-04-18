from flask import Flask, render_template, request
from moduls import select_data, insert_data
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/gpa',  methods=['POST'])
def gpa_cu():
    culculs = request.form['culculs']
    fizika=request.form['fizika']
    programming = request.form['eprogramming']
    english = request.form['english']
    as1 = request.form['as']
    philosophy = request.form['philosophy']
    gpa = (8*int(culculs)+6*int(fizika)+4*int(philosophy)+6*int(programming)+4*int(english)+2*int(as1))/30
    gpa_rounded = round(gpa, 2)
    gpa_4 = (gpa*4)/5
    gpa_100 = (gpa*100)/5
    insert_data(culculs=culculs,fizika=fizika,programming=programming,philosophy=philosophy,as1=as1,english=english)
    return render_template('shortenurl.html', shortcode=gpa_rounded, gpa_4=round(gpa_4, 3), gpa_100=round(gpa_100, 2))


@app.route('/s')
def statistic():
    marks = select_data()
    calculus = marks[0][0]
    english = marks[0][1]
    fizika= marks[0][2]
    falsafa= marks[0][3]
    akademik_nutq= marks[0][4]
    dasturlash= marks[0][5]
    return render_template('more.html',
                           calculus=round(calculus, 2),
                           fizika=round(fizika, 2),
                           falsafa=round(falsafa, 2),
                           akademik_nutq=round(akademik_nutq, 2),
                           english=round(english, 2),
                           dasturlash=round(dasturlash, 2),
                           )


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
