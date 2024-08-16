$(document).ready(function () {
  var baseUrl = window.location.origin;
  var deleteBtn = $('.delete-btn');
  var searchBtn = $('#search-btn');
  var searchForm = $('#search-form');
  var filter = $('#filter');

  $(deleteBtn).on('click', function (e) {
    e.preventDefault();

    var delLink = $(this).attr('href');
    var result = confirm("Tem certeza que deseja excluir esta tarefa?");

    if (result) {
      window.location.href = delLink
    }
  })

  $(searchBtn).on('click', function () {
    searchForm.submit()
  })

  $(filter).change(function () {
    // window.location.href = baseUrl + '?filter=' + $(this).val()
    var filter = $(this).val();
    console.log({ filter });
    console.log(window.location.href);
    if (filter === '') {
      window.location.href = baseUrl
    } else {
      window.location.href = baseUrl + '?filter=' + filter
    }
  })
})