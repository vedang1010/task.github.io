var info = document.getElementById("information_section");
var home = document.getElementById("home");
var details = document.getElementById("details");
var str = document.getElementById("structure");
var faq = document.getElementById("questions");
var timeline = document.getElementById("timeline");
var btns=document.getElementsByClassName("btn");
var sec=document.getElementsByClassName("sec")

function toggleTl(targetDiv) {
       
    switch (targetDiv) {
        case "tlBtn":  
            info.style.display="none";
            timeline.style.display = "flex";
            break;
        case "faqBtn":
            info.style.display="flex";
            for(var i=0; i<btns.length; i++){
                sec[i].style.display="none";
            } 
            faq.style.display = "flex";
            break;
        case "homeBtn":
            info.style.display="flex";
            for(var i=0; i<btns.length; i++){
                sec[i].style.display="none";
            } 
            home.style.display = "flex";
            break;
        case "detailsBtn":
            info.style.display="flex";
            for(var i=0; i<btns.length; i++){
                sec[i].style.display="none";
            } 
            details.style.display = "flex";
            break;
        case "strBtn":
           
            info.style.display="flex";
            for(var i=0; i<btns.length; i++){
                sec[i].style.display="none";
            } 
            str.style.display = "flex";
            break;
        

        default:
            break;
    }


}

const register_button = document.getElementById(' reg_button');
    
        register_button.addEventListener('mouseover',function(e){
            // let x= e.clientX - e.target.offsetLeft;
            // let y= e.clientY - e.target.offsetTop;

            let ripples = document.createElement('span');
            // ripples.style.left= x + 'px';
            // ripples.style.top= y + 'px';
            this.appendChild(ripples);
            this.style.overflow="hidden";

            setTimeout(() => {
                ripples.remove()},1000);
            
        
    })

const buttons = document.querySelectorAll('.faq');

buttons.forEach((button) =>{
    button.addEventListener('click', () =>{
        button.classList.toggle('active')

    })
})



var items = document.querySelectorAll(".timeline li");

function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        // rect.top >= 0 &&
        // rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
        if (isElementInViewport(items[i])) {
            if (!items[i].classList.contains("in-view")) {
                items[i].classList.add("in-view");
            }
        }
        else if (items[i].classList.contains("in-view")) {
            items[i].classList.remove("in-view");
        }
    }
}

window.addEventListener("load", callbackFunc);
window.addEventListener("scroll", callbackFunc);

const list = document.querySelectorAll(".list");
    
function activeLink() {
  list.forEach((item) => item.classList.remove("active"));
  this.classList.add("active");
}
list.forEach((item) => item.addEventListener("click", activeLink));
