function loadData() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/movies',
        type: 'GET',
        success: function (res) {
            console.log('data from server: ', res);
            displayMovies(res.objects)
        },
        error: function (error) {
            console.error("Error On Get", error);
        }
    });
}

function displayMovies(list) {
    var table = $("#tblCatalog > tbody");
    console.log(table)
    for (var i = 0; i < list.length; i++) {
        var movie = list[i];
        var row =
            `<tr>
        <td>${movie.id}</td>
        <td>${movie.title}</td>
        <td>${movie.release_year}</td>
        <td>${movie.price}</td>
        </tr>
        `;
        console.log(row);
        table.append(row);
    }
}

function init() {
    loadData();
}

window.onload = init()