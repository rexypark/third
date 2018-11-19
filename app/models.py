from django.db import models


# Address # 데이터베이스에 테이블로 저장 콜론으로 활용
class Address(models.Model):
    address = models.CharField(max_length=20)

    def __str__(self):  # string값으로 저장
        return self.address


# (PrimaryKey)기본키 >
# (ForeignKey)외래키

class House(models.Model):
    number = models.IntegerField()
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number) + self.address.address  # 101대연동
