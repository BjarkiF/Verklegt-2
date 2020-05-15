from django import forms
from django.forms import ModelForm
from items.models import Item, ItemManufacturer, ItemCategory


class EditItemForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":13,"cols":55,'style':'resize:none;'}))

    class Meta:
        model = Item
        fields = ('description', 'price')

class CreateItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateItemForm, self).__init__(*args, **kwargs)
        self.fields['manufacturer_id'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['category_id'].label_from_instance = lambda obj: "%s" % obj.name

    manufacturer_id = forms.ModelChoiceField(queryset=ItemManufacturer.objects.all())
    category_id = forms.ModelChoiceField(queryset=ItemCategory.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 9, 'cols':50, 'style':'resize:none;'}))
    img = forms.CharField(max_length=999, widget=forms.TextInput())

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category_id', 'manufacturer_id', 'img')