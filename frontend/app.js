var que = require('que');

function beginApp() {
  var club = new que.App("club", '/static/template');
  club.addView(require('./views/index.js'));
  club.run();
}

beginApp();
