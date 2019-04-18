const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
var bodyParser = require('body-parser');
var data=null;
//app.use(bodyParser.json());
//app.use(bodyParser.urlencoded({ extended: true }));

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));

router.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index2.html'));
  //__dirname : It will resolve to your project folder.
});
router.post('/get_data',function(req,res){
  data=req.body;
  console.log(data);
  res.send("done")
});
router.get('/get_data2',function(req,res){
	res.setHeader('Content-Type','application/json');
	res.end(JSON.stringify(data));
  //console.log(data);
});

app.use('/', router);

let port = process.env.PORT;
if (port == null || port == "") {
  port = 8000;
}
app.listen(port);

console.log('Running at Port ' + port);