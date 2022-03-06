Размещено на Heroku: https://fstr2602.herokuapp.com/api/v1/pereval/

Swagger по адресу: https://fstr2602.herokuapp.com/swagger-ui/



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