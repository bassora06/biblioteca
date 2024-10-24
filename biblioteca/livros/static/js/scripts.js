$(document).ready(function() {

    var deleteBtn = $('.delete-btn'); 
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // o cifrão serve para selecionar algo

    $(deleteBtn).on('click', function(e){

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer mesmo deletar esse livro?');

        if(result){
            window.location.href = delLink;
        }


    });

    $(searchBtn).on('click', function(){

        searchForm.submit();

    })

});