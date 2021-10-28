$('.answerUpVote').submit(function(e){
    $.post($(this).attr('action'), $(this).serialize(), function(data){
        elements = $('.'+this.url.split('/')[3]);
        ico = elements[0]
        votes = elements[1]

        if(ico.classList.contains('voted')){
            ico.classList.remove('voted');
            votes.innerText = parseInt(votes.innerText) - 1;
        }else {
            ico.classList.add('voted');
            votes.innerText = parseInt(votes.innerText) + 1;
        }
        
    });
    e.preventDefault();
})
$('#bookmark').submit(function(e){
    $.post($(this).attr('action'), $(this).serialize(), function(data){
        ico = $('#bookmarkIcon')[0];
        if(ico.classList.contains('voted')){
            ico.classList.remove('voted');
            $('.alert-danger').show();
            setTimeout(()=>{ $('.alert-danger').slideUp(); }, 2000);
        }else {
            ico.classList.add('voted');
            $('.alert-success').show();
            setTimeout(()=>{ $('.alert-success').slideUp(); }, 2000);
        }
    });
    e.preventDefault();
})

function showAnswerComment(e){

    console.log($('#a'+$(e).parent().attr('id')));
    $(e).parent().css('display', 'none');
    $('#a'+$(e).parent().attr('id')).css('display','');

}

$(window).ready(function() {
    console.log( "ready!" );
    console.log(accepted)
});