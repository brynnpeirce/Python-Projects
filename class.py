#Class assignemnt


#created first class
class Tenant1:
    name = 'Cara'
    account_number = 1
    contact = '360-123-123'
#second class has inherited information from Tenant1   
class Rental_UnitA(Tenant1):
    rent = 1500.00
    rent_due = 'first of every month'
#third class has inherited information from Tenant1    
class Contract(Tenant1):
    contract_type = 'month to month'
    pets_allowed = 'yes'
    smoking = 'No'

