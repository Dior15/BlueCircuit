ratingSlider = document.getElementById("ratingInput");
sliderValue = document.getElementById("sliderValue");
ratingSlider.addEventListener("input", function(){sliderValue.innerHTML=ratingSlider.value}, false);

sliderValue.innerHTML=ratingSlider.value