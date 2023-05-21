'''
Let's take general example,
Ravi, Ananya and three friends wants to build House in same neighborhood. They consult an Engineer.

Engineer builds a blueprints and presents to Ravi and friends....

Now All friends loved one particular blueprint with little modification...

Now engineer being smart he made copies of that blueprint and adjusted a little and delivered it to these five friends.

Let's Understand technically,

Class: It is the blueprint with data and functions(method) binded together.
Object: It is copy of blueprint(class) with unique values.
'''


# creating class(blueprint) 
class House:
    '''
    This is a docstring for the HouseBlueprint class

    It can provide High level overview  of the class.
    Summary of class's purpose and functionalitys.
    Details about attributes, description about methods and their purposes.

    Its good practice to mention docstring, It's helpful to your juniors/seniors or anyother developer to understand.
    ----------------------------------------------------------------------------
                            a docstring will look like
    ----------------------------------------------------------------------------
    A class representing House.

    Attributes:
        project_number: identify house
        owner(str): name of person who owns property
        house_type(str): studio/1BHK/2BHK/3BHk..
    '''

    def __init__(self, project_number, owner, house_type): #self keyword here will represent the objects of class House. Also its not necessary that we name it self, first_argument with any name will represent object of class.
        '''
        Initializes a new instance of House class.

        Args:
            project_number: identify house
            owner(str): name of person who owns property
            house_type(str): studio/1BHK/2BHK/3BHk..
        '''
        self.project_number = project_number
        self.owner = owner
        self.house_type = house_type

    def get_info(self):
        '''
        Displays House Details.

        Prints:
            Project Number, House Owner and House Type.
        '''
        print(f"PROJECT: {self.project_number}")
        print(f"Owner: {self.owner} | House Type: {self.house_type}\n")


# create objects of House class (Ravi's and Ananya's House)
house_ravi = House("REN_001","Ravi","2BHK") # internally first argument(self) is passed as objects name, house_ravi
house_ananya = House("NEW_009","Ananya","3BHK")


# access objects function(method)
house_ravi.get_info()
house_ananya.get_info()

