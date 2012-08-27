$(document).ready(function() {
    var currrent = 0;
    
    $('input').focus(function(e) {
        current = $(this).val();
    });

    $('input').bind('keypress', function(e) {
        var enter = e.which == 13,
            id = $(this).attr('id'),
            pk = id.substr('id_'.length),
            priority = $(this).val();
        
        if (enter) {
            $.ajax({
                type: 'POST',
                url: 'edit/',
                data: {pk: pk, priority: priority},
            }).error(function(data){
                $(this).val(current);
            });
        }
    });

});
