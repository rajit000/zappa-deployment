from django.db import connection, connections


def replace_null_with_empty_string_many(result):
    for dictionary in result:
        for i in dictionary:
            if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
                dictionary[i] = ''
            elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])              
    return result

def replace_null_with_empty_string(dictionary):
    for i in dictionary:
        if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
            dictionary[i] = ''
        elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])
    return dictionary

def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def StudentList_q():
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(""" Select * from localdb.Student where IsDeleted = 0""")
        if resp and cursor.rowcount:
            resp = dictfetchall(cursor)
        else:
            resp = None
    return resp

def StudentListCount_q():
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(""" Select count(co.Id) as count from ( Select * from localdb.Student where IsDeleted=0) co ; """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def StudentDetail_q(StudentUUID):
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(f""" Select * from localdb.Student where StudentUUID ='{StudentUUID}' and IsDeleted = 0 """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def StudentDetailDelete_q(StudentUUID):
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(f""" Update localdb.Student set IsDeleted = 1 where StudentUUID ='{StudentUUID}' """)
    return resp

def StudentDetailInsert_q(data):
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(""" Insert into localdb.Student (StudentUUID, FirstName, LastName, Class, Section, 
        City, District, State, Pincode, About, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy)
        Values(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",data)
    return resp

def OldStudentData_q(StudentUUID):
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(f""" Select * from localdb.Student where StudentUUID ='{StudentUUID}' and IsDeleted = 0 """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def StudentDetailsUpdate_q(data):
    with connections['mydb'].cursor() as cursor :
        resp = cursor.execute(""" Update localdb.Student Set FirstName =%s, LastName =%s, Class =%s, Section =%s, 
        City =%s, District =%s, State =%s, Pincode =%s, About =%s, UpdatedAt =%s, UpdatedBy =%s where StudentUUID = %s
        """,data)
    return resp