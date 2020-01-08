                                                                                                                                           
def calcualte_gross_salary(basic_salary):                                       
    hra = 0;                                                                    
    da = 0;     
    if (basic_salary < 2500):                                                   
        hra = (basic_salary * 10) / 100;                                        
        da = (basic_salary * 90) / 100;                                         
    else:                                                                       
        hra = 1000;                                                             
        da = (basic_salary * 95) / 100;                                         
                                                                                
    return (basic_salary + hra + da);                                           
if __name__ == "__main__":  
    basic_salary = float(input("Enter basic salary: "));                        
    gross_salary = calcualte_gross_salary(basic_salary);                        
    print("Gross Salary is: %f" % gross_salary);  
