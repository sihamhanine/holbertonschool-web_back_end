const fs = require('fs');

function countStudents(path) {
  try {
    // Lire le fichier de manière synchrone
    const data = fs.readFileSync(path, 'utf8');
    
    // Diviser les données par lignes
    const lines = data.split('\n');
    
    // Retirer les lignes vides
    const validLines = lines.filter((line) => line.trim() !== '');

    if (validLines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Afficher le nombre total d'étudiants (sans compter l'en-tête)
    console.log(`Number of students: ${validLines.length - 1}`);

    // Créer un objet pour stocker les étudiants par champ d'étude
    const fields = {};

    // Boucler à partir de la deuxième ligne pour ignorer l'en-tête
    for (let i = 1; i < validLines.length; i++) {
      const studentInfo = validLines[i].split(',');

      if (studentInfo.length >= 4) {
        const firstName = studentInfo[0];
        const field = studentInfo[3];

        // Ajouter les étudiants à leur champ correspondant
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    // Afficher le nombre d'étudiants par champ et leurs prénoms
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
