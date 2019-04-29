const mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'labticvi2019.cevummruy0nm.us-east-2.rds.amazonaws.com',
  user     : 'laboratorio',
  password : 'labtic2019',
  database : 'employees'
});

connection.connect();

connection.query('SELECT * FROM employees', function (error, result) {
  if (error) throw error;
  console.table(result);
});

connection.end();