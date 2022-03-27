def triangle(s1,s2,s3):
    if s1>s2 and s1>s3:
        if s1<s2+s3:
            print('Forms triangle')
        else:
            print('not')
    elif s2>s3 and s2>s3:
        if s2<s1+s3:
            print('Forms triangle')
        else:
            print('not')
    elif s3>s2 and s3>s1:
        if s3<s2+s1:
            print('Forms triangle')
        else:
            print('not')
triangle(2,3,6)


            