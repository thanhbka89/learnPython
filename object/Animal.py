"""
Trong đó:

Dòng 3: Phương thức __init__ có chức năng như một constructor trong C++, phương thức này sẽ tự động được gọi khi 1 đối tượng được tạo ra. Phương thức này có thể có hoặc không các tham số, tham số đầu tiên bắt buộc phải là self.
Dòng 4, 5: Các thuộc tính trong lớp bắt buộc phải được truy xuất thông qua tham số self, các thuộc tính sẽ được tạo ra khi được gán lần đầu tiên.
Dòng 6, 8: Khai báo một member function. Tham số đầu tiên trong member function luôn self.

Lưu ý:
Không thể khai báo 2 phương thức __init__ trong cùng 1 class.
Có thể hiểu self như là con trỏ this trong C++, nó dùng để trỏ đến chính đối tượng đang được thao tác.
"""

class Animal:
	def __init__(self, genus, age):
		self.genus = genus
		self.age = age
	def foot(self):
		print ("Gobble")
	def say(self):
		pass

#Tao doi tuong
dog = Animal('Dog', 2)
print(dir(dog))
print(dog.genus)
print(dog.age)
print(dog.foot())

if (not (hasattr(dog, 'name'))):
    setattr(dog, 'name', 'Rex')

print("Name: ", dog.name)
print(type(dog))

"""
Luu y:
Trong Python các thuộc tính, phương thức của lớp chỉ tồn tại ở dạng private và public và chúng được phân biệt dựa theo tên.

Kiểu private: Tên được bắt đầu bằng 2 dấu gạch dưới "__" và kết thúc tối đa là 1 dấu gạch dưới. (Ví dụ: __abc, __xyz_, ...)
Kiểu public: Tất cả các tên không phải tên của kiểu private và đúng quy tắc đều thuộc kiểu public.
"""
#Ke thua
class Duck(Animal):
    def __init__(self):
        Animal.__init__(self, 'Duck', 10)

    def say(self):
        print("Quack quack!")

#Tao doi tuong
duck = Duck()
print(duck.genus)
print(duck.say())

#Duck Typing : Ở ví dụ trên tôi thực hiên viết hàm quackquack với mong muốn truyền vào tham số vào là một đối tượng kiểu Duck, tuy nhiên tôi có thể dùng nó với một đối tượng kiểu Person.
class Person:
    def say(self):
        print("Hello STDIO!")


def quackquack(duck):
    duck.say()

person = Person()
quackquack(person)
quackquack(duck)
