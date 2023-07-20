import sys

math_ops = ['+', '-', '*', '/', '&', '|', '^', '<<', '>>']
def calculate_24(target, input):
    cal([], input, 0, 0, 2*len(input)-1, target)


def evaluate(list, target):
    stack=[]
    count=0
    for i in list:
        if i in math_ops:
            if i=="<<":
                count+=1
                
            num1=stack.pop()
            num2=stack.pop()
            stack.append("({}{}{})".format(num2,i,num1))
        else:
            stack.append(str(i))
    if count>1:
        return
    try:
        if eval(stack[0])==target:
            print("{}={}".format(target,stack[0]))
            sys.exit(0)
    except SystemExit:
        sys.exit(0)
    except:
        pass
            


def cal(stack, input, n_op, n_num, max_stack_len, target):
    if len(stack) == max_stack_len:
        evaluate(stack, target)
        return
    if n_op+1 < n_num:
        for op in math_ops:
            cal(stack+[op], input, n_op+1, n_num, max_stack_len, target)
    for i in input:
        temp = [it for it in input]
        temp.remove(i)
        cal(stack+[i], temp, n_op, n_num+1, max_stack_len, target)


if __name__ == "__main__":
    calculate_24(24, [4,10,7,12])
