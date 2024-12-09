document.addEventListener("DOMContentLoaded", () => {
    // Автоматическое определение системной темы (дополнительный функционал)
    // Если тема не установлена в куках, установить в соответствии с системной
    const userTheme = getCookie('theme');
    if(!userTheme) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefersDark) {
            window.location.href = '/set_theme/dark';
        } else {
            window.location.href = '/set_theme/light';
        }
    }
});

// Функция для получения значения куки
function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([$?*|{}()\[\]\\\/+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}
