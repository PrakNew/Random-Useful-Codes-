from flask import Flask, request
from flask_cors import CORS
from flask_pydantic import validate
from pydantic import BaseModel

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


class SearchQuery(BaseModel):
    query: str


class QueryModel(BaseModel):
    age: int


class ResponseModel(BaseModel):
    id: int
    age: int
    name: str
    nickname: str


# Example 1: query parameters only
@app.route("/", methods=["GET"])
@validate()
def get(query: QueryModel):
    age = query.age
    return ResponseModel(age=age, id=0, name="abc", nickname="123")


@app.route("/healthcheck/app", methods=["GET"])
@validate()
def healthcheck_status():
    try:
        # print("REQUEST: ", query.query)
        # print("QUERY", query)
        return '{"m":"success","s":0,"d":[]}'
    except Exception as e:
        return "error"


if __name__ == "__main__":
    app.run(port=12000, debug=True, threaded=False, host="0.0.0.0")
