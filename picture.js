$.ajax({
    type: 'GET',
    url: './picture.json',
    dataType: 'jsonp',
    jsonCallback: 'picture',
    success: function(data) {
        data.forEach(function(i){
            $document.write('<img src =' + '"' + i.picture + '"' + '>');  
        })
    },
    error:function() {
        console.log("error");
    }
});