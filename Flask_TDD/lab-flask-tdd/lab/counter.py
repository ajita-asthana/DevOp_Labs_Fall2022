from flask import Flask
import status
from flask import abort
app = Flask(__name__)

COUNTER = {}

@app.route("/counters/<name>", methods = ["POST"])
def create_counter(name):
    """Creates a counter"""
    app.logger.info(f"Request to create a counter {name}")
    global COUNTER
    if name in COUNTER:
        abort(status.HTTP_409_CONFLICT, f"Counter {name} already exists")
    COUNTER [name]  =  0
    return {"name": name, "count":COUNTER[name]}, status.HTTP_201_CREATED


@app.route("/counters/<name>", methods = ["PUT"])
def update_counter(name):
    """Updates a counter"""
    app.logger.info(f"Request to update a counter {name}")
    global COUNTER
    if name not in COUNTER:
        abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exists")
    COUNTER [name]  +=  1
    app.logger.info(f"Value in counter {COUNTER[name]}")
    return {"name": name, "count":COUNTER[name]}, status.HTTP_200_OK

@app.route("/counters/<name>", methods = ["GET"])
def read_counter(name):
    """Reads a counter value"""
    app.logger.info(f"Request to read a counter {name}")
    global COUNTER
    if name not in COUNTER:
        abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exists")
 
    app.logger.info(f"Value in counter {COUNTER[name]}")
    return {"count": COUNTER[name]}, status.HTTP_200_OK

@app.route("/counters/<name>", methods = ["DELETE"])
def delete_counter(name):
    """Deletes a counter"""
    app.logger.info(f"Request to delete a counter {name}")
    global COUNTER
    if name not in COUNTER:
        abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exists")
    app.logger.info(f"Value in counter {COUNTER[name]}")
    del COUNTER[name]
    return {}, status.HTTP_200_OK