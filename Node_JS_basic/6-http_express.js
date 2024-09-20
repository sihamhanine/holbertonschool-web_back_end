const express = require('express');
const app = express();

// Route for the root endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Listen on port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Export app for reuse
module.exports = app;
