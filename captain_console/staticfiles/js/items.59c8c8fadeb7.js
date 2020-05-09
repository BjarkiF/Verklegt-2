$(document).ready(function() {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-txt').val();
        $.ajax({
            url: '/items?search_filter' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d =>{
                    return '<div class="item"> \
                        <a href="/items/${d.id}"> \
                            <img class="item-img" src="${d.img}" \
                                 alt="${d.name}"/> \
                            <p class="item-name">${d.name}</p> \
                            <p class="item-price">Verð: ${d.price},-</p> \
                        </a> \
                    </div>'
                });
                $('.items').html(newHtml.join(''));
                $('#search-txt').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    })
});
