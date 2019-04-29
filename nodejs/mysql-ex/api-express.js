const express = require('express');
const knex = require('./knex.js')
var app = express();

app.listen(3000)

app.get('/employees', function(req, res) {
    knex.getEmployees(result => res.send(result))
});