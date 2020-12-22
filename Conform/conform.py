






def conform(hats):
    

    previous = hats[0]
    current_start = current_end = 0

    forward_intervals = []
    backward_intervals = []
    forward_count = backward_count = 0
    for i,hat in enumerate(hats):
        if hat != previous:
            if hat == 'B':
                forward_count += 1
                forward_intervals.append((current_start,current_end))
            else:
                backward_count += 1
                backward_intervals.append((current_start,current_end))
            current_start = current_end = i
        else:
            current_end += 1

        previous = hat


    if hat == 'B':
        backward_count +=1
    else:
        forward_count += 1

    intervals = forward_intervals if forward_count <= backward_count else backward_intervals

    for start,end in intervals:
        if start == end:
            message = f"Person in position {start}, please flip your cap!"
        else:
            message = f"Persons in positions {start} through {end}, please flip your caps!"

        print(message)


def conform_one_pass(caps):

    flip = 'F' if caps[0] == 'B' else 'B'


    
    start = None

    for i in range(1,len(caps)):
        cap = caps[i]
        if cap != flip:
            if start:
                if i - 1 != start:
                    print(f"Persons in positions {start} through {i -1}, please flip your caps!")
                else:
                    print(f"Person in position {start}, please flip your cap!")
                start = None
        else:
            if not start:
                start = i

def conform_bareheaded(hats):
    previous = hats[0]
    current_start = current_end = 0

    forward_intervals = []
    backward_intervals = []
    forward_count = backward_count = 0
    for i,hat in enumerate(hats):
        if hat != previous:
            if previous == 'F':
                forward_count += 1
                forward_intervals.append((current_start,current_end))
            elif previous == 'B':
                backward_count += 1
                backward_intervals.append((current_start,current_end))
            current_start = current_end = i
        else:
            current_end += 1

        previous = hat

    if hat == 'B':
        backward_count +=1
    elif hat == "F":
        forward_count += 1

    intervals = forward_intervals if forward_count <= backward_count else backward_intervals

    for start,end in intervals:
        if start == end:
            message = f"Person in position {start}, please flip your cap!"
        else:
            message = f"Persons in positions {start} through {end}, please flip your caps!"

        print(message)



def run_length_decoding(s):

    decoding = []

    i = 0


    while i < len(s):

        c = s[i]
        if c.isdigit():
            print('here')
            j = i + 1
            
            digit = [c]
            while j < len(s) and s[j].isdigit():
                digit.append(s[j])
                j += 1

        

            digit = int(''.join(digit))
            decoding.append(s[j] * digit)
            i = j + 1



    return ''.join(decoding)






def run_length_encoding(s):

    encoding = []
    
    previous = s[0]
    current_start = current_end = 0
    for i,c in enumerate(s):
        if c != previous:
            encoding.append(f"{i - 1 -  current_start + 1}{previous}")
            current_start = current_end = i
        else:
            current_end += 1

        previous =c 
    
    encoding.append(f"{current_end - 1- current_start + 1}{c}")

    return ''.join(encoding)


def run_length_encoding_2(s):
    # for one length characters don't add 1 


    encoding = []
    
    previous = s[0]
    current_start = current_end = 0
    for i,c in enumerate(s):
        if c != previous:
            encoding.append(f"{(i - 1 -  current_start + 1) if i - 1 != current_start else ''}{previous}")
            current_start = current_end = i
        else:
            current_end += 1

        previous =c 
    
    encoding.append(f"{(current_end - 1- current_start + 1) if current_end -  1  != current_start else ''}{c}")

    return ''.join(encoding)

def run_length_decoding_2(s):


    i = 0
    decoding = []
    while i < len(s):
        c = s[i]
        if c.isdigit():
            j = i + 1

            digit = [c]

            while j < len(s) and s[j].isdigit():
                digit.append(s[j])
                j += 1

            

            digit = int(''.join(digit))
            decoding.append(s[j] * digit)
            i = j + 1

        else:
            decoding.append(c)
            i += 1


    

    return ''.join(decoding)

















if __name__ == "__main__":

    s = "BWWWWWBWWWW"
    encoding = (run_length_encoding_2(s))
    print(encoding)
    decoding = run_length_decoding_2(encoding)

    print(decoding)
