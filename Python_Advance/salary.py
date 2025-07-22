#encoding=utf-8
'''
本模块用于计算员工薪资
'''

company = 'ByteDance'

def yearSalary(monthSalary):
    '''
    根据传入的月薪计算年薪
    param: 
        monthSalary:月薪
    return:
        年薪
    '''
    return monthSalary*12


def daySalary(monthSalary):
   
    '''   
    根据传入的月薪计算日薪(按照一个月22.5天计算)
    param: 
        monthSalary:月薪
    return:
        日薪
    '''
    pass


if __name__ =='__main__':
    print(yearSalary(3000))
    
 