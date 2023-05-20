#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Insert name', job='Insert job'):
        self._name = name
        self._job = job

    def set_name(self, name):
        if type(name) != str or not (1 <= len(name) <= 25):
            print('Name must be string between 1 and 25 characters.')
        else:
            self._name = name
    
    def get_name(self):
        return self._name
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
            print('Setting new job.')
        else:
            print('Job must be in the list of approved jobs.')

    def get_job(self):
        return self._job


    name = property(get_name, set_name)
    job = property(get_job, set_job)

