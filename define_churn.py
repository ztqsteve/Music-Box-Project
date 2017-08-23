import pandas as pd

#search active users
schema_search = ['uid','os','date']
df_search = pd.read_csv('/Users/zhangtianqi/desktop/music_box_project/data/all_search.log',
                 delimiter='\t',header=None,index_col=None,names=schema_search)
if df_search['uid'].isnull().any():
	df_search = df_search[-df_search['uid'].isnull()]
df_search['date_obj'] = pd.to_datetime(df_search['date'])
df_search = df_search.set_index('date_obj')
df_search_train = df_search.ix['2017-03-30': '2017-04-21']
search_uid_train = set(df_search_train['uid'])
df_search_test = df_search.ix['2017-04-22': '2017-5-12']
search_uid_test = set(df_search_test['uid'])
print "search data loading finished"

#download active users
schema_down = ['uid','os','date']
df_down = pd.read_csv('/Users/zhangtianqi/desktop/music_box_project/data/all_down.log',
                 delimiter='\t',header=None,index_col=None,names=schema_down)
if df_down['uid'].isnull().any():
	df_down = df_down[-df_down['uid'].isnull()]
df_down['date_obj'] = pd.to_datetime(df_down['date'],format='%Y%m%d')
df_down = df_down.set_index('date_obj')
df_down_train = df_down.ix['2017-03-30': '2017-04-21']
down_uid_train = set(df_down_train['uid'])
df_down_test = df_down.ix['2017-04-22': '2017-5-12']
down_uid_test = set(df_down_test['uid'])
print "download data loading finished"


#play active users
schema_play = ['uid','os','date']
df_play = pd.read_csv('/Users/zhangtianqi/desktop/music_box_project/data/all_play.log',
                 delimiter='\t',header=None,index_col=None,names=schema_play)
if df_play['uid'].isnull().any():
	df_play = df_play[-df_play['uid'].isnull()]
df_play['date_obj'] = pd.to_datetime(df_play['date'],format='%Y%m%d')
df_play = df_play.set_index('date_obj')

df_play_train = df_play.ix['2017-03-30': '2017-04-21']
df_play_train['count'] = 1
df_play_train_count = df_play_train[['uid','count']].groupby('uid').sum()
df_play_train = df_play_train_count[df_play_train_count['count'] > 3]
play_uid_train = set(df_play_train.index)

df_play_test = df_play.ix['2017-04-22': '2017-5-12']
play_uid_test = set(df_play_test['uid'])
print "play data loading finished"

#define churn users

train_set = play_uid_train
print 'train set finished!'
test_set = play_uid_test.union(down_uid_test,search_uid_test)
print 'test set finished!'

churn_users = []
for user in train_set :
	if user not in test_set :
		churn_users.append(user)

print "churn users:",len(churn_users)
print "churn rate:",float(len(churn_users))/float(len(train_set))

f = open('churn_users.log','w')

for ur in churn_users :
	line = str(ur) + '\n'
	f.write(line)
print 'churn users have been recorded.'
f.close()

file = open('train_set.log','w')
for uid in train_set:
	line = str(uid) + '\n'
	file.write(line)
file.close()































