from flask import Flask

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>", methods=["GET"])
def alkuluku(luku):
    if luku < 2:
        on_alkuluku = False
    else:
        on_alkuluku = True
        for i in range(2, int(luku**0.5) + 1):
            if luku % i == 0:
                on_alkuluku = False
                break

    vastaus = {
        "number": luku,
        "isPrime": on_alkuluku
    }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
