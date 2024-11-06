# Настройки конфигурации Jazzmin Admin
JAZZMIN_SETTINGS = {
    # Настройки заголовка окна
    "site_title": "KKC",  # Заголовок окна
    "site_header": "KKC_ADMINISTRATION",  # Заголовок на экране входа
    "site_brand": "KKC_ADMINISTRATION",  # Заголовок бренда
    "site_logo": None,  # Логотип для сайта (вверху слева)
    "login_logo": None,  # Логотип для формы входа
    "login_logo_dark": None,  # Логотип для формы входа в темной теме
    "site_logo_classes": "img-circle",  # CSS классы для логотипа
    "site_icon": None,  # Значок сайта
    "welcome_sign": "Добро пожаловать в ПУ сайта",  # Приветственный текст на экране входа
    "copyright": "Acme Library Ltd",  # Текст авторских прав внизу страницы

    # Настройки модели поиска
    "search_model": ["auth.User", "auth.Group"],  # Модели для поиска в строке поиска
    "user_avatar": None,  # Поле для аватара пользователя
    "custom_css": "css/custom_admin.css",  # Путь к пользовательскому CSS

    ############
    # Верхнее меню #
    ############
    "topmenu_links": [
        {
            "name": "Главная",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },  # Ссылка на главную страницу
        {"model": "auth.User"},  # Ссылка на модель пользователя
        {"app": "books"},  # Выпадающее меню приложений книг
    ],

    #############
    # Меню пользователя #
    #############
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True
        },  # Ссылка на поддержку
        {"model": "auth.user"}  # Ссылка на модель пользователя в меню пользователя
    ],

    #############
    # Боковое меню #
    #############
    "show_sidebar": True,  # Показать боковое меню
    "navigation_expanded": True,  # Авторазвернуть меню
    "hide_apps": [],  # Приложения для скрытия в боковом меню
    "hide_models": [],  # Модели для скрытия в боковом меню
    "order_with_respect_to": [
        "auth",
        "books",
        "books.author",
        "books.book"
    ],  # Порядок бокового меню
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",  # Иконка для приложения auth
        "auth.user": "fas fa-user",  # Иконка для модели пользователя
        "auth.Group": "fas fa-users",  # Иконка для группы пользователей
    },
    "default_icon_parents": "fas fa-chevron-circle-right",  # Иконка по умолчанию для родительских элементов
    "default_icon_children": "fas fa-circle",  # Иконка по умолчанию для дочерних элементов

    #################
    # Связанная модалка #
    #################
    "related_modal_active": False,  # Использовать модалки вместо всплывающих окон

    #############
    # Настройки UI #
    #############
    "custom_css": None,  # Относительные пути к пользовательскому CSS
    "custom_js": None,  # Относительные пути к пользовательскому JS
    "use_google_fonts_cdn": True,  # Подключить Google Fonts
    "show_ui_builder": True,  # Показать настраиваемый интерфейс в боковом меню

    ###############
    # Изменить вид #
    ###############
    "changeform_format": "horizontal_tabs",  # Формат изменения вида
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },  # Переопределения для конкретных моделей
    "language_chooser": False,  # Добавить выпадающий список языков
}

# Настройки UI Jazzmin
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,  # Маленький текст на панели навигации
    "footer_small_text": False,  # Маленький текст внизу страницы
    "body_small_text": True,  # Маленький текст в теле
    "brand_small_text": False,  # Маленький текст бренда
    "brand_colour": False,  # Цвет бренда
    "accent": "accent-secondary",  # Изменен на серый акцент
    "navbar": "navbar-light",  # Светлая панель навигации
    "no_navbar_border": True,  # Без границы для панели навигации
    "navbar_fixed": False,  # Зафиксированная панель навигации
    "layout_boxed": False,  # Коробочная компоновка
    "footer_fixed": True,  # Зафиксированное нижнее меню
    "sidebar_fixed": False,  # Зафиксированная боковая панель
    "sidebar": "sidebar-light",  # Светлая боковая панель
    "sidebar_nav_small_text": False,  # Маленький текст в боковой навигации
    "sidebar_disable_expand": False,  # Отключить развертывание боковой панели
    "sidebar_nav_child_indent": False,  # Без отступов для дочерних элементов
    "sidebar_nav_compact_style": False,  # Компактный стиль для боковой навигации
    "sidebar_nav_legacy_style": False,  # Старый стиль для боковой навигации
    "sidebar_nav_flat_style": False,  # Плоский стиль для боковой навигации
    "theme": "light",  # Настройка темы на светлую
    "dark_mode_theme": "slate",  # Тема в темном режиме
    "button_classes": {
        "primary": "btn-secondary",  # Класс для кнопок первичного цвета на сером фоне
        "secondary": "btn-light",  # Класс для кнопок вторичного цвета
        "info": "btn-info",  # Класс для информационных кнопок
        "warning": "btn-warning",  # Класс для кнопок предупреждения
        "danger": "btn-danger",  # Класс для кнопок опасности
        "success": "btn-success"  # Класс для кнопок успеха
    },
    "actions_sticky_top": False  # Липкие действия в верхней части
}
