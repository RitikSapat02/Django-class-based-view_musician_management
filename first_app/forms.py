
from django import forms
from first_app import models

'''
                #or
# from first_app.models import Album,Musicians


# class user_form(forms.Form):
    # user_name = forms.CharField(label = "Full Name" ,widget = forms.TextInput(attrs={'placeholder':'Enter your Full Name','style':'width:300px;color:red'}))

    # user_dob = forms.DateField(label="Date of birth",widget = forms.TextInput(attrs = {'type':'date'}))

    # user_email = forms.EmailField(required=False,label = "User Email",initial="abc@gmail.com")

    # boolean_field = forms.BooleanField(required = False)
    # char_field = forms.CharField(max_length = 15,min_length=5)
    # field = forms.ChoiceField(choices = (('','--select Option'),('1','First'),('2','Two'),('3','Three')))

    # choices = (('A','A'),('B','B'),('C','C'),)
    # radio = forms.ChoiceField(choices = choices,widget=forms.RadioSelect)

    # #validation code
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    # number_field = forms.IntegerField(validators = [validators.MaxValueValidator(10),validators.MinValueValidator(5)])

    # User_Email = forms.EmailField()
    # user_vmail = forms.EmailField()

    # def clean(self):
    #     all_cleaned_data = super().clean()
    #     user_vmail = all_cleaned_data['user_vmail']
    #     User_Email = all_cleaned_data['User_Email']

    #     if User_Email != user_vmail:
    #         raise forms.ValidationError("Fields dont match!!")

'''

##django model form
class MusicianForm(forms.ModelForm): #inherit 
    class Meta:  #if you want to define class inside a class so write class meta
        model = models.Musician      
        fields = "__all__"    #get allfields 

class AlbumForm(forms.ModelForm):
    release_date=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album   #get all data from album table
        fields = "__all__"       #get all fields