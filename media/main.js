$(document).ready(function () {
  $(".next").click(function () {
    var currentSlide = $(".show-slider");
    var nextSlide = currentSlide.next();

    if (nextSlide.length == 0) {
      nextSlide = $(".home-slider div:first");
    }
    currentSlide.removeClass("show-slider").addClass("hide-slider");
    nextSlide.addClass("show-slider").removeClass("hide-slider");
  });
  $(".prev").click(function () {
    var currentSlide = $(".show-slider");
    var prevSlide = currentSlide.prev();

    if (prevSlide.length == 0) {
      prevSlide = $(".home-slider div:last");
    }
    prevSlide.addClass("show-slider").removeClass("hide-slider");
    currentSlide.removeClass("show-slider").addClass("hide-slider");
  });
});
