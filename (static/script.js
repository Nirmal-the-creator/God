const startBtn = document.getElementById('startBtn');
const status = document.getElementById('status');
const logArea = document.getElementById('logArea');
let pollingInterval;

startBtn.onclick = () => {
  fetch('/start_training', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ episodes: 10 }) })
    .then(res => res.json())
    .then(data => {
      status.textContent = `Status: ${data.status}`;
      if (data.status === 'Training started') {
        startPolling();
      }
    });
};

function startPolling() {
  if (pollingInterval) clearInterval(pollingInterval);
  pollingInterval = setInterval(() => {
    fetch('/training_status').then(res => res.json()).then(data => {
      status.textContent = `Status: ${data.running ? 'Training running...' : 'Idle'}`;
      logArea.textContent = data.logs.join('
');
      if (!data.running) clearInterval(pollingInterval);
    });
  }, 1500);
}
