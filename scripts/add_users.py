import csv
from mainframe.models import User, Role

def run():
    fhand = open('mainframe/data/sample_users.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    User.objects.all().delete()
    Role.objects.all().delete()

    for row in reader:
        print(row)
        r, created = Role.objects.get_or_create(roleName=row[-1])
        u = User(username=row[0], first_name=row[1], last_name=row[2], email_id=row[3], country=row[4], joined_on=row[5], rating=row[7])
        u.save()
        print(r)
        u.roles.add(r)
