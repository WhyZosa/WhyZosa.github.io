from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)

# Текстовые данные резюме на двух языках
resume_data = {
    "ru": {
        "title": "Моё резюме",
        "personal_info": "Личная информация",
        "name": "Иван Иванов",
        "education": "Образование",
        "education_details": "HSE, XXXXXXXXXXX",
        "experience": "Опыт работы / проекты",
        "experience_details": "Разработка веб-приложений на Python и Flask",
        "skills": "Навыки",
        "skills_list": "Python, Flask, HTML, CSS, JavaScript",
        "contact": "Контактная информация",
        "contact_details": "Email: ivan@example.com\nТелефон: +7 (999) 123-45-67",
        "language_label": "Язык",
        "theme_label": "Тема",
        "dark_theme": "Тёмная",
        "light_theme": "Светлая",
        "russian": "Русский",
        "english": "Английский"
    },
    "en": {
        "title": "My Resume",
        "personal_info": "Personal Information",
        "name": "Ivan Ivanov",
        "education": "Education",
        "education_details": "HSE, XXXXXXXXXXX",
        "experience": "Experience / Projects",
        "experience_details": "Web application development with Python and Flask",
        "skills": "Skills",
        "skills_list": "Python, Flask, HTML, CSS, JavaScript",
        "contact": "Contact Information",
        "contact_details": "Email: ivan@example.com\nPhone: +7 (999) 123-45-67",
        "language_label": "Language",
        "theme_label": "Theme",
        "dark_theme": "Dark",
        "light_theme": "Light",
        "russian": "Russian",
        "english": "English"
    }
}


@app.route('/')
def index():
    # Получаем текущий язык из кук
    lang = request.cookies.get('lang', 'ru')
    # Получаем текущую тему из кук
    theme = request.cookies.get('theme', 'light')
    # Передаём данные в шаблон
    return render_template('index.html', data=resume_data[lang], current_lang=lang, current_theme=theme)

@app.route('/set_language/<language>')
def set_language(language):
    resp = make_response()
    resp.set_cookie('lang', language, max_age=60*60*24*30) # 30 дней
    resp.headers['Location'] = '/'
    resp.status_code = 302
    return resp

@app.route('/set_theme/<theme>')
def set_theme(theme):
    resp = make_response()
    resp.set_cookie('theme', theme, max_age=60*60*24*30) # 30 дней
    resp.headers['Location'] = '/'
    resp.status_code = 302
    return resp

if __name__ == '__main__':
    app.run(debug=True)
