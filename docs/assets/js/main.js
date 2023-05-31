$(function () {

  function initSearchBox(searchData) {

    const pages = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.obj.whitespace('title'),
      queryTokenizer: Bloodhound.tokenizers.whitespace,

      local: eval(searchData),
    });

    $('#search-box').typeahead({
      minLength: 0,
      highlight: true
    }, {
      name: 'pages',
      display: 'title',
      source: pages,
    });

    $('#search-box').bind('typeahead:select', function (ev, suggestion) {
      window.location.href = suggestion.url;
    });
  }

  function styleContentToMD() {
    $('#markdown-content-container table').addClass('table');
    $('#markdown-content-container img').addClass('img-responsive');
  }


  fetch(baseurl + '/search.json')
    .then((r) => {
      if (r.ok) {
        return r.text()
      }
    })
    .then(resp => initSearchBox(resp))


  styleContentToMD();
});
