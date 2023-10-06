import pytest
from app.models import Category, Product,Order,OrderItem
from django.urls import reverse
from django.test import Client,TestCase
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(name='test product', price='123', digital=True)
    assert Product.objects.count() == 1
    assert product.name == 'test product'
    assert product.price == '123'
    assert product.digital == True
    assert product is not None

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Test Category", is_sub=False)
    assert category.name == 'Test Category'
    assert category.is_sub == False
    assert category is not None

@pytest.mark.django_db
def test_register_view():
    client = Client()# tạo 1 đối tượng client để thực hiện các yêu cầu http giả lập
    username = 'testuser'
    password = 'testpassword'
    #thực hiện yêu cầu post đến url(register) với những thuộc tính cần đăng ký(username, password1,2)
    response = client.post(reverse('register'), {'username': username, 'password1': password, 'password2': password})
    assert response.status_code == 302 # kểm tra trạng thái http  phản hồi (302: chuyển hướng thành công)
    assert User.objects.filter(username=username).exists()#=>true #lọc kiểm tra trong database có username vừa tạo hay không

@pytest.mark.django_db
def test_login_view():
    client = Client()
    username = 'testuser'
    password = 'testpassword'
    user = User.objects.create_user(username=username, password=password)
    response = client.post(reverse('login'), {'username': username, 'password': password})
    assert response.status_code == 302
    assert client.session['_auth_user_id'] == str(user.id)#kiểm tra phiên đăng nhập của user dựa vào id

@pytest.mark.django_db
def test_logout_view():
    client = Client()
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    assert '_auth_user_id' not in client.session
    
@pytest.mark.django_db
class OrderModelTest(TestCase):
    def setUp(self):        
        self.user = User.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )
        
        self.order = Order.objects.create(
            customer=self.user,
            transaction_id='123'
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            price=10.0
        )
        
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            quantity=2
        )

    def test_get_cart_item(self):
        self.assertEqual(self.order.get_cart_item, 2)

    def test_get_cart_total(self):
        self.assertEqual(self.order.get_cart_total, 20.0)

    def test_order_item_get_total(self):
        self.assertEqual(self.order_item.get_total, 20.0)
     
    # test_order_str_method(self):
    # str(self.order), str(self.order.id)
    


# for TamTran

#đây là Vương

#Vuong vừa mới sửa bài

#đây là Vương
#Tuấn ơi
# Vương đẹp trai hơn Chiến
# Hoàng nè

