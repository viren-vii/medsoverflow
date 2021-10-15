$('#answerUpVote').submit(function(e){
    $.post($(this).attr('action'), $(this).serialize(), function(data){
        
    });
    e.preventDefault();
})