import customer_pb2 as helper
import revenue_pb2 as helper_2

from add_cust_data_serialized import product,customer,orderItem,order

#================OPTIONAL===================================
##additional code just to replicate same message

departments=[]
for i in range(200):
#adding sub department
    sub_dept=helper_2.Sub_Department()
    sub_dept.sub_dept_id=str(i)
    sub_dept.sub_dept_name=str("sub_dept_{}".format(i+1))
    sub_dept.order.CopyFrom(order)

##adding data
    department=helper_2.Department()
    department.dept_id=str(i)
    department.dept_name=str("dept_{}".format(i))
    department.sub_dept.extend([sub_dept])
    departments.append(department)


if __name__=='__main__':
    for i in range(len(departments)):
         print("=================\n" ,departments[i])