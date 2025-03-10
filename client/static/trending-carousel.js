class imageCarousel {
  // Class to represent the image carousel
  trendingMovies = [];
  // Array to hold the currently trending movies to be displayed, should hold 9
  currentDisplay = 0;
  // Indicates the array index of the left most movie currently being displayed by the image carousel
  currentlyRotating = false;
  // Indicates if the carousel is already rotating to stop the button from being pressed during the animation
  trendingCarousel = null;

  constructor() {
    let trendingMoviesString = document.getElementById("trend1").getHTML();
    this.trendingMovies = trendingMoviesString.split(' ');
    this.trendingCarousel = document.getElementById("trendingCarousel");
    // Retrieving links to images of the most popular movies

    // Assigning each movie into a div within the image carousel
    document.getElementById("trend1").innerHTML = "<img src=\"" + this.trendingMovies[0] + "\" class=\"carouselImage1\">";
    document.getElementById("trend2").innerHTML = "<img src=\"" + this.trendingMovies[1] + "\" class=\"carouselImage2\">";
    document.getElementById("trend3").innerHTML = "<img src=\"" + this.trendingMovies[2] + "\" class=\"carouselImage3\">";
    document.getElementById("trend4").innerHTML = "<img src=\"" + this.trendingMovies[3] + "\" class=\"carouselImage1\">";
    document.getElementById("trend5").innerHTML = "<img src=\"" + this.trendingMovies[4] + "\" class=\"carouselImage2\">";
    document.getElementById("trend6").innerHTML = "<img src=\"" + this.trendingMovies[5] + "\" class=\"carouselImage3\">";    
    document.getElementById("trend7").innerHTML = "<img src=\"" + this.trendingMovies[6] + "\" class=\"carouselImage1\">";
    document.getElementById("trend8").innerHTML = "<img src=\"" + this.trendingMovies[7] + "\" class=\"carouselImage2\">";
    document.getElementById("trend9").innerHTML = "<img src=\"" + this.trendingMovies[8] + "\" class=\"carouselImage3\">";

  }

  async rotateCarousel(direction) {
    // Rotates the carousel based on the input direction, the direction is a value -1 or 1 specified by which button/method calls the rotateCarousel method
    if (!this.currentlyRotating && document.hasFocus()) { // document.hasFocus() stops weird flickering when tabbing out and back in
      this.currentlyRotating = true; // Prevents from this function running again while the animation is still running
      this.currentDisplay += direction;

      if (this.currentDisplay < 0) { // When the image carousel wants to go left but is at left edge
        this.currentDisplay = 6;
        this.trendingCarousel.scrollLeft += 1000000;
      } else if (6 < this.currentDisplay) { // When the image carousel wants to go right but is at right edge
        this.currentDisplay = 0;
        this.trendingCarousel.scrollLeft -= 1000000;
      } else { // When the image carousel is at neither edge
        this.trendingCarousel.scrollLeft += Math.ceil(direction * (parseFloat(getComputedStyle(document.getElementById("trend2")).marginLeft.replace("px", "")) * 2 + parseFloat(getComputedStyle(document.getElementById("trend2")).width.replace("px", ""))));
      }
      

      await this.sleep(350); // Waits 350ms before setting currently rotating to false to give time for the animation to finish before allowing the carousel to begin rotating again

      this.currentlyRotating = false;  
    }
  }

  // Used to pause the execution of code in the rotateCarousel method
  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

let trendingCarousel = new imageCarousel();
// Object representing the image carousel

let carouselLeftButton = document.getElementById("carouselLeftButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(-1)}, false);
// Event listener for left button of image carousel

let carouselRightButton = document.getElementById("carouselRightButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(1)}, false);
// Event listener for right button of image carousel

let automaticInterval = setInterval(function(){trendingCarousel.rotateCarousel(1);}, 4000);
//Automatically spinning the carousel every 4 seconds
