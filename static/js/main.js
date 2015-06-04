(function() {
    NodeList.prototype.forEach = function(fn) {
        var i;
        for (i = 0; i < this.length; i++) fn(this.item(i));
    };

    var inputs = {
        'indent-char': document.getElementsByName('indent-char'),
        'indent-level': document.getElementsByName('indent-level'),
        'download': document.getElementsByName('download')
    };


    var selectChar = document.getElementById('indent-char'),
        selectLevel = document.getElementById('indent-level'),
        selectDownload = document.getElementById('download');


    var modifyInput = function(inputName) {
        return function(e) {
            var val = this.value;
            inputs[inputName].forEach(function(item) {
                item.value = val;
            });
        };
    };


    selectChar.onchange = modifyInput('indent-char');
    selectLevel.onchange = modifyInput('indent-level');
    selectDownload.onchange = modifyInput('download');
})();
