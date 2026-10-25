fetch('/api/health').then(r=>r.json()).then(d=>document.querySelector('#health').textContent=d.status);
