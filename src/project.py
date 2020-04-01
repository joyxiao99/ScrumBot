## @file project.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Project objects
#  @date Mar 21, 2020

from meetingList import MeetingList
from meeting import *
from sprint import *

## @brief Class representing Project objects
class Project():
    ## @brief Prject constructor
    #  @param n Name of project
    #  @param d Descripton of project
    def __init__(self, n, d=None):
        self.name = n
        self.desc = d
        self.meetings = MeetingList()
        self.rqes = []
        self.sprints = []
        self.c = 0

    ## @brief Accessor for description of project
    def get_desc(self):
        if (self.desc == None):
            return "No description"
        else:
            return self.desc

    ## @brief Accessor for name of project
    def get_name(self):
        return self.name

    ## @brief Accessor for meetings of project
    def get_meetings(self):
        return map(self.__get_meeting, self.meetings.to_seq())

    ## @brief Accessor for requirements of project
    def get_rqes(self):
        return self.rqes

    ## @brief Accessor for sprints of project
    def get_sprints(self):
        return map(self.__get_sprint, self.sprints)

    ## @brief Mutator for descripton of project
    #  @param desc New description for project
    def set_desc(self, desc=None):
        self.desc = desc

    ## @brief Mutator for adding meeting to project
    #  @param name Name of meeting
    #  @param datetime Time and date of meeting
    #  @param m_type Type of meeting
    #  @param desc Description of meeting
    def add_meeting(self, name, datetime, m_type, desc=None):
        meeting = Meeting(name, datetime, m_type, desc)
        self.meetings.add(meeting)

    ## @brief Mutator for adding a requirement to project
    #  @param s Requirement to be added
    def add_rqe(self, s):
        self.rqes.append(s)

    ## @brief Mutator for adding a sprint to project
    def add_sprint(self):
        sprint = Sprint()
        self.sprints.append(sprint)
        self.c = self.c + 1

    ## @brief Mutator for removing a meeting from project
    #  @param n Key-value of project to be removed
    def rm_meeting(self, n):
        try:
            self.meetings.remove(n)
        except KeyError as e:
            raise KeyError

    ## @brief Mutator for removing a requirement from project
    #  @param n Index of requirement to be removed
    def rm_rqe(self, n):
        self.rqes.pop(n)

    ## @brief Mutator for removing a sprint from project
    def rm_sprint(self):
        if (self.c==0):
            raise IndexError
        else:
            del self.sprints[-1]
            self.c = self.c - 1

    # Meeting inherited commands

    ## @brief Mutator for updating meeting description
    #  @param index Index of meeting
    #  @param desc Description of meeting
    def set_meeting_desc(self, id, desc=None):
        meeting = self.__get_meeting_by_id(id)
        if (not meeting):
            raise KeyError
        
        meeting.set_desc(desc)

    def get_meeting_name(self, id):
        meeting = self.__get_meeting_by_id(id)
        if (not meeting):
            raise KeyError
        
        return meeting.get_name() 

    def get_meeting_desc(self, id):
        meeting = self.__get_meeting_by_id(id)
        if (not meeting):
            raise KeyError
        
        return meeting.get_desc()

    # Sprint (and Task) inherited commands

    ## @brief Mutator for adding task to sprint
    #  @param name Name of Task
    #  @param deadline Deadline of Task
    #  @param details Details of Task
    def add_task(self, name, deadline, details=None):
        sprint = self.sprints[-1]
        sprint.add_task(name, deadline, details)
    
    ## @brief Accessor for getting tasks from sprint
    #  @param index Index of sprint
    def get_tasks(self, index):
        sprint = self.sprints[index]
        return sprint.get_tasks()

    ## @brief Mutator for removing a task from sprint
    #  @param Index of task
    def rm_task(self, index):
        sprint = self.sprints[-1]
        sprint.rm_task(index)
    
    ## @brief Mutator for adding feedback to a task
    #  @param index Index of task
    def add_feedback(self, index, feedback):
        sprint = self.sprints[-1]
        sprint.add_feedback(index, feedback)
    
    ## @brief Mutator for removing feedback from a task
    #  @param task_index Index of task
    #  @param feedback_index Feedback of task
    def rm_feedback(self, task_index, feedback_index):
        sprint = self.sprints[-1]
        sprint.rm_feedback(task_index, feedback_index)
    
    ## @brief Mutator for setting details for a task
    #  @param index Index of task
    #  @param details Details of task
    def set_details(self, index, details):
        sprint = self.sprints[-1]
        sprint.set_details(index, details)

    def __get_meeting(self, meeting):
        return (meeting.get_name(), meeting.get_datetime(), meeting.get_type())

    def __get_meeting_by_id(self, id):
        for i, j in self.meetings.to_seq():
            if (id == i):
                return j
        return None


    def __get_sprint(self, sprint):
        return sprint.get_date()
    