import psutil
from flask import Flask, render_template, jsonify
from collections import deque
import time

app = Flask(__name__)

# Deques to store CPU and memory history for live charting (up to 10 data points)
cpu_history = deque(maxlen=10)
mem_history = deque(maxlen=10)
time_history = deque(maxlen=10)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent

    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"

    # Update history for live chart
    current_time = time.strftime('%H:%M:%S')  # Get current time in HH:MM:SS format
    cpu_history.append(cpu_metric)
    mem_history.append(mem_metric)
    time_history.append(current_time)

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

@app.route("/metrics")
def metrics():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent

    data = {
        "cpu_metric": cpu_metric,
        "mem_metric": mem_metric,
        "cpu_history": list(cpu_history),
        "mem_history": list(mem_history),
        "time_history": list(time_history)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
