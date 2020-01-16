# import os
from csv import DictReader, writer
import operator


# Path to collect data from the Resources folder

# py_poll_csv = os.path.join(r'pypoll\election_data.csv')
voter = []
candidate = []
county = []
with open('pypoll/election_data.csv',"r") as py_file:
    py_poll = DictReader(py_file)
    for p_reader in py_poll:
        voter.append(p_reader["Voter ID"])
        candidate.append(p_reader["Candidate"])
        county.append(p_reader["County"])


br = "--------------------------------------"

def title():
    return "Election results"+"\n"+br

def total_votes(v):
    return "Total votes: " + str(len(v)) +"\n"+br

def tabulation(cndt,v):
    name = "O'Tooley"

    khan = f"Khan: {(cndt.count('Khan') / len(v) *100):.3f}% ({cndt.count('Khan')})"
    correy = f"Correy: {(cndt.count('Correy') / len(v) *100):.3f}% ({cndt.count('Correy')})"
    li = f"Li: {(cndt.count('Li') / len(v) *100):.3f}% ({cndt.count('Li')})"
    O_tooley = f"O'Tooley: {(cndt.count(name ) / len(v) *100):.3f}% ({cndt.count(name )})"
    br = "--------------------------------------"
    can_dict = {"Khan":cndt.count('Khan'),"Correy": cndt.count('Correy'),"Li":cndt.count('Li') , "O'Tooley": cndt.count(name ) }
    winner = f"Winner: {max(can_dict.items(), key=operator.itemgetter(1))[0]}"

    return khan + "\n" + correy + "\n" + li + "\n" + O_tooley + "\n" +br+"\n"+winner+"\n"+br

print(title())
print(total_votes(voter))
print(tabulation(candidate,voter))

with open("pypoll/Py_poll_output.csv","w") as file:
    py_poll_write = writer(file)
    py_poll_write.writerow([title()])
    py_poll_write.writerow([total_votes(voter)])
    py_poll_write.writerow([tabulation(candidate,voter)])
















