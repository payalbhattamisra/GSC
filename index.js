
const registerButton = document.getElementById('registerButton');

// Add a click event listener to the register button
registerButton.addEventListener('click', function() {
    // Redirect to the registration page
    window.location.href = 'registration.html';
});
var express = require("express");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");

const app = express();

app.use(bodyParser.json());
app.use(express.static('public'));
app.use(bodyParser.urlencoded({
  extended: true
}));

mongoose.connect('mongodb://localhost:27017/mydb', { useNewUrlParser: true, useUnifiedTopology: true });

var db = mongoose.connection;

db.on('error', (err) => {
  console.error("Error in connecting to Database:", err);
});

db.once('open', () => {
  console.log("Connected to Database");
});

app.post("/signup", async (req, res) => {
  try {
    var Name = req.body.Name;
    var City = req.body.City;
    var Location = req.body.Location;
    var Type = req.body.Type;
    var Quantity = req.body.Quantity;
    var Frequency = req.body.Frequency;
    var Price = req.body.Price;

    var data = {
      "Name": Name,
      "City": City,
      "Type": Type,
      "Quantity": Quantity,
      "Frequency": Frequency,
      "Price": Price
    };

    await db.collection('users').insertOne(data);
    console.log("Record Inserted Successfully");
  } catch (err) {
    console.error("Error inserting record:", err);
    res.status(500).send("Internal Server Error");
  }
});

app.get("/", (req, res) => {
  res.set({
    "Allow-access-Allow-Origin": '*'
  });
  return res.redirect('index.html');
}).listen(3000);

console.log("Listening on PORT 3000");
