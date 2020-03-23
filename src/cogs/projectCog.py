## @file projectCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to projects.
#  @date Mar 12, 2020

import discord
from discord.ext import commands
import sys
sys.path.append("/mnt/c/Users/timch/Desktop/ScrumBot/src")

from project import *
from projectList import ProjectList
from meeting import *
import meetingTypes

import datetime as dt

## @brief Discord commands related to the creation, removal and modification of projects.
#  @details These commands are only to be used inside a guild.
class projectCog(commands.Cog, name="Project Commands"):
    def __init__(self, bot):
        self.project_list = ProjectList()
        self.bot = bot
    
    @commands.command(name="addMeeting", brief="Add a meeting to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_meeting(self, ctx, n: int, name, date, time, m_type, *, s=None):
        print(f'[Log] add_meeting from {ctx.author}, name: {name}, date: {date}, time: {time}, desc: {s} in project: {n}')
        date_val = [int(i) for i in date.split('/')]
        time_val = [int(i) for i in time.split(':')]

        d = dt.date(date_val[0], date_val[1], date_val[2])
        t = dt.time(time_val[0], time_val[1])
        m = MeetingTypes.from_str(m_type)
        meeting = Meeting(name, d, t, m, s)

        val = self.project_list.to_seq()[n][1]
        print(val)
        self.project_list.update(n, val.add_meeting(meeting))
        
        await ctx.send(f'> Added meeting **{name}** to project {n}')

    @commands.command(name="addProject", brief="Add a project to the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def add_project(self, ctx, name, *, desc=None):
        print(f'[Log] add_project from {ctx.author}, name: {name}, desc: {desc}')
        proj = Project(name, desc)
        self.project_list.add(proj)

        await ctx.send(f'> Added project **{name}**')

    @commands.command(name="addRqe", aliases=["addRequirement", "addReq"], brief="Add a requirement to a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def add_rqe(self, ctx, a: int, *s):
        raise NotImplementedError

    @commands.command(name="addSprint", brief="Add a sprint to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_sprint(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getProjectDesc", aliases=["getProjectDescription", "getProjDesc"], brief="Get the description of a project.")
    @commands.guild_only()
    async def get_project_desc(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getRqes", aliases=["getRequirements", "getReqs"], brief="Get the requirements of a project.")
    @commands.guild_only()
    async def get_rqes(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getSprints", brief="Get the sprints of a project.")
    @commands.guild_only()
    async def get_sprints(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="listMeetings", brief="List all meetings of a project.")
    @commands.guild_only()
    async def list_meetings(self, ctx, n: int):
        print(f'[Log] list_meetings from {ctx.author}, project: {n}')
        proj = self.project_list.to_seq()[n][1]
        print(proj.get_meetings())

        #seq = [f'id: {i} - name: {j.get_name()} - date: ' for i, j in proj.get_meetings()]
        #lst = '\n'.join(seq)

    @commands.command(name="listProjects", aliases=["listProject"], brief="List all projects in a guild.")
    @commands.guild_only()
    async def list_projects(self, ctx):
        print(f'[Log] list_projects from {ctx.author}')
        
        seq = [f'id: {i} - name: {j.get_name()} - desc: {j.get_desc()}' for i, j in self.project_list.to_seq()]
        lst = '\n'.join(seq)

        if (not seq):
            await ctx.send(f'> No current projects.')
            return

        embed = discord.Embed(title='List of Projects')
        embed.add_field(name='\uFEFF', value=lst)

        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmLastSprint", aliases=["removeLastSprint", "rmSprint", "removeSprint"], brief="Remove the last sprint of a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_last_sprint(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="rmMeeting", aliases=["removeMeeting"], brief="Removes a meeting from a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_meeting(self, ctx, a: int, b: int):
        raise NotImplementedError

    @commands.command(name="rmProject", aliases=["removeProject"], brief="Removes a project from the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def rm_project(self, ctx, n: int):
        print(f'[Log] rm_project from {ctx.author}, project: {n}')
        self.project_list.remove(n)
        await ctx.send(f'> Removed project {n}')

    @commands.command(name="rmRqe", aliases=["removeRqe", "rmReq", "rmRequirement"], brief="Removes a requirement from a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def rm_rqe(self, ctx, n: int, m: int):
        raise NotImplementedError

    @commands.command(name="setProjectDesc", aliases=["setProjectDescription"], brief="Set a description for a given project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def set_project_desc(self, ctx, n: int, *, s):
        print(f'[Log] set_project_desc from {ctx.author}, project: {n}, desc: {s}')
        val = self.project_list.to_seq()[n][1]

        self.project_list.update(n, Project(val.get_name(), s))
        await ctx.send(f'> Successfully updated description for project {n}.')

def setup(bot):
    bot.add_cog(projectCog(bot))