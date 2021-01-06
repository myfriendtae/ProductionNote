$(document).ready(function(){
    $('a').click(function(e){
        e.preventDefault();
        console.log('clicked')
        var selected =  $(this).attr('href')
        console.log(selected)
    })
})

