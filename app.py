from flask import Flask, render_template, request, json
import nltk
from nltk import word_tokenize
from gensim.summarization import summarize, keywords
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import re
import numpy as np
import pandas as pd
from lda_summarization import summarize_methods
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

@app.route('/ldasummarize', methods=['POST'])
def summarize2():
    _text = request.form['inputText']
    summarize_lda(_text)
    if _text:
        return json.dumps(summarize_lda(_text))
    else:
        return json.dumps({'html': '<span>Enter the text</span>'})

def summarizeAlgo(_text):

    tos_text_paras = _text.split("\n")
    copyright = ['Collective Work',\
    'Compilation',\
    'Compulsory License',\
    'Copyright',\
    'Copyright Holder/Copyright Owner',\
    'Copyright Notice',\
    'Derivative Work',\
    'Exclusive Right',\
    'Expression',\
    'Fair Use',\
    'First Sale Doctrine',\
    'Fixation',\
    'Idea',\
    'Infringement',\
    'Intellectual Property',\
    'License',\
    'Master Use License',\
    'Mechanical License',\
    'Medium',\
    'Moral Rights',\
    'Musical Composition',\
    'Parody',\
    'Patent',\
    'Performing Rights',\
    'Permission',\
    'Public Domain',\
    'Publication/Publish',\
    'Right Of Publicity',\
    'Royalty',\
    'Service Mark',\
    'Sound Recording',\
    'Statutory Damages',\
    'Synchronization License',\
    'Tangible Form Of Expression',\
    'Term',\
    'Title',\
    'Trademark',\
    'Trade Secret',\
    'Work For Hire']

    privacy = ["privacy"]

    copyright_all,privacy_all = [],[]

    for para in tos_text_paras:
        check = 0
        for word in para.split(" "):
            if word in copyright:
                copyright_all.append(para)
                check = 1
            if word in privacy:
                privacy_all.append(para)
                check = 1
            if check != 0:
                break

    copyright_all = [sent for sent in copyright_all if len(word_tokenize(sent)) > 5]

    privacy_all = [sent for sent in privacy_all if len(word_tokenize(sent)) > 5]

    categoryDict = {}

    if (len(copyright_all) != 0):

        if (len(copyright_all) != 1):

            copyright_text = ' '.join(copyright_all)
            copyright_all = summarize(copyright_text, split=True, ratio=.5)


        categoryDict["Copyright"] = copyright_all




    if (len(privacy_all) != 0):
        if (len(privacy_all) != 1):
            privacy_text = ' '.join(privacy_all)
            privacy_all = summarize(privacy_text, split=True, ratio=.5)
        categoryDict["Privacy"] = privacy_all


    for key in categoryDict.keys():
        print(key + ":")
        print(categoryDict[key])
        print()
    return categoryDict

def summarize_lda(_text):
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()
    topic_dic = {'Privacy': ['privacy', 'cookie', 'confidentiality'],
                 'Copyright': ['copyright', 'infringement', 'dmca', 'intellectual', 'holder', 'agent', 'trademark'],
                 'Content Sharing/Use': ['share'],
                 'Cancelation/Termination': ['cease', 'terminate', 'suspend', 'cancel'],
                 'Modification/Pricing': ['modification', 'pricing']}
    dictionary2 = corpora.Dictionary.load('lda_dictionary')
    ldamodel2 = gensim.models.ldamodel.LdaModel.load('lda_model')
    pars = re.split('\r?\n\r?\n+', _text)
    topic_pars = summarize_methods.create_topic_pars(pars, tokenizer, p_stemmer, en_stop, ldamodel2, dictionary2, topic_dic)

    category_dict = {}
    for topic_par in topic_pars:
        cat = topic_par[1]
        par = topic_par[0]
        if (cat not in category_dict):
            category_dict[cat] = [par]
        else:
            category_dict[cat].append(par)

    #for topic in category_dict:
    #    category_dict[topic] = summarize(' '.join(category_dict[topic]), split=True, ratio=.1)
    return(category_dict)


if __name__ == "__main__":
    app.run()
