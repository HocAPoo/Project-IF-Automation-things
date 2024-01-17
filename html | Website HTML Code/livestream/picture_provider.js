function showSlides() {
  var delay = 3000;
  var container = document.getElementById('imageContainer');
  function findImage() {
    var image = new Image();
    // Append a timestamp to the image URL to prevent caching
    image.src = '/PiVid1/image.jpg?' + Date.now();
    return image;
  }

  function displayNextImage() {
    var image = findImage();

    image.onerror = function() {
      setTimeout(findImage, 500);
    };

    container.innerHTML = '';
    container.appendChild(image);

    setTimeout(displayNextImage, delay);
  }

  displayNextImage();
}

showSlides();


