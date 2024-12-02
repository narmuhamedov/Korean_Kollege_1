document.addEventListener("DOMContentLoaded", function () {
    // Проверяем, есть ли параметр "page" в URL
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('page')) {
        // Прокручиваем к блоку с классом "news"
        const newsBlock = document.querySelector('.news');
        if (newsBlock) {
            newsBlock.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    }
});
