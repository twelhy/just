
const map = L.map('map').setView([43.29813788, 68.23864099], 12);
fetch("https://app.alempay.kz/api/service-info/position/?format=json&lang=kz&region=12&route=5A")
  .then(res => res.json())
  .then(data => {
    data.pos.forEach(bus => {
      // Маркер салу
      L.marker([bus.lat, bus.lon]) // координаттар
        .addTo(map) // картаға қосу
        .bindPopup(`Автобус №${bus.num}<br>Бағыт: ${bus.dir}`); // үстіне басқанда ақпарат
    });
  });