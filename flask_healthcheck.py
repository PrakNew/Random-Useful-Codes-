from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app_config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 121600,
    "JSON_SORT_KEYS": False,
}
app.config["TIMEOUT"] = 60000000
app.config.from_mapping(app_config)


@app.route("/healthcheck/app", methods=["GET"])
def healthcheck_status():
    try:
        return '{"m":"success","s":0,"d":[]}'
    except Exception as e:
        return "error"


if __name__ == "__main__":
    app.run(port=12000, debug=True, threaded=False, host="0.0.0.0")
