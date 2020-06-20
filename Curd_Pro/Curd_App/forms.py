from django import forms 

class Insert_Form(forms.Form):
	product_id=forms.IntegerField(
		label='Enter Your ID',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your ID'
			})
		)
	product_name=forms.CharField(
		label='Enter Your Name',
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Name'
			})
		)
	product_cost=forms.IntegerField(
		label='Enter Your Cost',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Cost'
			})
		)
	product_color=forms.CharField(
		label='Enter Your Color',
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Color'
			})
		)
	product_class=forms.CharField(
		label='Enter Your Class ',
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your class '
			})
		)
	custom_name=forms.CharField(
		label='Enter Custom Name',
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Custom Name'
			})
		)
	custom_mobile=forms.IntegerField(
		label='Enter Your Mobile ',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Mobile'
			})
		)
	custom_email=forms.EmailField(
		label='Enter Your Email ',
		widget=forms.EmailInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Email'
			})
		)

class Update_Form(forms.Form):
	product_id=forms.IntegerField(
		label='Enter Your ID',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your ID'
			})
		)

	product_cost=forms.IntegerField(
		label='Enter Your Cost',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your Cost'
			})
		)


class Delete_Form(forms.Form):
	product_id=forms.IntegerField(
		label='Enter Your ID',
		widget=forms.NumberInput(
			attrs={
			'class':'form-control',
			'placeholder':'Your ID'
			})
		)

