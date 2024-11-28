document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;

            // Закрываем другие элементы
            document.querySelectorAll('.accordion-item').forEach(i => {
                if (i !== item) {
                    i.classList.remove('open');
                    i.querySelector('.accordion-content').style.maxHeight = null;
                }
            });

            // Переключаем текущий элемент
            const content = item.querySelector('.accordion-content');
            if (item.classList.contains('open')) {
                item.classList.remove('open');
                content.style.maxHeight = null;
            } else {
                item.classList.add('open');
                content.style.maxHeight = content.scrollHeight + 'px'; // Автоматическая высота
            }
        });
    });
});
