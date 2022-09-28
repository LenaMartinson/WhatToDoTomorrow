To Russian version scroll down.

# WhatToDoTomorrow

This application is designed to help not to make stupid mistakes like "go cycling in the rain", as well as diversify life with the non-trivial activities. Potentially, this will help to make a schedule for longer period, not just for a 1 day.

It uses Open Weather API (to know forecast to the next day) and The Bored API to help to choose activity relevant the weather.

The algorithm of application:

* User types the city of residence and preferred activity
* The app makes request to API, analyze it and approve/disapprove your choice
* If activity is not very suitable, app makes request to another API and give you alternative

Enjoy the app!

# WhatToDoTomorrow

Изначально, пользователь указывает город, в котором он будет находиться на следующий день и вид активности, которым бы хотел заняться.

После отправки этой информации, приложение сообщает погоду на следующий день, и проанализировав ее, либо одобряет выбор активности, либо предлагает свою.

Погода узнается с помощью Open Weather API, альтернативный вид деятельности, если требуется, с помощью The Bored API.

Это приложение призвано помочь не совершать глупые ошибки по типу "поехать кататься на велосипеде в дождь", а также разнообразить жизнь с помощью нетривиальных активностей. Потенциально это будет помогать составлять расписание и на более длительные периоды, не только на 1 день.

# Про реализацию

В начале приложение делает два запроса в Open Weather API, первый - чтобы узнать локацию города, второй уже для погоды. Если введенного города не существует, то пользователь попадет на ту же страница только вместо данных будет строка про "Invalid town".

Дальше происходит анализ активности и погоды: 
1) Активность подразумевает нахождение на улице (это проверяется через поиск глаголов перемещения в строке - да, система иногда ошибается)
2) Погода не слишком хорошая для такого (много осадков, сильный ветер, слишком большая или слишком маленькая температура)

Если оба эти пункта выполнены, то запрос в The Bored API, полученную активность также проверяют, и так происходит до того момента, как не будет найдено занятие, не связанное с нахождением на улице.
