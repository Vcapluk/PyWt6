#какие такие переменные сюда можно поместить?


'''
    а вот уже и придумал. Или просто приснилось. Читал про SQLite, понял, что в БД будет много много строчек(64 цифры в id-шнике). в мегатаблице. 
    Но все они (строки) должны подчиняться какому то шаблону. 
    и вот этот шаблон сюда и надо складывать. Потому что при несовпадении запроса содержимого все валится в ошибку. 
    Можно этому шаблону задать дефолтные значения, и тогда в недостающие столбики будут вставляться дефолтные значения. 
    И тогда оно будет заполняться NULL(допустим)(а оно нам и не важно значит, если мы не передали это в запрос на запись...) 
    Может надо будет добавить какие то "флаги" для быстрого поиска...(а надо ли? 2 000 000 записей за 15 секунд. Мне такая нагрузка и не нужна, даже близко...)
    
    дошёл до транзакций... Может фиксировать не более 50 транзакций в секунду. Очень неплохо, мышка так клацать не успевает)
    
'''

# очевидно, что здесь надо прописать еще и пути для сосздания БД. 
    # После написания программы, ее надо будет запаковать в *.exe. Значит и БД должна быть внутри этого экзешника, чтоб БД случайно не удалилась...

