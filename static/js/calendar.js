$(document).ready(function(){
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    var date = yyyy + '-' + mm + '-' + dd;
    // console.log(date)
    get_forms(date);

    $('td.datepicker').click(function(e) {
        e.preventDefault();
        var selected = $(this).closest('td')
        $('td').removeClass('selected')
        selected.toggleClass('selected')
        get_forms(selected.attr('value'))
        // console.log(selected.attr('value'))
    })

    function get_forms(date) {
        $.ajax({
            type: 'GET',
            url: "groups/",
            data: {"date": date},
            success: function(res) {
                $('#groups').html(res);
                $('#files').empty();
            },
            error: function(res) {
                console.log('ajax group GET error')
            }
        })
    }
})