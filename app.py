from flask import Flask, jsonify, request, render_template
import threading
import time
import cleanrl_runner

app = Flask(__name__)

training_thread = None
training_logs = []

def run_training(params):
    global training_logs
    training_logs = []
    def log_callback(msg):
        training_logs.append(msg)
    cleanrl_runner.run_ppo(log_callback=log_callback, episodes=params.get('episodes', 10))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_training', methods=['POST'])
def start_training():
    global training_thread
    if training_thread and training_thread.is_alive():
        return jsonify({'status': 'Training already running'})
    params = request.json or {}
    training_thread = threading.Thread(target=run_training, args=(params,))
    training_thread.start()
    return jsonify({'status': 'Training started'})

@app.route('/training_status')
def training_status():
    return jsonify({
        'running': training_thread.is_alive() if training_thread else False,
        'logs': training_logs[-20:]
    })

if __name__ == '__main__':
    app.run(debug=True)
