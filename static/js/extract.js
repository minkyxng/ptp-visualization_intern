window.onload=function(){ // 날짜 선택에 max값 제한 둠( 값이 있는 날짜 까지만)
    var today = new Date();
    var yesterday = new Date(today.setDate(today.getDate()-1)).toISOString().substring(0, 10)
    document.getElementById('date').setAttribute('max',yesterday);
}


function checkOnlyOne(element){ //중복check금지
    const checkboxes = document.getElementsByName("nodeid");

    checkboxes.forEach((cb) =>{
        cb.checked = false;
        })

        element.checked = true;
    }


