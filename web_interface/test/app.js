const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
var data=null;

router.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index.html'));
  //__dirname : It will resolve to your project folder.
});
router.post('/get_data',function(req,res){
  data=req.query;
  console.log(data);
  res.send("done")
});
router.get('/get_data2',function(req,res){
	res.setHeader('Content-Type','application/json');
	res.end(JSON.stringify(data));
  //console.log(data);
});

app.use('/', router);

app.listen(process.env.port || 7002);

console.log('Running at Port 7002');