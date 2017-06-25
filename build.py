from operator import itemgetter


def solution_asc(dic):
    '''
    Enter your code here
    '''
    dic1 = list(dic.items())
    lst_asc = sorted(dic1,key=itemgetter(0))
    return lst_asc


def solution_desc(dic):
    '''
    Enter your code here
    '''
    dic1 = list(dic.items())
    lst_dsc = sorted(dic1,key=itemgetter(0),reverse=True)
    return lst_dsc
