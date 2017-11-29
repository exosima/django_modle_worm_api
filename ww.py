#import sys,os
#sys.path.append('D:\worm\worm')
#import worm.settings
#os.environ['DJANGO_SETTINGS_MODULE']='worm.settings'
#import django
#django.setup()
#from urlworm import models

class get_model() :
    url = '' #项目地址
    pr_name = '' #项目名称
    import sys,os
    sys.path.append(url)
    import worm.settings
    os.environ['DJANGO_SETTINGS_MODULE']=pr_name+'.settings'
    import django
    django.setup()
#    from urlworm import models
    def get_models_object() :
        pass
        #这个获取model对象的函数重写
        #def get_models_object() :
        #import apps.models
        #return apps.models这个是例子

#        return models
    
