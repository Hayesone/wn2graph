from flask import Flask
from flask import render_template, request
from wn2graph import cyphers
from wn2graph.config import graph
from forms import word2input, word1inputs

app = Flask(__name__)
app.config['SECRET_KEY'] = '2c8553196a4dafa672b8c68d70a24e21eedb937d'


w2c = word1inputs()

@app.route('/')
def hello_world():  # put application's code here
    return home()

@app.route("/home/", methods=['GET', 'POST'])
def home(): # home landing page
    return render_template("home.html")

@app.route("/w2word/", methods=['GET', 'POST'])
def w2word(): # home landing page
    print("w2word()")
    form = word2input(request.form)

    if request.method == 'POST' and form.validate():
        wordN = form.word1.data
        wordT = form.word2.data
        try:
            print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
            cypherOut = cyphers.word2word(wordN, wordT)
            print(cypherOut)
            return render_template("w2word.html", w2word_form=form, cypherOut=cypherOut)
        except:
            return render_template("w2word.html", w2word_form=form)


    print("Using default values for query")

    wordN = "open"
    wordT = "close"
    print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
    cypherOut = cyphers.word2word(wordN, wordT)
    print(cypherOut)
    return render_template("w2word.html", w2word_form=form, cypherOut=cypherOut)

@app.route("/w2synonym/", methods=['GET', 'POST'])
def w2synonym(): # home landing page
    errorInput = "<h2>Error with input, either input is not in the graph, or input is not lowercase"
    form = word1inputs(request.form)

    if request.method == 'POST' and form.validate():
        wordN = form.word1.data
        try:
            print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
            cypherOut = cyphers.word2connects(wordN)
            print(cypherOut)
            return render_template("w2synonym.html", form=form, cypherOut=cypherOut)
        except:
            return render_template("w2synonym.html", form=form)

    print("Using default values for query")

    wordN = "open"
    print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
    cypherOut = cyphers.word2connects(wordN)
    print(cypherOut)
    return render_template("w2synonym.html", form=form, cypherOut=cypherOut)

@app.route("/w2concept2w/", methods=['GET', 'POST'])
def w2concept2w(): # home landing page
    errorInput = "<h2>Error with input, either input is not in the graph, or input is not lowercase"
    form = word1inputs(request.form)

    if request.method == 'POST' and form.validate():
        wordN = form.word1.data
        try:
            print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
            cypherOut = cyphers.wordsFromRelatedConcepts(wordN)
            print(cypherOut)
            return render_template("w2concept2w.html", form=form, cypherOut=cypherOut)
        except:
            return render_template("w2concept2w.html", form=form)

    print("Using default values for query")

    wordN = "open"
    print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
    cypherOut = cyphers.wordsFromRelatedConcepts(wordN)
    print(cypherOut)
    return render_template("w2concept2w.html", form=form, cypherOut=cypherOut)


@app.route("/w2wjaccard/", methods=['GET', 'POST'])
def w2wjaccard(): # home landing page
    print("w2wjaccard()")
    form = word2input(request.form)

    if request.method == 'POST' and form.validate():
        wordN = form.word1.data
        wordT = form.word2.data
        try:
            print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
            cypherOut = cyphers.w2wjacard(wordN, wordT)
            print(cypherOut)
            return render_template("w2wjaccard.html", w2word_form=form, cypherOut=cypherOut)
        except:
            return render_template("w2wjaccard.html", w2word_form=form)


    print("Using default values for query")

    wordN = "open"
    wordT = "open up"
    print(f"GDS projected graph created: {cyphers.checkExsistsGDSgraph()}")
    cypherOut = cyphers.w2wjacard(wordN, wordT)
    print(cypherOut)
    return render_template("w2wjaccard.html", w2word_form=form, cypherOut=cypherOut)

if __name__ == '__main__':
    app.run()
