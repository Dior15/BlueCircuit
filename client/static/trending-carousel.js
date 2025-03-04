class imageCarousel {
  // Class to represent the image carousel
  trendingMovies = [];
  // Array to hold the currently trending movies to be displayed, should hold 9
  currentDisplay = 0;
  // Indicates the array index of the left most movie currently being displayed by the image carousel
  currentlyRotating = false;
  // Indicates if the carousel is already rotating to stop the button from being pressed during the animation

  constructor() {
    let trendingMoviesString = document.getElementById("trendingCarouselLeft").getHTML();
    this.trendingMovies = trendingMoviesString.split(' ');
    // Retrieving 

    document.getElementById("trendingCarouselLeft").innerHTML = "<img src=\"" + this.trendingMovies[this.currentDisplay % 9] + "\" class=\"carouselImage1\">";
    document.getElementById("trendingCarouselMain").innerHTML = "<img src=\"" + this.trendingMovies[(this.currentDisplay + 1) % 9] + "\" class=\"carouselImage2\">";
    document.getElementById("trendingCarouselRight").innerHTML = "<img src=\"" + this.trendingMovies[(this.currentDisplay + 2) % 9] + "\" class=\"carouselImage3\">";

  }

  async rotateCarousel(val) {
    if (!this.currentlyRotating && document.hasFocus()) { // document.hasFocus() stops weird flickering when tabbing out and back in
      this.currentlyRotating = true;
      // Reassigns the index of the left most element in the carousel to be references when redrawing the carousel using the array of trending movies
        this.currentDisplay = (this.currentDisplay + val) % 9;
    
        if (this.currentDisplay < 0) { 
          // Looping when negative because modulo doesn't work the way I expected it to with negative numbers(?)
          this.currentDisplay = 8;
        }
    
        this.redrawCarousel();

        await this.sleep(600);
        this.currentlyRotating = false;  
        

    }
  }

  async redrawCarousel() {
  // Redraws the movies in the carousel

  // There are 3 transparent divs above the images that will blackout the images when they are transitioning
  // Their opacity will be adjusted to fade in and out over the images
    let opacity = 0;

    let blackout1 = document.getElementById("blackout1");
    let blackout2 = document.getElementById("blackout2");
    let blackout3 = document.getElementById("blackout3");

    // Fading the blackout divs in
    let interval = setInterval(function(){
      opacity += 0.066;
      if (1 <= opacity) {
        opacity = 1;
        clearInterval(interval);
      }
      blackout1.style.opacity = "" + opacity + "";
      blackout2.style.opacity = "" + opacity + "";
      blackout3.style.opacity = "" + opacity + "";
    }, 15); 

    await this.sleep(300);
    // Waiting for the divs to fade in
    // Without this, the following code will run at the same time and cause issues
    
    document.getElementById("trendingCarouselLeft").innerHTML = "<img src=\"" + this.trendingMovies[this.currentDisplay % 9] + "\">";
    document.getElementById("trendingCarouselMain").innerHTML = "<img src=\"" + this.trendingMovies[(this.currentDisplay + 1) % 9] + "\">";
    document.getElementById("trendingCarouselRight").innerHTML = "<img src=\"" + this.trendingMovies[(this.currentDisplay + 2) % 9] + "\">";
    // Setting the new images to appear in the carousel

    // Fading out the blackout divs
    let interval1 = setInterval(function(){
      opacity -= 0.066;
      if (opacity <= 0) {
        opacity = 0;
        clearInterval(interval1);
      }
      blackout1.style.opacity = "" + opacity + "";
      blackout2.style.opacity = "" + opacity + "";
      blackout3.style.opacity = "" + opacity + "";
 
    }, 15); 

  }

  // Automatic carousel spin
  async automaticCarouselSpin() {
    await this.sleep(5000);

    // Automatic scrolling through the image carousel
    let interval = setInterval(function(){
      this.rotateCarousel(1);
    }, 5000); 
  }

  // Used to pause the execution of code in the redrawCarousel method
  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

let trendingCarousel = new imageCarousel();
// Object representing the image carousel

let carouselLeftButton = document.getElementById("carouselLeftButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(-1)}, false);
// Event listener for left button of image carousel

let carouselRightButton = document.getElementById("carouselRightButton").addEventListener("click", function(){trendingCarousel.rotateCarousel(1)}, false);
// Even listener for right button of image carousel

let automaticInterval = setInterval(function(){
  trendingCarousel.rotateCarousel(1);
}, 4000);