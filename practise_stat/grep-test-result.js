class TestRow {
    constructor(){
        this.qNo = '';
        this.objective = '';
        this.isCorrect = '';
        this.qId = '';
    }    
}
var keyword = "GNPDS1RBIE";
var table = document.getElementsByClassName(keyword)[0];
var tbody = document.getElementsByClassName(keyword)[0].getElementsByTagName("tbody")[0];
var rowCnt = tbody.childElementCount;
var testResult = [];

for(let i = 0; i < rowCnt; i++){
    var testRow = new TestRow();
    testRow.qNo = tbody.childNodes[i].childNodes[0].innerText;
    testRow.objective = tbody.childNodes[i].childNodes[3].innerText;
    testRow.isCorrect = tbody.childNodes[i].childNodes[2].className.includes('IN') ? false : true;
    testRow.qId = tbody.childNodes[i].childNodes[5].innerText;
    testResult[i] = testRow;
}

console.log(testResult);
