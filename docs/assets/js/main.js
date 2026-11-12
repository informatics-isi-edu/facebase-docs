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


  // "On this page" sidebar: list the page's h2 headings and highlight the
  // one being read. The layout only adds #page-toc when the page qualifies
  // (3+ h2 headings and no `toc: false`), so this does nothing elsewhere.
  function buildPageToc() {
    var $toc = $('#page-toc');
    if (!$toc.length) return;

    var $list = $toc.find('ul');
    $('#markdown-content-container h2[id]').each(function () {
      var $link = $('<a>').attr('href', '#' + this.id).text($(this).text());
      $list.append($('<li>').append($link));
    });

    // Offset is a bit more than the fixed top navbar's height.
    $('body').scrollspy({ target: '#page-toc', offset: 110 });
  }


  fetch(baseurl + '/search.json')
    .then((r) => {
      if (r.ok) {
        return r.text()
      }
    })
    .then(resp => initSearchBox(resp))


  styleContentToMD();
  buildPageToc();
});
