# WhatToDoTomorrow

Изначально, пользователь указывает город, в котором он будет находиться на следующий день и вид активности, которым бы хотел занаяться.

После отправки этой информации, приложение сообщает погоду на следующий день, и проанализуровав ее, либо одобряет выбор активности, либо предлагает свою.

Погода узнается с помощью Open Weather API, алтернативный вид деятельности, если требуется, с помощью The Bored API.

Это приложение призвано помочь не совершать глупые ошибки по типу "поехать кататься на велосипеде в дождь", а также разнообразить жизнь с помощью нетривиальных активностей. Потенциально это будет помогать составлять расписание и на более длительные периоды, не только на 1 день.

# Про реализацию

В начале приложение делвет два запроса в Open Weather API, первый - чтобы узнать локацию города, второй уже для погоды. Если введенного города не существует, то пользователь поппадет на ту же страница только вместо данных будет строка про "Invalid town".

Дальше проимходит анализ активности и погоды: 
1) Активность подразумевает нахождение на улице (это проверяется через поиск глаголов перемещения в строке - да, система иногда ошибается)
2) Погода не слишком хорошая для такого (много осадков, сильный ветер, слишком большая или слишком маленькая температура)

Если оба эти пункта выполнены, то запрос в The Bored API, полученную активность также проверяют, и так происходит до того момента, как не будет найдено занятие, не связанное с нахождением на улице.
