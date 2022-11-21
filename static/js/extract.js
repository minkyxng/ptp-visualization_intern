window.onload=function(){
    var today = new Date();
    var yesterday = new Date(today.setDate(today.getDate()-1)).toISOString().substring(0, 10)
    document.getElementById('date').setAttribute('max',yesterday);
//    document.getElementById('date').value = new Date(today.setDate(today.getDate()-1)).toISOString().substring(0, 10);
//    document.getElementById('node1').setAttribute('checked',true);
}


function checkOnlyOne(element){
    const checkboxes = document.getElementsByName("nodeid");

    checkboxes.forEach((cb) =>{
        cb.checked = false;
        })

        element.checked = true;
    }


