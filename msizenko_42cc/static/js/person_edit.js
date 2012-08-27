$(".datepicker").datepicker({ dateFormat: 'yy-mm-dd'});

$(document).ready(function() { 
    var options = {
            target: '#person-data',
            dataType: 'json',
            beforeSubmit: before,
            success: after
        }

    $('#person-data').ajaxForm(options);
        
}) 

function before(formData, jqForm, options) {
    jqForm.find('*').attr('disabled', true);
    $('.errorlist').remove();
    $('#save-person').attr('value', 'Saving...');
    $('#message').text('');        
}

function after(responseText, statusText, xhr, $form){
    var html = '';
    
    $form.find('*').removeAttr('disabled');
    $('#save-person').attr('value', 'Save');
    if (responseText.success) {
        $('#message').text('Changes have been saved');        
    } else {
        errors = responseText.errors
        for (var key in errors) {
            html = '<ul class="errorlist">';
            for(i=errors[key].length; i--;) {
                html += '<li>' + errors[key][i] + '</li>';
            }        
            html += '</ul>';        
            $('#id_' + key).parent().prepend(html);
        }
    }
}

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $("#profile-photo").attr('src', e.target.result);
            }

           reader.readAsDataURL(input.files[0]);
       }
   }
