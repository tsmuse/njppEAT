from django.db import models

# An Application is a single submission. It is essentially the digital version of the paper form. 
# It has Child and Adult objects representing each child and adult on the application. It also has 
# data fields for the status of the family's participation in a public assistance program,the case number if 
# they participate, and all the information from the contact section of the paper form. There are also helper
# fields for the total of all child monthly income, the total of all adult monthly income, and the total 
# adult monthly income broken out by source. These will be 0 if no income information needed to be provided
class Application(models.Model):
    contact_address_one = models.CharField(max_length=200, blank=True)
    contact_address_two = models.CharField(max_length=200, blank=True)
    contact_city = models.CharField(max_length=50, blank=True) # as far as I can find no US city has name longer than 24 chars
    contact_state = models.CharField(max_length=2, blank=True)
    contact_zip = models.CharField(max_length=10, blank=True)
    contact_phone = models.CharField(max_length=10)
    contact_email = models.EmailField(blank=True)
    contact_name_of_filer = models.CharField(max_length=200)
    date_completed = models.DateTimeField()
    participate_assistance = models.BooleanField()
    assistance_case_number = models.CharField(max_length=50, blank=True) # i really hope this is long enough, otherwise ouch

    # NOTE: all income should be converted to monthly before being stored. All income values are monthly income.
    total_child_income = models.IntegerField(blank=True,null=True)
    total_adult_income = models.IntegerField(blank=True,null=True)
    total_adult_income_wages = models.IntegerField(blank=True,null=True)
    total_adult_income_assistance = models.IntegerField(blank=True,null=True)
    total_adult_income_other = models.IntegerField(blank=True,null=True)

    # this is a helper to make it easier to mess with the data in the console
    def __str__(self):
    	return self.contact_name_of_filer

# A Child is one child inside an Application. There will be at least one in every Application. Each Child has a 
# reference to it's Application, the child's name, the child's status as a student, foster child, & homeless/runaway/migrant
# as well as the child's monthly income broken down by source if income information was required to be submitted. 
class Child(models.Model):
	application = models.ForeignKey(Application)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1,blank=True)
	student = models.BooleanField()
	foster_child = models.BooleanField()
	homless = models.BooleanField()

	# NOTE: all income should be converted to monthly before being stored. All income values are monthly income.
	total_income = models.IntegerField(blank=True,null=True)
	work_income = models.IntegerField(blank=True,null=True)
	assitance_income = models.IntegerField(blank=True,null=True)
	other_income = models.IntegerField(blank=True,null=True) # Is this enough? Or shoudl it be outside_income && other_income?

	# this is a helper to make it easier to mess with the data in the console
	def __str__(self):
		return self.first_name + " " + self.last_name




# An Adult is one adult inside an Application. There may not be any Adult objects in an Application. There is no
# connection in the system between an Adult and the contact_name_of_filer. An Adult has a reference to it's Application
# the adult's name, the adult's income total and broken down by source, and possibly a SSN.
class Adult(models.Model):
	application = models.ForeignKey(Application)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	# NOTE: all income should be converted to monthly before being stored. All income values are monthly income.
	total_income = models.IntegerField(blank=True,null=True)
	work_income = models.IntegerField(blank=True,null=True)
	assitance_income = models.IntegerField(blank=True,null=True)
	other_income = models.IntegerField(blank=True,null=True)

	# this is a helper to make it easier to mess with the data in the console
	def __str__(self):
		return self.first_name + " " + self.last_name
