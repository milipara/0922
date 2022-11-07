from django.shortcuts import render
import random

# Create your views here.
def index(request):
    
    names = ['가' , '나' , '다' , '라']
    name = random.choice(names)
    
    images=[
    'https://picok.co.kr/data/file/wing8657/m15526234805252/img_m15526234805252_800.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5ZwffFs01eXscEMEL9pz29Lmiaar_bS9BMg&usqp=CAU'
    ]
    image = random.choice(images)
    
    dinner_menu = ['감자튀김' , '비빔밥' , '라면' , '치킨']
    dinner = random.choice(dinner_menu)
    
    context = {
        'name' : name,
        'img' : image,
        'dinner' : dinner
    }
# 환영하는 메인 페이지를 보여준다.
    return render(request,'index.html', context)

def welcome(request, name):
    # 사람들이 /welcome/ 이름을 입력하면 환영 인사와 이름을 동시에 보여준다.
    
    context ={
        'name' : name,
        'greetings' : [
            '안녕하세요' , 'hello' , 'こんにちは.' , '你好。'
        ]
    }
    
    return render(request, 'welcome.html', context)