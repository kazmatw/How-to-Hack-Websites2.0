from flask import Flask, render_template, session, request
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_bytes()

items = {5427: ("Black Shiba ", 1024),
         5428: ("Red Shiba", 1024),
         5429: ("White Shiba", 4096),
         5430: ("FLAG", 99999999),
         5431: ("Evil Shiba", 65536),
         5432: ("Null Shiba", 0)}


@app.route("/")
def home():
    if 'money' not in session:
        session['money'] = 65536
    if 'stuff' not in session:
        session['stuff'] = []
    return render_template("index.html", items=items)


@app.route("/item/<int:item_id>")
def view_item(item_id):
    return render_template("item.html", item=items[item_id], item_id=item_id)


@app.route("/buy", methods=['POST'])
def buy_item():
    cost = int(request.form.get("cost"))
    item_id = int(request.form.get("item_id"))
    wallet = int(request.form.get("wallet", session['money']))
    if cost > wallet:
        return "<script>alert(`You don't have enough money Q_Q`); location.href='/';</script>"
    session['money'] = wallet - cost
    session['stuff'].append(items[item_id])
    return "<script>alert(`Success!`); location='/'</script>"


if __name__ == "__main__":
    app.run(debug=True)
