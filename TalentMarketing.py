

class Skills():
    def __init__(self, id, name,category):
        self._id = id
        self._name = name
        self._category = category
    def setId(self,id):
        self._id = id
    def getId(self):
        return self._id
    def setName(self,name):
        self._name = name
    def getName(self):
        return self._name
    def setCategory(self,category):
        self._category = category
    def getCategory(self):
        return self._category



class Project():

    def __init__(self,id,name,duration,start_date,end_date,required_skills,location,description,is_complete):
        self._id = id
        self._name = name
        self._duration = duration
        self._start_date = start_date
        self._end_date = end_date
        self._required_skills = required_skills
        self._location = location
        self._description = description
        self._is_complete = is_complete

        self._requests = []
        self._members = []

    def addMember(self,employee):
        if employee not in self._members:
            self._members.append(employee)

    def deleteMember(self,employee):
        if employee in self._members:
            self._members.remove(employee)

    def Request(self,employee):
        if employee not in self._requests:
            self._requests.append(employee)
    def getRequest(self):
        return self._requests


class Assessment():
    def __init__(self,project_id,endosed_skills,feedback,rating):
        self._project_id = project_id
        self._endosed_skills = endosed_skills
        self._feedback = feedback
        self._rating = rating
    def getEndosedSkills(self):
        return self._endosed_skills

class User():
    def __init__(self,id,password,login_status,register_date,name,sex,birthday,role,email):
        self._id = id
        self._password = password
        self._login_status = login_status
        self._register_date = register_date
        self._name = name
        self._sex = sex
        self._birthday = birthday
        self._role = role
        self._email = email


class ProjectOwner(User):

    def __init__(self,id,password,login_status,register_date,name,sex,birthday,role,email):
        super().__init__(id,password,login_status,register_date,name,sex,birthday,role,email)

        self._projects = []

    def PostProject(self, project):
        ### post the project
        self._projects.append(project)

    def showRequests(self,project_id):
        for proj in self._projects:
            if proj.id == project_id:
                print(proj.getRequests)

    def Match(self,project_id, requested_employee):
        ### calculate the matching scores based on employee's interests and skills
        ### and the project's requirements
        ##project.required_skills
        pass

    def Accept(self,project_id, requested_employee):
        ### send message to employee ("Approval")
        for proj in self._projects:
            if proj.id == project_id:
                proj._members.append(requested_employee)

    def Deny(self,project_id, requested_employeee):
        ### send message to employee ("Deny")
        pass

    def Assess(self,employee, assessment):
        employee.completeProject(assessment)



class Employee(User):
    def __init__(self,id,password,login_status,register_date,name,sex,birthday,role,email):
        super().__init__(id,password,login_status,register_date,name,sex,birthday,role,email)
        self._skills  = []
        self._interests = []
        self._approved_projects = []
        self._completed_projects = []

    def addSkill(self, skill):
        if skill not in self._skills:
            self._skills.append(skill)

    def deleteSkill(self,skill):
        if skill in self._skills:
            self._skills.remove(skill)

    def addInterest(self,interest):
        if interest not in self._interests:
            self._interests.append(interest)

    def deleteInterest(self,interest):
        if interest in self._interests:
            self._interests.remove(interest)

    def applyProject(self, project_id):
        ### communication with project service, call the Request() function
        ### if approval, put the project on the projects list
        self._approved_projects.append(project_id)
        ### else, just return
        pass

    def completeProject(self,assess_results):
        self._completed_projects.append(assess_results)
        for skill in assess_results.getEndosedSkills():
            self.addSkill(skill)
