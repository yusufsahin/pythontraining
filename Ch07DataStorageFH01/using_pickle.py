import pickle

data={'isim':'Alice','yas':25}

with open('data.pkl', 'wb') as f:
    pickle.dump(data,f,protocol=pickle.HIGHEST_PROTOCOL)

with open('data.pkl', 'rb') as f:
    loaded_data=pickle.load(f)
    print(loaded_data)