import os
from csv import DictReader, writer
us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}
# emp_csv = os.path.join(r'python-challenge\pyboss\Resources\employee_data.csv')
e_name = []
e_dob = []
e_id = []
e_ssn = []
e_state = []
first = []
last = []
with open ("python-challenge/pyboss/Resources/employee_data.csv", "r") as csv_f:
    emp_file = DictReader(csv_f)

    for e_row in emp_file:
       e_name.append(e_row["Name"])
       e_dob.append( e_row["DOB"])
       e_id.append(e_row["Emp ID"])
       e_ssn.append(e_row["SSN"])
       e_state.append( e_row["State"])
def header():
    h = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    return h

def emp_id():
    return e_id

def name_split_first(fnme):
    fn= [i.split(' ')[0] for i in fnme]
    for j in range(len(fn)):
        first.append(fn[j])  
    return first

def name_split_last(lnme):
    ln= [i.split(' ')[1] for i in lnme]
    for j in range(len(ln)):
        last.append(ln[j])  
    return last

def date_fo_bitrh(dob):
    new_dob=[]
    for i in dob:
      new_dob.append(i.replace('-','/'))  
    return new_dob

def state_abv(sabv_dict,sabv):
    new_state = []
    for i in sabv:
        if i in sabv_dict:
            new_state.append(sabv_dict[i])
    return new_state       

def ssn_star(ssn):
    new_ssn=[]
    for i in range(len(ssn)):
        new_ssn.append("***-**"+str(ssn[i][6:]))
    return new_ssn
    
data = zip(emp_id(),name_split_first(e_name),name_split_last(e_name),date_fo_bitrh(e_dob),ssn_star(e_ssn),state_abv(us_state_abbrev,e_state))
with open("python-challenge/pyboss/Resources/Py_boss_output.csv","w", newline='') as pyfile:
    py_boss_write = writer(pyfile)
    py_boss_write.writerow(header())
    for w in data:
        py_boss_write.writerow(w)
