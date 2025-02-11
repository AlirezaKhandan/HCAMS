// server.js
const express = require('express');  // Import express module
const app = express();  // Create an express application

const PORT = process.env.PORT || 5000;  // Port for the server

// Middleware for parsing JSON requests
app.use(express.json());

// A simple route that sends "Hello World"
app.get('/', (req, res) => {
  res.send('Hello World');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
