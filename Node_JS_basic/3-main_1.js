const countStudents = require('./3-read_file_async');

countStudents("database.csv")
    .then((data) => {
        console.log(data); // Affiche les résultats des étudiants
        console.log("Done!");
    })
    .catch((error) => {
        console.error(error.message); // Affiche le message d'erreur
        console.log("Done!");
    });

console.log("After!");
