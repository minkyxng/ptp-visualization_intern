// import fs from "fs";
// document.getElementById('logo').onclick = function(){
//   var fs = require('fs');
//   fs.readFile('log/ptplog_slave.txt', function(err, data){
//     if(err) throw err;
//     var array = data.toString().split('\n');
//     for(i in array){
//       console.log(array[i]);
//     }
//   })
// }

function logoclick(){
  // console.log('hi');
    var fs = require('fs');
    var path = '/Users/minkyxng/Documents/GitHub/ptp-visualization/js/log/ptplog_slave';
    fs.readFile(path, 'utf8', function(err, data){
    if(err) throw err;
  //   // var array = data.toString().split('\n');
  //   // for(i in array){
    //   console.log(array[i]);
    console.log(data);
    // }
  })
}

$
