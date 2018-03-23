from random import randrange
def main():
    FN = ['Dominic', 'Brian', 'Letty', 'Mia', 'Han', 'Hobs', 'Sean', 'Jason', 'Vince', 'Tyrese' ]
    MN = [ 'NULL', 'Solo', 'Chris', 'Tyrone', 'Tyler', 'Reese', 'Parker', 'NULL', 'Janet', 'Leah']
    LN = ['Toretto', 'Santana', 'OConnor', 'Gibson', 'Statham', 'OBrian', 'Walker', 'Bourne', 'Beckford', 'Sharma']
    CourseType = ['Break', 'Weekend', 'Evening']
    Address = ['Moringside Ave', 'West Hill Dr', 'Challenger Crt', 'Coleraine Dr', 'Keeler Blvd', 'Harvest Moon Dr', 'Bissel Dr']
    Unit = ['NULL', 'NULL', '3', '31k','NULL',  '409','NULL',  '11A', 'NULL', '1507', '9j']
    PostalCode = ['A1A1A1', 'B2B2B2', 'C3C3C3', 'D4D4D4', 'E5E5E5', 'F6F6F6', 'G6G6G6']
    City = ['Toronto', 'Scarborough', 'Markham', 'Pickering']
    PhoneNumber1 = [ '1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777']
    PhoneNumber2 = [ 'NULL', '1111111111', 'NULL', '2222222222', 'NULL', '3333333333', 'NULL', '4444444444']
    Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',]
    Days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12','11', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27', '28']
  
    
    for i in range(500):
        IDNumbers = '2018'+ str(i+1)
        print 'INSERT INTO student VALUES ('+ "'" + IDNumbers +"'" +  ',' +"'" +  FN[randrange(0,10)] +"'" +  ',' +"'" +  MN[randrange(0,10)] +"'" +  ',' +"'" +  LN[randrange(0,10)]+"'" +  ',' +"'" +  CourseType[randrange(0,3)]+"'" +  ',' + "'" + str(randrange(1,500)) +' ' + Address[randrange(0,6)] +"'" +  ',' +"'" +  Unit[randrange(0,11)] +"'" +  ',' +"'" +  PostalCode[randrange(0,7)] +"'" +  ',' +"'" +  City[randrange(0,3)] +"'" +  ',' + PhoneNumber1[randrange(0,7)] + ',' + PhoneNumber2[randrange(0,8)] + ',' + str(randrange(1,10))+ ');'

    for i in range(1000):
        IDNumbersP = '2018'+ str(randrange(1,500))

        #print 'INSERT INTO payment VALUES (' + str(i+1) + ',' + IDNumbersP + ',' + 'DATE ' + "'"+ '2018-' + Months[randrange(0,11)] + '-' + Days[randrange(0,27)] + "'"+ ',' + str(randrange(0,400)) +');'


main()
