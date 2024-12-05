
        document.querySelectorAll('.accordion-header').forEach(header => {
            header.addEventListener('click', () => {
                const activeHeader = document.querySelector('.accordion-header.active');
                if (activeHeader && activeHeader !== header) {
                    activeHeader.classList.remove('active');
                    activeHeader.nextElementSibling.style.display = 'none';
                }
                header.classList.toggle('active');
                const content = header.nextElementSibling;
                if (header.classList.contains('active')) {
                    content.style.display = 'block';
                } else {
                    content.style.display = 'none';
                }
            });
        });