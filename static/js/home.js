let currentScrollPosition = 0;
let currentScrollAmount = 320;
const sCont = document.querySelector('.storys-container');
const hScroll = document.querySelector('.horizontal-scroll');

// scroll handle

const btnScrolleft = document.querySelector('#btn-scroll-left');
const btnScrolRight = document.querySelector('#btn-scroll-right');

btnScrolleft.style.opacity = '0';

let maxScroll = -sCont.offsetWidth + hScroll.offsetWidth;

function scrollHorizontally(val) {
    currentScrollPosition += (val * currentScrollAmount);
    if (currentScrollPosition >= 0) {
        currentScrollPosition = 0;
        btnScrolleft.style.opacity = "0";
    } else {
        btnScrolleft.style.opacity = "1";
    }

    if (currentScrollPosition <= maxScroll) {
        currentScrollPosition = maxScroll;
        btnScrolRight.style.opacity = "0";
    } else {
        btnScrolRight.style.opacity = "1";
    }

    sCont.style.left = currentScrollPosition + 'px';
}

// handle comment hiding
function displayComment(id) {
 var comment_id = document.getElementById('${id}');
 if (comment_id.style.display === "none") {
 comment_id.style.display = "block";
 } else {
    comment_id.style.display = "none";
 }
}