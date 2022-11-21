window.onload=function(){
    var today = new Date();
    var yesterday = new Date(today.setDate(today.getDate()-1)).toISOString().substring(0, 10)
    document.getElementById('date').setAttribute('max',yesterday);
}


function checkOnlyOne(element){
    const checkboxes = document.getElementsByName("nodeid");

    checkboxes.forEach((cb) =>{
        cb.checked = false;
        })

        element.checked = true;
    }


