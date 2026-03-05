function changeImage(){
    let dropdown = document.getElementById("school");
    let img = document.getElementById("schoolImage");

    img.src = dropdown.value;
}