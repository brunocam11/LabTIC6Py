var knex = require('knex')({
  client: 'mysql',
  connection: {
    host : 'labticvi2019.cevummruy0nm.us-east-2.rds.amazonaws.com',
    user : 'laboratorio',
    password : 'labtic2019',
    database : 'employees'
  }
});

module.exports.getEmployees = (callback) => knex.select().from('employees').limit(10).then(rows => {
  console.table(rows)
  callback(rows)
})