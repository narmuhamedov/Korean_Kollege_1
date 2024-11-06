let bcgHead = document.getElementById('bcg_head')


window.addEventListener('scroll', function(){
    if(scrollY == 0){
        bcgHead.classList.remove("blue");
        bcgHead.classList.add("black");
        
        
    }
    else{
        bcgHead.classList.remove("black");
        bcgHead.classList.add("blue");
    }
})



// BURGER
document.addEventListener('DOMContentLoaded', () => {
const burger = document.getElementById("burger");
const cross = document.getElementById("cross");
const menu = document.getElementById("menu");

function toggleMenu(){
    burger.classList.toggle("d-none") ;
    cross.classList.toggle("d-block");
    menu.classList.toggle("d-flex")
}

burger.addEventListener("click", toggleMenu)
cross.addEventListener("click", toggleMenu)


function closeMenuIfClickedOutside(event) {
    // Проверяем, клик был ли вне меню и вне кнопок
    if (!menu.contains(event.target) && !burger.contains(event.target) && !cross.contains(event.target)) {
        // Если меню открыто, то закрываем его
        if (menu.classList.contains("d-flex")) {
            toggleMenu();
        }
    }
}


document.addEventListener("click", closeMenuIfClickedOutside);
document.addEventListener("scroll", closeMenuIfClickedOutside);
})