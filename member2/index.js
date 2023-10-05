const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const port = 5000;

mongoose.connect('mongodb://localhost/myapp', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;

// Create a User model
const User = mongoose.model('User', {
  username: String,
  password: String,
});

// Middleware
app.use(bodyParser.json());

// Register a new user 
app.post('/register', async (req, res) => {
  try {
    const { username, password } = req.body;

    const user = new User({ username, password });
    await user.save();

    res.json({ message: 'User registered successfully' });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while registering the user' });
  }
});

// Login 
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  const user = await User.findOne({ username });

  if (!user) {
    return res.status(401).json({ error: 'Authentication failed' });
  }

  if (user.password !== password) {
    return res.status(401).json({ error: 'Authentication failed' });
  }

  res.json({ message: 'Login successful' });
});

// List all users (for demonstration purposes)
app.get('/users', async (req, res) => {
  try {
    const users = await User.find({}, { password: 0 }); // Exclude passwords from the response
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while fetching users' });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
