const express = require("express");
const { Pool } = require("pg");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors({
  origin: "*"  // Барлық origin-дарға рұқсат
}));


// Database connection
const pool = new Pool({
  user: "linx",
  host: "localhost",
  database: "school",
  password: "1234", // өзің қойған пароль
  port: 5432,
});

// 🔹 Тіркелу (қолданушы қосу)
app.post("/register", async (req, res) => {
  try {
    const { firstname, surname, email, password, point1, age, birthday, grade } = req.body;

    if (!firstname || !password) {
      return res.status(400).json({ error: "Атың мен құпиясөз керек!" });
    }

    const hash = await bcrypt.hash(password, 10);

    await pool.query(
      "INSERT INTO users (firstname, surname, email, password, point1, age, birthday, grade) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)",
      [firstname, surname, email, hash, point1, age, birthday, grade]
    );

    res.json({ message: "Қолданушы сәтті тіркелді!" });
  } catch (err) {
    console.error("Register error:", err);
    res.status(500).json({ error: "Server error" });
  }
});

// 🔹 Логин
app.post("/login", async (req, res) => {
  try {
    const { firstname, password } = req.body;

    const result = await pool.query(
      "SELECT * FROM users WHERE firstname = $1",
      [firstname]
    );

    if (result.rows.length === 0) {
      return res.status(400).json({ error: "Қолданушы табылмады" });
    }

    const user = result.rows[0];
    const valid = await bcrypt.compare(password, user.password);

    if (!valid) {
      return res.status(400).json({ error: "Құпиясөз қате" });
    }

    const token = jwt.sign({ id: user.id, firstname: user.firstname, surname: user.surname, email: user.email, point1: user.point1, age: user.age, birthday: user.birthday, grade: user.grade }, "secret", { expiresIn: "1h" });
    res.json({ token });
  } catch (err) {
    console.error("Login error:", err);
    res.status(500).json({ error: "Server error" });
  }
});

// 🔹 Тест сұрақтарын алу
app.get("/questions", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM questions");
    res.json(result.rows);
  } catch (err) {
    console.error("Questions error:", err);
    res.status(500).json({ error: "Server error" });
  }
});

// Token тексеретін функция
function authenticateToken(req, res, next) {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];

  if (!token) return res.status(401).json({ error: "Токен жоқ!" });

  jwt.verify(token, "secret", (err, user) => {
    if (err) return res.status(403).json({ error: "Токен жарамсыз!" });
    req.user = user; // ✅ Дұрыс
    next();
  });
}

// Қорғалған маршрут
app.get("/profile", authenticateToken, (req, res) => {
  res.json({
    user: req.user
  });
});



// 🔹 Серверді іске қосу
app.listen(3000, () => {
  console.log("✅ Server running on http://localhost:3000");
});
