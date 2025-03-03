class imageCarousel {
  // Class to represent the image carousel
  trendingMovies = [];
  // Array to hold the currently trending movies to be displayed, should hold 9
  currentDisplay = 0;
  // Indicates the array index of the left most movie currently being displayed by the image carousel

  constructor() {
    // Get 9 movies to be displayed on the image carousel
    for (let i = 0; i < 9; i++) {
      this.trendingMovies.push("Movie Title " + i);
    }

    // Display the first 3 movies on the image carousel's panels
    this.drawCarousel();
  }

  rotateCarousel(val) {
  // Reassigns the index of the left most element in the carousel to be references when redrawing the carousel using the array of trending movies
    this.currentDisplay = (this.currentDisplay + val) % 9;

    if (this.currentDisplay < 0) { 
      // Looping when negative because modulo doesn't work the way I expected it to with negative numbers(?)
      this.currentDisplay = 8;
    }

    this.drawCarousel();
  }

  drawCarousel() {
  // Redraws the movies in the carousel
    document.getElementById("trendingCarouselLeft").innerHTML = this.trendingMovies[this.currentDisplay % 9];
    document.getElementById("trendingCarouselMain").innerHTML = this.trendingMovies[(this.currentDisplay + 1) % 9];
    document.getElementById("trendingCarouselRight").innerHTML = this.trendingMovies[(this.currentDisplay + 2) % 9];
  }

}

let trendingCarousel = new imageCarousel();
// Object representing the image carousel

let carouselLeftButton = document.getElementById("carouselLeftButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(-1)}, false);
// Event listener for left button of image carousel

let carouselRightButton = document.getElementById("carouselRightButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(1)}, false);
// Even listener for right button of image carousel