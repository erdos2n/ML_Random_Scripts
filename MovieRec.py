import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM 

#fetch data and format

data = fetch_movielens(min_rating = 4.0)

#print high ratings

print(repr(data['train']))
print(repr(data['test']))

#create movie list

model = LightFM(loss = 'warp') #weight approx rank pairwise

#train model
model.fit(data['train'], epochs = 30, num_threads = 2)

def sample_recommendation(model, data, user_ids):
	#number of users and movies in training data
	n_users, n_items = data['train'].shape

	#generate recs
	for user_id in user_ids:
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#predicted movies
		scores = model.predict(user_id, np.arange(n_items))

		top_items = data['item_labels'][np.argsort(-scores)]

		print("User %s" % user_id)
		print("   Known positives:")

		for x in known_positives[:3]:
			print("     %s" % x)

		print("   Recommended")

		for x in top_items[:3]:
			print("     %s" % x)
#########################################################
#########################################################

sample_recommendation(model, data, [3, 25, 45, 101, 123])