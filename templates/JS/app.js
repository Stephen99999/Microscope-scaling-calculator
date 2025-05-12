document.getElementById('calcForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const specimenSize = document.getElementById('specimenSize').value;
  const magnification = document.getElementById('magnification').value;

  fetch('/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: `username=${encodeURIComponent(username)}&specimenSize=${encodeURIComponent(specimenSize)}&magnification=${encodeURIComponent(magnification)}`
  })
  .then(response => response.text())
  .then(data => {
    const resultEl = document.getElementById('result');
    resultEl.innerText = data;
    resultEl.style.display = 'block';     // Make sure it's shown
    resultEl.style.opacity = 1;           // If CSS had faded it out
  })
  .catch(err => {
    document.getElementById('result').innerText = "Error: " + err;
  });
});
