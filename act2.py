student_data = {'id1' :
    {'name': ['sara'],
     'class' : ['v'],
     'subject_intergration':['english, math, science']
     },
     'id2': 
     {'name': ['david'],
     'class' : ['v'],
     'subject_intergration':['english, math, science']
     },
     'id3':
         {'name': ['sara'],
     'class' : ['v'],
     'subject_intergration':['english, math, science']
     },
     'id4':
         {'name': ['surya'],
     'class' : ['v'],
     'subject_intergration':['english, math, science']
     },
    }
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)