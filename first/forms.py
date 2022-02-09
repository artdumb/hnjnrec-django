
from django.forms import ModelForm
from first.models import Picdata, Placedata, Reviewdata, Password
from django.utils.translation import gettext_lazy as _
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Reviewdata
        fields = ['comment', 'password', 'pic', ]
        labels = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'comment': _('댓글'),
            'password': _('비밀번호')
        }
        help_texts = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'comment': _('댓글고고'),
            'password': _('삭제시 필요!')
        }
        widgets = {
            'pic': forms.HiddenInput(),
            'password': forms.PasswordInput()
        }


class PlacedataForm(ModelForm):
    class Meta:
        model = Placedata
        fields = ['place_name', 'password']
        labels = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'place_name': _('장소이름'),
            'password': _('비밀번호')
        }
        help_texts = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'place_name': _('장소이름을 입력해주세요'),
            'password': _('비밀번호를 입력해주세요'),
        }
        widgets = {
            'place_id': forms.HiddenInput(),
            'password': forms.PasswordInput()

        }


class PicdataForm(ModelForm):
    class Meta:
        model = Picdata
        fields = ['title', 'cam', 'film', 'lens',
                  'descrip', 'place_id', 'password']
        labels = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'title': _('제목'),
            'cam': _('카메라 바디'),
            'film': _('필름'),
            'lens': _('카메라 렌즈'),
            'descrip': _('설명'),
            'password': _('비밀번호')

        }
        help_texts = {
            # _는  gettext_lazy로 글자관련(다국어 등등) 유지보수를 위해 추가
            'title': _('제목을 입력해주세요.'),
            'cam': _('카메라 바디를 입력해주세요'),
            'film': _('필름을 입력해주세요'),
            'lens': _('카메라 렌즈을를입력해주세요'),
            'descrip': _('설명을 입력해주세요'),
            'password': _('비밀번호를 입력해주세용')

        }
        widgets = {
            'place_id': forms.HiddenInput(),
            'password': forms.PasswordInput()

        }
        error_message = {
            'title': {
                'max_length': _('설명이 너무 깁니다')
            },
            'cam': {
                'max_length': _('설명이 너무 깁니다')
            },
            'film': {
                'max_length': _('설명이 너무 깁니다')
            },
            'lens': {
                'max_length': _('설명이 너무 깁니다')
            },
            'descrip': {
                'max_length': _('설명이 너무 깁니다')
            },

        }
