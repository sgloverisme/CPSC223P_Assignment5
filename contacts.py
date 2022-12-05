import json

class Contacts:
    def __init__(self, filename):
        self.filename=filename
        self.data={} #Set a member varialbe equal to an empty data dictionary.???
        try: 
            with open(filename, 'r') as f: #reading
                #json.load(f)  #loading into json
                self.data=json.load(f)
        except FileNotFoundError:
            pass

    def add_contact(self, id, first_name, last_name):

        exists = id in self.data
        if exists:
            return "error" 

        self.data[id]=[first_name, last_name]
        #self.sort_contacts()
        self.write_data()
        return self.data[id]      

    def modify_contact(self, id, first_name, last_name):
        exists = id in self.data

        if not exists:
            return "error"
        self.data[id]= [first_name, last_name]
        self.sort_contacts()
        self.write_data()
        return self.data[id]

    def delete_contact(self, id):
        exists=id in self.data 

        if not exists: 
            return "error"
        x= self.data.pop(id)
        self.write_data()
        return x 

    def write_data(self):
        with open(self.filename, 'w') as f:
             json.dump(self.data,f)

    
    def sort_contacts(self):
        l=[]
        for key in self.data:
            l.append(key, self.data[key][0], self.data[key][1])
        s=sorted(l, key= lambda x: (x[2], x[1])) #from library.  x[2] is the last name, x[1] is the first name 

        d={}

        for item in s:
            id=item[0] #key
            fn=item[1]
            ln=item[2]
            d[id] = [fn,ln]
            self.data[id]=d
            self.write_data()

            return self.data[id]