const express = require('express');
const fs = require('fs');

const app = express();
const port = 8000;

app.get('/data/:id', (req, res) => {
    const id = parseInt(req.params.id); // ID-ны санға айналдырамыз
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send("Error reading file");
        } else {
            const jsonData = JSON.parse(data);
            const item = jsonData.find(d => d.id === id); // Сан ретінде салыстырамыз
            if (item) {
                res.json(item);
            } else {
                res.status(404).send("Item not found");
            }
        }
    });
});

app.get('/data', (req, res) => {
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send("Error reading file");
        } else {
            const jsonData = JSON.parse(data);
            res.json(jsonData);
        }
    });
});

app.post('/data', express.json(), (req, res) => {
    const newItem = req.body;
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send("Error reading file");
        } else {
            const jsonData = JSON.parse(data);
            newItem.id = jsonData.length ? Math.max(...jsonData.map(d => d.id)) + 1 : 1; // ID-ны автоматты түрде тағайындаймыз
            jsonData.push(newItem);
            fs.writeFile('data.json', JSON.stringify(jsonData, null, 2), (err) => {
                if (err) {
                    res.status(500).send("Error writing file");
                } else {
                    res.status(201).json(newItem);
                }
            });
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://10.9.8.41:${port}`);
});