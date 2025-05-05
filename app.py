from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Predefined QA pairs
responses = {
    "What is the total revenue?": "The total revenue is $10 million.",
    "How has net income changed over the last year?": "Net income increased by 12% over the last year.",
    "What are the key performance indicators?": "The KPIs include ROI, EBITDA margin, and customer acquisition cost.",
    "What is the current burn rate?": "The current monthly burn rate is $150,000.",
    "What is our gross profit margin?": "The gross profit margin is 68%."
}

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if 'conversation' not in session:
        session['conversation'] = []

    user_query = None
    bot_response = None

    if request.method == 'POST':
        user_query = request.form['query']
        bot_response = responses.get(user_query, "Sorry, I can only answer predefined questions.")

        session['conversation'].append({'user': user_query, 'bot': bot_response})
        session.modified = True

    return render_template('index.html', conversation=session['conversation'])

if __name__ == '__main__':
    app.run(debug=True)
