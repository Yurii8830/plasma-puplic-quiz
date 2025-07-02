from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # змінити на більш безпечний у продакшн
app.jinja_env.globals.update(enumerate=enumerate)

# Питання по темі Plasma та Stablecoin Collective
questions = [
    {
        'question': 'What is Plasma in the context of blockchain?',
        'options': [
            'A layer 2 scaling solution',
            'A cryptocurrency',
            'A smart contract platform',
            'A mining algorithm'
        ],
        'answer': 'A layer 2 scaling solution'
    },
    {
        'question': 'What is the main purpose of the Stablecoin Collective within Plasma?',
        'options': [
            'To create new cryptocurrencies',
            'To promote stablecoin research and adoption',
            'To develop mining hardware',
            'To manage Plasma wallets'
        ],
        'answer': 'To promote stablecoin research and adoption'
    },
    {
        'question': 'Which of the following is NOT a benefit for Stablecoin Collective members?',
        'options': [
            'Regular research updates',
            'Private AMAs with industry leaders',
            'Free cryptocurrency airdrops',
            'Early access to Plasma products'
        ],
        'answer': 'Free cryptocurrency airdrops'
    },
    {
        'question': 'How can members unlock rewards in the Stablecoin Collective?',
        'options': [
            'By mining Plasma tokens',
            'By actively contributing to discussions and research',
            'By buying Plasma products',
            'By inviting friends to join'
        ],
        'answer': 'By actively contributing to discussions and research'
    },
    {
        'question': 'What special role is given to the most active and long-term supporters?',
        'options': [
            'SC Contributor',
            'Plasma OG',
            'Stablecoin Master',
            'Blockchain Ambassador'
        ],
        'answer': 'Plasma OG'
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'current' not in session:
        session['current'] = 0
        session['score'] = 0

    if request.method == 'POST':
        selected = request.form.get('option')
        correct = questions[session['current']]['answer']
        if selected == correct:
            session['score'] += 1
        session['current'] += 1

        if session['current'] >= len(questions):
            score = session['score']
            total = len(questions)
            session.clear()
            return render_template('result.html', score=score, total=total)

        return redirect(url_for('index'))

    current = session['current']
    return render_template('index.html',
                           question=questions[current],
                           qid=current + 1,
                           total=len(questions))


if __name__ == '__main__':
    app.run(debug=True)
