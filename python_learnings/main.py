from flask import Flask,render_template,request
from calculations import events
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        quantity = int(request.form['quantity'])
        per_person = int(request.form['per_person'])
        per_gift = int(request.form['per_gift'])
        clothes = int(request.form['clothes'])
        jwellery = int(request.form['jwellery'])

        obj = events(quantity, per_person, per_gift, clothes, jwellery)

        data = {
            'banquet': obj.banquet_hall(),
            'decor': obj.decor(),
            'makeup': obj.makeup(),
            'gifts': obj.gifts(),
            'shopping': obj.shopping()
        }
        data['total'] = sum(data.values())
        return render_template('result.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)