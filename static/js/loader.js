window.addEventListener('DOMContentLoaded', function() {
  var preloaders = document.getElementsByClassName('preloader');
  var contents = document.getElementsByClassName('content');

  for (var i = 0; i < preloaders.length; i++) {
    var preloader = preloaders[i];
    var content = contents[i];
    var image = content.querySelector('img');

    image.onload = createOnLoadHandler(preloader, content);
    image.onerror = createOnLoadHandler(preloader, content);
  }

  function createOnLoadHandler(preloader, content) {
    return function() {
      preloader.classList.add('hide');
      content.classList.remove('hidden');
    };
  }
});
