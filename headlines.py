from flask import Flask, render_template, jsonify, request
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}


# @app.route("/bbc")
# def bbc():
#     return get_news('bbc')
# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    query = request.args.get("publication")
    
    if not query or query.lower() not in RSS_FEEDS:
            publication = 'bbc'
        
    else:
        publication = query
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    
    return  render_template("home.html", articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
