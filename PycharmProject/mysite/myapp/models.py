from django.db import models

# Create your models here.
'''相当于对数据库表的映射'''
class Stu(models.Model):
    '''定义Stu表对应的Model类'''
    #定义属性：默认主键自增 id字段不可写
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=16)
    age=models.SmallIntegerField()
    sex=models.CharField(max_length=1)
    classid=models.CharField(max_length=8)

    #定义默认输出格式
    def _str_(self):
        return "%d:%s:%d:%S:%S"%(self.id,self.name,self.age,self.sex,self.classid)

    #自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table='stu'#对应数据库表名