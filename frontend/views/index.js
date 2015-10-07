var que = require('que');

var indexView = new que.View("index");

indexView.route("/", function () {
  $('#main-content').html(this.render('index.html'));
});

module.exports = indexView

