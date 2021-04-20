from flask import Flask, render_template
import redis, time

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count(os_route):
    """ Se encarga de contar las visitas a cada uno de los endpoints expuestos:
    windows, linux y mac. Larga el fallo luego de 5 intentos fallidos.

    Argumento:
    os_route -- La ruta solicitada/visitada
    """
    retries = 5
    while True:
        try:
            if(os_route == "windows"):
                return cache.incr('hitsWindows')
            elif(os_route == "linux"):
                return cache.incr('hitsLinux')
            elif(os_route == "mac"):
                return cache.incr('hitsMac')
        except redis.exceptions.ConnectionError as e:
            if(retries == 0):
                raise e
            retries -= 1
            time.sleep(0.5)


@app.route("/windows")
def windowsWeb():
    countWindows = get_hit_count("windows")
    return render_template("windows.html", countWindows=countWindows)


@app.route("/mac")
def macWeb():
    countMac = get_hit_count("mac")
    return render_template("mac.html", countMac=countMac)


@app.route("/linux")
def linuxWeb():
    countLinux = get_hit_count("linux")
    return render_template("linux.html", countLinux=countLinux)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/other")
def other():
    return render_template("other.html")


@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):
  return render_template("404.html")

if __name__ == "__app__":
    app.run(debug=True)

# Run Flask Application
app.run(host="0.0.0.0", port=5000)
