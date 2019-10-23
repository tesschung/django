from django.contrib.auth.forms import UserChangeForm, UserCreationForm # 원래 UserChangeForm, UserCreationForm을 불러와서 아래에서 커스터마이징한다.
from django.contrib.auth import get_user_model # 현재 활성화(active)된 user model을 return 한다


# 장고에 form을 customizing하여 사용
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model() # accounts.User을 반환하게 된다.
        fields = ['email', 'first_name', 'last_name', ]
        

# 커스터마이징한 유저모델을 인식하지 못해서 직접 get_user_model함수로
# 유저모델 정보를 넣어줌
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields