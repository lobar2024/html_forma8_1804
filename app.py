from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = int(request.form.get('c'))

        kopaytir = a * b * c

        return render_template('result8.html', name=name, a=a, b=b, c=c, kopaytir=kopaytir)

    return render_template('index7.html')

if __name__ == '__main__':
    app.run(debug=True)
