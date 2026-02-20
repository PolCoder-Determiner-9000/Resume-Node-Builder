class Job:
    '''
    initialize role: Take values and put it as role
    part: Header, Projects, Job Experience, Skills
    role: Role user took in
    Description:
    Tags: Languages, 
    '''
    def __init__(self, part: str, role: str, description: str, tags: list):
        self.part = part
        self.role = role
        self.description = description
        self.tags = tags if tags else []
    
    def remove_tags(self, remove: str):
        if remove.upper() not in [x.upper() for x in self.tags]:
            raise "Object not in tags."
        else:
            self.tags.remove(remove)

    def edit_tags(self, target: str, replace: str):
        if target.upper() not in [x.upper() for x in self.tags]:
            raise "item not in tags."
        else:
            target_i = self.tags.index(target)
            self.tags[target_i] = replace

    def edit_description(self, new: str):
        self.description = new
    
    def __str__(self):
        return f"Role: {self.role}\nDescription: {self.description}\n" \
        f"Tags: {self.tags}\n"

    def latek_str(self):
        pass

    def job_match(self, tag: str):
        pass
    

    



