Программа нужна для оперативного просмотра состояний электрооборудования. 
    Есть условные единицы, они имеют несколько состояний, которые отображаются в табличной форме чекбоксами. При изменении состояния отмечаем нужный чекбокс. Программа это запоминает и делает лог с датой и временем изменения, и состоянием, которое было и стало. Так же должна быть возможность изменять "Заметки", может через отдельную кнопочку справа.
Запуск программы через ярлык.
В программе должна быть возможность добавлять оборудование самостоятельно, а так же удалять его (если неверно внес данные в наименовании единицы оборудования).
Должна быть разбивка по вкладкам. Например: есть 4 категории оборудования по его месту расположения, они должны быть на разных вкладках. Так же должна быть сводная таблица, в которой будут собраны все отключенные единицы оборудования.
При закрытии программы она уже должна знать все изменения, которые были внесены за текущий сеанс, чтобы исключить потерю информации.
Сделать отдельную вкладку с историей изменений по конкретному присоединению(выбор из списка ключей/доступного оборудования). Значит, лог надо писать в базу данных, чтоб можно было найти изменения по ключу. Пока программа строится с помощью pickle. Вопрос, сколько может весить такая БД за год?
Первая вкладка - отключенное оборудование.

12.12.24  пробую создать что то с SQlite