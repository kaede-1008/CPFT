$.ajax({
    type: 'GET',
    url: './picture.json',
    dataType: 'json',
    data: {name: 'picture'},
    success: function(data) {
        var dataArray = data;
        $.each(dataArray, function(i){
          $document.write('<img src =' + '"' + dataArray[i].picture + '"' + '/>');  
        })
    },
    error:function() {
        console.log("error");
    }
});