#!/usr/bin/env python
# coding: utf-8

# In[22]:


#The Moscow Times - Wednesday, October 2, 2002
#The Guardian - Friday, 11.10.13
#Daily News - Thursday, 18 August 1977
from datetime import datetime
first = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
second = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
third = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')


# In[33]:


stream = ['2018-04-02', '2018-02-29', '2018-19-02']
def datecheck(string):
    try:
        date = datetime.strptime(string, '%Y-%m-%d')
        return string, True
    except:
        return string, False
dict(datecheck(list_) for list_ in stream)


# In[96]:


from datetime import timedelta
start_date = '2020-01-05'
end_date = '2020-01-22'
def list_of_date(start_date, end_date):
    list_ = []
    try:
        d_start = datetime.strptime(start_date, '%Y-%m-%d')
        d_end = datetime.strptime(end_date, '%Y-%m-%d')
    except:
        return []
    if (d_end - d_start).days > 0:
        while d_start <= d_end:
            list_.append(datetime.strftime(d_start,'%Y-%m-%d'))
            d_start = d_start + timedelta(days = 1)
    else:
        pass
    return list_
list_of_date(start_date, end_date)  


# In[103]:


DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[DEFAULT_USER_COUNT-2]
#1.list index out of range - ошибка говорит о том, что мы пытаемся обратиться по индексу, которого нет в списке
#2 при втором запуске функция не работает, т.к. в списке остался 1 элемент, значит к списку нельзя обраттиться по индексу [1] 

