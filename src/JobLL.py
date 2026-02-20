class HeaderNode:
    def __init__(self, node_type: str, header: str):
        self.node_type = node_type
        self.header = header
    
    def change_type(self, new: str):
        self.node_type = new

    def change_header(self, new: str):
        self.header = new
    


        


class DescriptionNode:
    '''
    initialize role: Take values and put it as role
    Type: Header, Projects, Job Experience, Skills
    role: Role user took in
    Description: (String or List) What the user did at the job 
    '''
    def __init__(self, node_type: str, role: str, description, tags: list, desc_is_list=False):
        self.node_type = node_type
        self.role = role
        self.description = description
        self.desc_list = desc_is_list
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

    def edit_description(self, new: str, ind=-1):
        if not self.desc_list and ind < 0:
            raise "Description is not a list."
        elif not self.desc_list:
            self.description = new
        
        elif self.desc_list and ind < len(self.description):
            self.desc_list[ind] = new
        else:
            raise f"Index is larger than list length ({len(self.description)})."
            
    
    def __str__(self):
        return f"Role: {self.role}\nDescription: {self.description}\n" \
        f"Tags: {self.tags}\n"

    def latek_str(self):
        pass

    def job_match(self, tag: str):
        pass
    

    



