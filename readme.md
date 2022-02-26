Размещено на Heroku: https://fstr2602.herokuapp.com/api/v1/pereval/

отправляем на адрес https://fstr2602.herokuapp.com/api/v1/pereval/


{"raw_data": {
        "pereval_id": "12211",
        "beautyTitle": "пер. ",
        "title": "Пхия",
        "other_titles": "Триев",
        "connect": "",
        "user": {"id": "test",
                 "email": "user@email.tld",
                 "phone": "79031234567",
                 "fam": "Пупкин",
                 "name": "Василий",
                 "otc": "Иванович"},
        "coords": {"latitude": "45.3842",
                   "longitude": "7.1525",
                   "height": "1200"},
        "type": "pass",
        "level": {"winter": "",
                  "summer": "1А",
                  "autumn": "1А",
                  "spring": ""}},
"images": {"sedlo": [2, 3],
        "Nord": [1],
       "West": "null",
        "South": [4, 5],
        "East": [6]},
"status": "new"}



Инструкция по публикации на хостинг:
1. В консоле пишем git clone https://github.com/lehakot-create/FSTR.git Hakathon FSTR v2
2. cd Hakathon FSTR v2 (переходим в папку Hakathon FSTR v2)
3. python -m venv venv (создаем виртуальное окружение)
4. cd venv/scripts/activate (активируем виртуальное окружение)
5. cd prj (в консоли переходим в папку prj)
6. pip install -r requirements.txt (устанавливаем зависимости из файла requirements.txt)
7. heroku login (логинимся на хероку)
8. heroku create nameapp (создаем приложение и даем имя nameapp)
9. git add .
10. git commit -m "Diploy"
11. git push heroku main
12. heroku run python manage.py migrate