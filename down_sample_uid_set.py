import random

fchurn = open('churn_users.log','r')
ds_churn_rate = 0.5
ds_good_user_rate = 0.25
churn = []
for uid in fchurn:
    if random.uniform(0, 1) <= ds_churn_rate:
        churn.append(uid)
churn = set(churn)
print '# of churn users:',len(churn)

fplay = open('train_set.log','r')

train_uid = []
for uid in fplay:
    if uid in churn:
        train_uid.append(uid)
    else:
        if random.uniform(0,1) <= ds_good_user_rate:
            train_uid.append(uid)
print '# of train data:',len(train_uid)

file1 = open('ds_train_set.log','w')
for uid in train_uid:
	line = str(uid)
	file1.write(line)
file1.close()

file2 = open('ds_churn_users.log','w')
for uid in churn:
	l = str(uid)
	file2.write(l)
file2.close()

fplay.close()
fchurn.close()