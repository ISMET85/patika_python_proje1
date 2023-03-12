input =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output =[1,'a','cat',2,3,'dog',4,5]
def flatten_list(in_list, output_list):
    for item in in_list:
        if type(item) is list:
            flatten_list(item, output_list)
        else:
            output_list.append(item)
input_values = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]              
output_list=[]

flatten_list(input_values, output_list)
print(output_list)