const http = require('http');

// Créer un serveur HTTP
const app = http.createServer((req, res) => {
  // Définir le contenu de la réponse
  res.statusCode = 200; // Code de statut HTTP 200 : OK
  res.setHeader('Content-Type', 'text/plain'); // Le contenu est en texte brut
  res.end('Hello Holberton School!'); // Le corps de la réponse
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exporter le serveur pour d'autres fichiers si nécessaire
module.exports = app;
