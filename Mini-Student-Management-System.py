#Mini Student Management System



def Student_Management_System():
    
   Student_list = [] 
    
    
   def add_student():
       
       name = input("\nEnter your name: ")
       Last_name = input("Enter your last name: ")
       
       full_name = (f"{name} {Last_name}")
       
       while True:
         try :
           
             age = int(input("Enter your age: "))
             break
         except ValueError:
           
             print("\nNumbers only!")   
       
       course = input("Your course is:\n")
       
       while True:
       
         try:
             
            score = int(input("Your score is:\n"))
            break
         
         except ValueError:
             
             print("\nNumbers only!")
       
         
       
       student_data = {
           
          "Name": full_name,
          "Age": age,
          "Course": course,
          "Score": score 
           
           
       }
       
       Student_list.append(student_data)
       
       print("\nSuccessfully Added!")
    
   def view_students():
       
      if Student_list: 
          
         print("\n=============== The list ===============")
       
         for List_info in Student_list:
        
              Name = List_info["Name"]
              Age = List_info["Age"]
              Course = List_info["Course"]
              Score = List_info["Score"] 
           
              print(f"""
            
Name: {Name}
Age: {Age}
Course: {Course}
Score: {Score}    
           
               """)
      else:
          
          print("\nNo data yet")
          
       
          
          
   def Search_student():
       
       if Student_list:
           
           
           fname_input = input("\nYour full name:\n").strip()
           Found = False
           Partial_found = False
           for search_name in Student_list:
               
              Fullname = search_name["Name"]
           
              if fname_input.lower() == Fullname.lower():
                  
                  print("\nWe found your name!")
                  
                  
                      
                  Name = search_name["Name"]
                  Age = search_name["Age"]
                  Course = search_name["Course"]
                  Score = search_name["Score"] 
           
                  print(f"""
           
             
Name: {Name}
Age: {Age}
Course: {Course}
Score: {Score}    
           
                      """)
                  Found = True
                  break
                      
              elif fname_input.lower() in Fullname.lower().split():
                   
                   Partial_found = True       
           
           
               
                  
           
           if Partial_found:
               
               print("\nName is not in full name")
               
           else:
                
                print("\nNo matching name found!")      
           
           
           
           
       else:
           
           
           print("\nNo data yet")       
     
   def Delete_student():
        
        if Student_list:
            print("\nNote: Must include a full name")
            name_search = input("Enter your name: ").strip()
            
            
            Found = False
            Partial_found = False
            for search_name in Student_list:
                
                    Fullname = search_name["Name"]
                
                    if name_search.lower() == Fullname.lower():
                    
                        print("\nWe found your name:")
                    
                        
                        Name = search_name["Name"]
                        Age = search_name["Age"]
                        Course = search_name["Course"]
                        Score = search_name["Score"]
                        
                        print(f"""
              
                    
                        
Name: {Name}
Age: {Age}
Course: {Course}
Score: {Score}                        
                 
                        
                        """)
                        
                        
                        
                        for index, student_info in enumerate(Student_list):
                            
                          if student_info['Name'].lower() == name_search.lower():
                            
                            while True:
                              Delete_input = input(f"Are you sure you want to delete this information? 'Yes' or 'No'\nEnter: ").lower()
                            
                              if Delete_input == "yes":
                                
                                    
                                        
                                        del Student_list[index]
                                        print("\nSuccessfully deleted!")
                                        break
                                    
                                    
                                
                              elif Delete_input == "no":
                                
                                 print("\nLet's proceed")
                                 
                              
                              
                                
                              else:
                                
                                
                                
                                   print("\nPlease follow the given instruction")
                                
                        Found = True        
                        
                        
                        
                    elif name_search.lower() in Fullname.lower().split():
                         
                         Partial_found = True
                             
            
                
                   
                   
            if Partial_found:
                
                print("\nName is not in full name")   
               
            else:
                
                print("\nNo matching name found")     
                       
                   
        else:
            
            print("\nNo data yet")
        
               
   def show_menu():    
        
     print("\n1. Add Student")
     print("2. View Student")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Exit")
    
     return input("\nChoose option: ")
     
   while True:
    
     options = show_menu()

     if options == "1" or options == "Add student":
       
       add_student()
      
     elif options == "2" or options == "View student":
         
         view_students()
         
     elif options == "3" or options == "Search student":
         
         Search_student()
      
     elif options == "4" or options == "Delete student":
         
         Delete_student() 
         

     elif options == "5" or options == "Exit":
         
         print("\nGoodbye!")
         exit()
      
     else:
         
         print("\nPlease choose the option") 
         

Student_Management_System()    