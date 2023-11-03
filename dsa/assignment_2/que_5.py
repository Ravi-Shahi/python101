class Team:
    
    def __init__(self, *members):
        self.members = []
        for member in members:
            self.members.append(member)
    #add single member
    def addMember(self, member):
        self.members.append(member)
    #add bunch of member
    def addMembers(self,*members):
        for member in members:
            self.members.append(member)
    def getMembers(self):
        return self.members
    
try:
    team1 = Team('Ravi','Roshan','Ragahv','Rohit')
    print(team1.getMembers())
    team1.addMember('Ritesh')
    print(team1.getMembers())
    team1.addMembers('Honey','Badsh','Palash','Shivam','Kohli')
    print(team1.getMembers())
except Exception as e:
    print("Error occured!",e,"Debug it!")
    