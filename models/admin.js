var mongoose = require("mongoose");

var adminSchema = new mongoose.Schema({
  employee_id: {
    type: String,
    required: true,
  },
  firstName: {
    type: String,
  },
  middleName: {
    type: String,
  },
  lastName: {
    type: String,
  },
  contactNumber: {
    type: Number,
    min: 1111111111,
    max: 9999999999,
  },
  email: {
    type: String,
    required: true,
    min: 7,
    max: 255,
  },
  password: {
    type: String,
    required: true,
    max: 1024,
    min: 4,
  },
  autherisation_level: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model("CwcEmployee", cwcEmployeeSchema);
