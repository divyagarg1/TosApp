from flask import Flask, render_template, request, json
import nltk
from gensim.summarization import summarize
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize1():
    _text =  request.form['inputText']
    if _text:
		return  json.dumps(summarizeAlgo(_text))
    else:
        return json.dumps({'html':'<span>Enter the text</span>'})

def summarizeAlgo(_text): 
	try:
		return summarize(_text, split=True, ratio=.05)
	except:
		return sys.exc_info()[0]

if __name__ == "__main__":
    app.run()
