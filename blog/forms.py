from django import forms
from .models import Post


# 폼은 일반폼(Form)과 모델폼(Model Form) 두 종류가 있다.\
# Form (일반 폼) : 화면에 나타날 입력 필드를 직접 필드 정의, 위젯 설정이 필요
# Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성
# PostForm : 만들 폼의 이름(Post라는 Model과 연결되는 폼이다.)
# forms.ModelForm 은 장고에게 이 폼이 ModelForm이라는 것을 알려주는 역할
class PostForm(forms.ModelForm):

    # Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
    class Meta:  # 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요
        model = Post  # 사용할 모델
        fields = ('title', 'text',)  # Post 폼에서 사용할 모델의 속성